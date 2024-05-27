import wandb
import os
import torch

from pyresearchutils.config_reader import ConfigReader


def load_run(in_run_name, in_project_name, in_user_name, in_cr: ConfigReader):
    api = wandb.Api()
    runs = api.runs(f"{in_user_name}/{in_project_name}")
    for run in runs:
        if run.name == in_run_name:
            return in_cr.decode_run_parameters(run.config), run
    return None, None


def download_file(in_run, in_file):
    if os.path.isfile(in_file):
        os.remove(in_file)
    in_run.file(in_file).download()


def load_model_weights(in_run, in_model, in_file_name):
    download_file(in_run, in_file_name)
    in_model.load_state_dict(torch.load(in_file_name))
