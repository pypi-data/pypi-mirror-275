#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import Dict, Optional

import torch
from torch import nn

from internlm.model.modules.linear import new_linear
from internlm.model.modules.utils import Silu
from internlm.utils.logger import get_logger

logger = get_logger(__file__)


def split_fused_mlp_weight(w1_w3):
    w1, w3 = torch.split(w1_w3, w1_w3.shape[0] // 2, dim=0)
    return w1, w3


def _mlp_pre_load_convert(
    module: "FeedForward", state_dict, prefix: str, *args, **kwargs  # pylint: disable=W0613
) -> None:
    w1_name, w3_name, fused_name = f"{prefix}w1.weight", f"{prefix}w3.weight", f"{prefix}fused_w1_w3.weight"

    if module.mlp_layer_fusion and fused_name not in state_dict:
        w1, w3 = state_dict.pop(w1_name), state_dict.pop(w3_name)
        state_dict[fused_name] = torch.cat([w1, w3], dim=0)

    if not module.mlp_layer_fusion and (w1_name not in state_dict or w3_name not in state_dict):
        state_dict[w1_name], state_dict[w3_name] = split_fused_mlp_weight(state_dict.pop(fused_name))


def _mlp_save_convert(module: "FeedForward", state_dict, prefix: str, *args, **kwargs) -> Dict:  # pylint: disable=W0613
    w1_name, w3_name, fused_name = f"{prefix}w1.weight", f"{prefix}w3.weight", f"{prefix}fused_w1_w3.weight"

    if module.mlp_layer_fusion:
        state_dict[w1_name], state_dict[w3_name] = split_fused_mlp_weight(state_dict.pop(fused_name))

    return state_dict


class FeedForward(nn.Module):
    """
    Base FeedForward in flash implementation.

    Args:
        in_features (int): size of each input sample
        hidden_features (int): size of hidden state of FFN
        out_features (int): size of each output sample
        bias (bool): Whether the bias is needed for linears. True by default. But it is typically set to False
                    in the config.
        device (Optional[Union[str, torch.device]]): The device will be used.
        dtype (Optional[torch.dtype]): The type of data.
        multiple_of (int): For efficient training. Reset the size of hidden feature. 256 by default.
        mlp_layer_fusion (Optional[Bool]):  Some linears without bias in FFN can be fused to reduce the comm cost of SP.
        activation_type (str): the activation function used for feed forward, "swiglu" by default.
    """

    def __init__(
        self,
        in_features: int,
        hidden_features: int,
        out_features: int = None,
        bias: bool = True,
        device: Optional[torch.device] = None,
        dtype: Optional[torch.dtype] = None,
        multiple_of: int = 256,
        mlp_layer_fusion: Optional[bool] = False,
        activation_type: str = "swiglu",
    ):
        super().__init__()

        # TODO: support gelu...
        assert activation_type in ("swiglu"), f"Unsupported activation type: {activation_type}"

        self.mlp_layer_fusion = mlp_layer_fusion

        hidden_features = multiple_of * ((hidden_features + multiple_of - 1) // multiple_of)

        if self.mlp_layer_fusion:
            assert bias is False, "Fuesd FeedForward only support bias is False."

            self.fused_w1_w3 = new_linear("w13", in_features, hidden_features * 2, bias, device=device, dtype=dtype)
            self.w2 = new_linear("w2", hidden_features, out_features, bias, device=device, dtype=dtype)

            self._register_load_state_dict_pre_hook(_mlp_pre_load_convert, with_module=True)
            self._register_state_dict_hook(_mlp_save_convert)
        else:
            self.w1 = new_linear("w1", in_features, hidden_features, bias, device=device, dtype=dtype)
            self.w2 = new_linear("w2", hidden_features, out_features, bias, device=device, dtype=dtype)
            self.w3 = new_linear("w3", in_features, hidden_features, bias, device=device, dtype=dtype)

    def forward(self, x):
        if not self.mlp_layer_fusion:
            w1_o = self.w1(x)
            w3_o = self.w3(x)
        else:
            fussed_out = self.fused_w1_w3(x)
            w1_o, w3_o = torch.split(fussed_out, fussed_out.shape[-1] // 2, dim=-1)
        out = self.w2(Silu(w1_o, w3_o))
        return out


def new_feed_forward(
    in_features: int,
    hidden_features: int,
    out_features: int = None,
    bias: bool = True,
    device: Optional[torch.device] = None,
    dtype: Optional[torch.dtype] = None,
    multiple_of: int = 256,
    mlp_layer_fusion: Optional[bool] = False,
    activation_type: str = "swiglu",
) -> FeedForward:
    return FeedForward(
        in_features, hidden_features, out_features, bias, device, dtype, multiple_of, mlp_layer_fusion, activation_type
    )
