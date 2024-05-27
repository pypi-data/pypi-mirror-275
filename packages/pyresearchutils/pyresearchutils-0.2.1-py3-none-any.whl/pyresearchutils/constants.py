import importlib

FOUND_PYTORCH = importlib.util.find_spec("torch") is not None
FOUND_TF = importlib.util.find_spec("tensorflow") is not None
FOUND_WANDB = importlib.util.find_spec("wandb") is not None
CONFIG = "config_file"
BASELOGFOLDER = 'base_log_folder'
SEED = 'seed'
DEVICE = None
