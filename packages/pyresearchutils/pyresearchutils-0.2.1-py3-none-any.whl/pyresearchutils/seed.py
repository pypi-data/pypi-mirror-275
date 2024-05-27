import random

import numpy as np
from pyresearchutils.logger import info
from pyresearchutils.constants import FOUND_PYTORCH

if FOUND_PYTORCH:
    import torch
else:
    torch = None


def set_seed(seed: int = 0):
    if FOUND_PYTORCH:
        torch.manual_seed(seed)
    random.seed(seed)
    np.random.seed(seed)
    info(f"Setting Random Seed to {seed}")
