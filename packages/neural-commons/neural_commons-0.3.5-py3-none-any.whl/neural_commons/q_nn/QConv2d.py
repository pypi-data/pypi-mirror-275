import math
from typing import Union
import torch
import torch.nn.functional as F
from neural_commons.cf_nn import CFModule
from neural_commons.helpers.torch_helper import ridge_regression
from neural_commons.q_nn import ParamModule

_size_2_t = Union[int, tuple[int, int]]
_sqrt_2 = math.sqrt(2)


class QConv2d(CFModule):
    def __init__(self, in_channels: int, out_channels: int,
                 kernel_size: _size_2_t,
                 stride: _size_2_t = 1,
                 padding: _size_2_t = 0,
                 dilation: _size_2_t = 1,
                 bias: bool = True,
                 norm_output: bool = True,
                 ):
        super().__init__(norm_output=norm_output)
        if isinstance(kernel_size, int):
            kernel_size = (kernel_size, kernel_size,)
        if isinstance(stride, int):
            stride = (stride, stride,)
        if isinstance(dilation, int):
            dilation = (dilation, dilation,)
        bias_param = None if not bias else torch.randn((out_channels,)) / _sqrt_2
        inv_scale = math.sqrt(in_channels * math.prod(kernel_size))
        if bias:
            inv_scale *= _sqrt_2
        weight = torch.randn((out_channels, in_channels, *kernel_size)) / inv_scale
        p_tensors = [weight]
        if bias_param is not None:
            p_tensors.append(bias_param)
        self.bias = bias
        self.p_module = ParamModule(p_tensors)
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.dilation = dilation
        self.padding = padding

    def forward(self, x: torch.Tensor):
        if self.bias:
            w, b = self.p_module()
        else:
            w = self.p_module()[0]
            b = None
        return torch.conv2d(x, w, b, self.stride, self.padding, self.dilation,
                            groups=1)
