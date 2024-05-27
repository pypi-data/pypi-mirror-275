import numpy as np
from typing import Dict, List
import pickle
from pyresearchutils.logger import critical


class MetricLister:
    def __init__(self, data=None):
        if data is None:
            self.data: Dict[str, List] = dict()
        else:
            self.data = data

    def add_value(self, **kwargs):
        for k, v in kwargs.items():
            if self.data.get(k) is None:
                self.data.update({k: [v]})
            else:
                self.data[k].append(v)

    def get_array(self, name):
        if self.data.get(name) is None:
            critical(f"Can't find parameter{name}")
        return np.asarray(self.data[name])

    def save2disk(self, location):
        # Open a file and use dump()
        with open(location, 'wb') as file:
            # A new file will be created
            pickle.dump(self.data, file)

    @staticmethod
    def load_data(location):
        with open(location, 'rb') as file:
            # A new file will be created
            data = pickle.load(file)
        return MetricLister(data)

    def print_last(self):
        for k, v in self.data.items():
            print(k, "=", v[-1])
