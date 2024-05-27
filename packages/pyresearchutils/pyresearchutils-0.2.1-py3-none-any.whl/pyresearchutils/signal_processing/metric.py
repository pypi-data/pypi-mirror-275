import numpy as np
from pyresearchutils.constants import FOUND_PYTORCH
from pyresearchutils.logger import critical

if FOUND_PYTORCH:
    import torch
else:
    torch = None


def db(x):
    """

    Args:
        x:

    Returns:

    """
    if isinstance(x, np.ndarray):
        return 10 * np.log10(x)
    elif FOUND_PYTORCH and isinstance(x, torch.Tensor):
        return 10 * torch.log10(x)
    else:
        raise critical(f"Unknown input format of type {type(x)}")
