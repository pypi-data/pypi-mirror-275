from typing import Tuple

import torch

from internlm.accelerator import AcceleratorType, get_accelerator
from internlm.core.context import global_context as gpc
from internlm.utils.logger import get_logger

logger = get_logger(__file__)
internlm_accelerator = get_accelerator()

try:
    from torch_npu.optim import NpuFusedAdamW

    del NpuFusedAdamW

    npu_adamw_impl = True
except (ModuleNotFoundError, ImportError):
    npu_adamw_impl = False


# TODO: 给上次一个统一的接口，这些接口都能被下层的各种实现支持，哪些参数应该保留，那些参数应该省略？
def new_compatible_adamw(params, lr: float = 0.001, betas: Tuple[float, float] = (0.9, 0.999), eps: float = 1e-8):
    """
    return a compatibel adamw instance.
    """
    adam_extra_kwargs = {}
    backend = internlm_accelerator.get_accelerator_backend()

    if backend is AcceleratorType.GPU and torch.__version__ >= "2.1.0":
        if gpc.is_rank_for_log():
            logger.warning(
                "Use fused AdamaW to avoid nan grad norm when "
                "model size is larger and use_fp32_norm=True, Please note this!"
            )
        adam_extra_kwargs["fused"] = True
    elif backend is AcceleratorType.NPU:
        if gpc.is_rank_for_log():
            logger.warning(
                "Use normal AdamaW, NPU fused_adamw currently has"
                "accuracy issues and is not supported yet. Please note this!"
            )
        # TODO: support npu version adamw
    elif backend is AcceleratorType.DIPU:
        if gpc.is_rank_for_log():
            logger.warning("Use torch.optim.AdamW rather than deeplink adamw. Please note this!")
        # TODO: support deeplink version adamw
    else:
        if gpc.is_rank_for_log():
            logger.warning("Use torch.optim.AdamW rather than FusedAdamW. Please note this!")

    return torch.optim.AdamW(params, lr=lr, betas=betas, eps=eps, **adam_extra_kwargs)
