import torch
import numpy as np
from typing import Any
from pyresearchutils.torch.working_device import get_working_device


def change2torch(x: Any) -> torch.Tensor:
    """

    Args:
        x:

    Returns:

    """
    if isinstance(x, torch.Tensor):  # If is tensor return
        return x
    if isinstance(x, (float, int)):  # Change float to tensor
        x = [x]
    return torch.tensor(x).to(get_working_device())


def torch2numpy(x: torch.Tensor) -> np.ndarray:
    return x.detach().cpu().numpy()
