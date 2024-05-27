from typing import List

import torch
from pyresearchutils.logger import info
from pyresearchutils import constants


def get_working_device():
    if constants.DEVICE is None:
        working_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        info("Current Working Device is set to:" + str(working_device))
        constants.DEVICE = working_device
        return working_device
    else:
        return constants.DEVICE


def update_device(*args) -> List:
    return [a.to(get_working_device()) for a in args]
