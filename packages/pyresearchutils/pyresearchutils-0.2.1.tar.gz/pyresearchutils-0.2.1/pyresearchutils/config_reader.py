import argparse
from argparse import Namespace
import os
import json

import copy

from pyresearchutils import constants


def _handle_boolean(input_dict):
    for name, c in input_dict.items():
        if isinstance(c, str):
            if c.lower() == "true":
                input_dict[name] = True
            if c.lower() == "false":
                input_dict[name] = False


class ConfigReader(object):
    def __init__(self):
        self.arg_dict = dict()
        self.enum_dict = dict()
        self.parameters = None

    def add_parameter(self, name, **kwargs):
        if name == constants.CONFIG:
            raise Exception(f"Cant user the argument named:{constants.CONFIG}")
        if kwargs.get('enum'):
            self.enum_dict[name] = kwargs.get('enum')
            kwargs.pop('enum')
        self.arg_dict.update({name: kwargs})

    def notebook_parameters(self, **kwargs):
        self.get_user_arguments()
        return self.parameters

    def _handle_enums(self, input_dict):
        for name, c in self.enum_dict.items():
            input_dict[name] = c[input_dict[name]]
        return input_dict

    def _handle_enums2str(self, input_dict):
        for name, c in self.enum_dict.items():
            input_dict[name] = input_dict[name].name
        return input_dict

    def get_user_arguments(self):
        if self.parameters is None:
            lcfg = self.load_config()  # Load Config from file
            argparser = argparse.ArgumentParser()
            for k, v in self.arg_dict.items():
                argparser.add_argument('--' + k, **v)
            parameters, _ = argparser.parse_known_args()
            parameters_dict = vars(parameters)
            for pname, pvalue in self.arg_dict.items():
                if parameters.__getattribute__(pname) == pvalue["default"] and lcfg.get(
                        pname) is not None:  # Same as defulat
                    parameters_dict[pname] = lcfg.get(pname)
            parameters_dict = self._handle_enums(parameters_dict)
            _handle_boolean(parameters_dict)
            self.parameters = Namespace(**parameters_dict)
        return self.parameters

    def save_config(self, folder):
        args = self.get_user_arguments()
        args = copy.deepcopy(args)
        args_dict = vars(args)
        args_dict = self._handle_enums2str(args_dict)
        with open(os.path.join(folder, 'run.config.json'), 'w') as outfile:
            json.dump(args_dict, outfile)

    def load_config(self):
        argparser = argparse.ArgumentParser()
        argparser.add_argument('--' + constants.CONFIG, type=str, required=False)
        config_args, _ = argparser.parse_known_args()
        config_file = config_args.__getattribute__(constants.CONFIG)
        if config_args.__getattribute__(constants.CONFIG) is None:
            return {}
        with open(config_file, 'r') as outfile:
            cfg = json.load(outfile)
        return cfg

    def decode_run_parameters(self, in_dict):
        new_dict = {}
        for k, v in self.arg_dict.items():
            if isinstance(v, dict):
                v = v["default"]
            if in_dict.get(k) is None:
                new_dict.update({k: v})
            else:
                new_dict.update({k: in_dict.get(k)})
            if self.enum_dict.get(k) is not None:
                new_dict[k] = new_dict[k].split(".")[-1]
        return Namespace(**self._handle_enums(new_dict))


def initialized_config_reader(default_base_log_folder=None):
    cr = ConfigReader()
    cr.add_parameter(constants.BASELOGFOLDER, default=default_base_log_folder, type=str)
    cr.add_parameter(constants.SEED, default=0, type=int)
    return cr
