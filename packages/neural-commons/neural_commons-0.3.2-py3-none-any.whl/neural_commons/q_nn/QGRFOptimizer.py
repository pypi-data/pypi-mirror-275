import math
from typing import Iterable, Protocol, Union, Optional
import torch
from torch import autograd

from neural_commons.helpers.torch_helper import rms
from neural_commons.q_nn import ParamModule


class _TLossFn1(Protocol):
    def __call__(self) -> torch.Tensor:
        ...


class _TLossFn2(Protocol):
    def __call__(self, **kwargs) -> torch.Tensor:
        ...


_TLossFn = Union[_TLossFn1, _TLossFn2]


class QGRFOptimizer:
    def __init__(self, p_modules: Iterable[ParamModule], stochastic_selection: bool = False):
        self.p_modules = list(p_modules)
        if len(self.p_modules) == 0:
            raise ValueError("Empty collection of ParamModules provided.")
        self.selected_index = -1
        self.stochastic_selection = stochastic_selection

    @classmethod
    def _lr_loss_grad(cls, fwd_fn: _TLossFn, sm: ParamModule, p_grads: tuple[torch.Tensor, ...],
                      lr: float, l1_lambda: float, l2_lambda: float, dev: torch.device,
                      **kwargs) -> tuple[float, float]:
        lr_t = torch.tensor(lr, device=dev, dtype=torch.float).requires_grad_()
        sm.set_gradient(p_grads, lr_t)
        try:
            lr_loss = cls._fwd_loss(fwd_fn, sm, l1_lambda, l2_lambda, **kwargs)
            lr_grad = autograd.grad(lr_loss, lr_t)[0]
            return lr_loss.item(), lr_grad.item(),
        finally:
            sm.clear_gradient()

    @classmethod
    def _simple_loss(cls, fwd_fn: _TLossFn, sm: ParamModule, p_grads: tuple[torch.Tensor, ...],
                     lr: float, l1_lambda: float, l2_lambda: float,
                     dev: torch.device, **kwargs) -> float:
        with torch.no_grad():
            lr_t = torch.tensor(lr, device=dev, dtype=torch.float)
            sm.set_gradient(p_grads, lr_t)
            try:
                lr_loss = cls._fwd_loss(fwd_fn, sm, l1_lambda, l2_lambda, **kwargs)
                return lr_loss.item()
            finally:
                sm.clear_gradient()

    @staticmethod
    def _optimal_lr(lr1: float, lr2: float, lr_loss1: float, lr_loss2: float,
                    lr_grad1: float, lr_grad2: float, lr_expansion: float) -> tuple[float, Optional[float]]:
        if math.isinf(lr_grad2) or math.isnan(lr_grad2):
            return lr1, 1.0 / lr_expansion,
        elif math.copysign(1, lr_grad1) != math.copysign(1, lr_grad2):
            # Secant root-finding method
            return (lr1 * lr_grad2 - lr2 * lr_grad1) / (lr_grad2 - lr_grad1), None,
        elif lr_loss2 == lr_loss1:
            return lr1, 1.0,
        elif lr_loss2 < lr_loss1:
            return lr2, lr_expansion,
        else:
            return lr1, 1.0 / lr_expansion,

    def _update_pm(self, pm: ParamModule, p_grads: tuple[torch.Tensor, ...],
                   lr: float, update_rate: float,
                   prior_approx_lr: float, approx_lr_factor: float,
                   max_change: float):
        if approx_lr_factor is not None:
            new_approx_lr = prior_approx_lr * approx_lr_factor
        else:
            new_approx_lr = lr
        pm.update_approx_lr(new_approx_lr)
        if lr == 0:
            return
        with torch.no_grad():
            eff_lr = lr * update_rate
            increments = []
            m_tensors = pm.tensors
            g: torch.Tensor
            for g, t in zip(p_grads, m_tensors):
                change = -g * eff_lr
                max_change_rms = rms(t) * max_change
                change_rms = rms(change)
                if change_rms > max_change_rms:
                    change *= max_change_rms / change_rms
                increments.append(change)
            pm.increment_tensors(increments)

    @staticmethod
    def _get_extra_loss(sm: ParamModule, l1_lambda: float,
                        l2_lambda: float) -> torch.Tensor:
        fixed_tensors = sm.tensors
        live_tensors = sm()
        elem_count = 0
        sq_value_sums = []
        abs_value_sums = []
        for lt, ft in zip(live_tensors, fixed_tensors):
            elem_count += torch.numel(lt)
            sq_value_sums.append(torch.sum(lt.pow(2)).view(1))
            abs_value_sums.append(torch.sum(torch.abs(lt)).view(1))
        mean_sq_value = torch.sum(torch.cat(sq_value_sums)) / elem_count
        mean_abs_value = torch.sum(torch.cat(abs_value_sums)) / elem_count
        return l1_lambda * mean_abs_value + l2_lambda * mean_sq_value

    @classmethod
    def _fwd_loss(cls, fwd_fn: _TLossFn, sm: ParamModule,
                  l1_lambda: float, l2_lambda: float, **kwargs):
        return fwd_fn(**kwargs) + cls._get_extra_loss(sm, l1_lambda, l2_lambda)

    def get_approx_lr(self, sm: ParamModule):
        return sm.approx_lr_ma

    def _step(self, fwd_fn: _TLossFn, sm: ParamModule, update_rate: float,
              l1_lambda: float, l2_lambda: float, max_change: float,
              lr_expansion: float = 2.0, **kwargs):
        loss = self._fwd_loss(fwd_fn, sm, l1_lambda, l2_lambda, **kwargs)
        dev = loss.device
        p_grads = sm.grad(loss)
        p_grads = tuple(g.detach() for g in p_grads)
        loss = loss.item()
        approx_lr = self.get_approx_lr(sm)
        lr1 = 0
        lr2 = approx_lr * 2.0
        lr_loss1, lr_grad1 = self._lr_loss_grad(fwd_fn, sm, p_grads, lr1,
                                                l1_lambda, l2_lambda,
                                                dev, **kwargs)
        lr_loss2, lr_grad2 = self._lr_loss_grad(fwd_fn, sm, p_grads, lr2,
                                                l1_lambda, l2_lambda,
                                                dev, **kwargs)
        opt_lr, approx_lr_factor = self._optimal_lr(lr1, lr2, lr_loss1, lr_loss2, lr_grad1, lr_grad2,
                                                    lr_expansion=lr_expansion)
        if approx_lr_factor is None:
            if self._simple_loss(fwd_fn, sm, p_grads, opt_lr, l1_lambda, l2_lambda,
                                 dev, **kwargs) > lr_loss1:
                # Failed to decrease loss. Reduce approx LR.
                opt_lr = lr1
                approx_lr_factor = 1.0 / lr_expansion
        self._update_pm(sm, p_grads, opt_lr, update_rate, approx_lr, approx_lr_factor,
                        max_change=max_change)
        return loss

    def step(self, fwd_fn: _TLossFn, update_rate: float = 1.0, l1_lambda: float = 0.001,
             l2_lambda: float = 0.001, max_change: float = 0.3, **kwargs) -> float:
        if update_rate <= 0 or update_rate > 1.0:
            raise ValueError("update_rate expected to be in ]0, 1].")
        p_modules = self.p_modules
        num_modules = len(p_modules)
        if self.stochastic_selection:
            m_lr = [m.approx_lr_ma for m in p_modules]
            m_lr = torch.tensor(m_lr, dtype=torch.float)
            m_weight = torch.log1p(m_lr)
            self.selected_index = torch.multinomial(m_weight, 1).item()
        else:
            self.selected_index = (self.selected_index + 1) % num_modules
        selected_module = p_modules[self.selected_index]
        return self._step(fwd_fn, selected_module,
                          update_rate=update_rate,
                          l1_lambda=l1_lambda, l2_lambda=l2_lambda,
                          max_change=max_change,
                          **kwargs)
