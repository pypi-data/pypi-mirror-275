import os

from pyresearchutils import logger
from pyresearchutils.seed import set_seed
from pyresearchutils.log_folder import generate_log_folder
from pyresearchutils.config_reader import ConfigReader
from pyresearchutils import constants

if constants.FOUND_WANDB:
    import wandb
else:
    wandb = None


def initialized_log(project_name: str, config_reader: ConfigReader = None,
                    enable_wandb: bool = False):
    """

    Args:
        project_name:
        config_reader:
        enable_wandb:

    Returns:

    """
    run_log_dir = None
    args = None
    if config_reader is not None:
        args = config_reader.get_user_arguments()

        os.makedirs(args.base_log_folder, exist_ok=True)
        run_log_dir = generate_log_folder(args.base_log_folder)

        logger.set_log_folder(run_log_dir)
        set_seed(args.seed)
        config_reader.save_config(run_log_dir)
        logger.info(f"Log Folder Set to {run_log_dir}")
    if constants.FOUND_WANDB and enable_wandb:
        wandb.init(project=project_name,
                   dir=args.base_log_folder if config_reader is not None else None)  # Set WandB Folder to log folder
        if config_reader is not None:
            wandb.config.update(config_reader.get_user_arguments())  # adds all of the arguments as config variables®
    if constants.FOUND_PYTORCH:
        from pyresearchutils.torch.working_device import get_working_device
        constants.DEVICE = get_working_device()
    return args, run_log_dir
