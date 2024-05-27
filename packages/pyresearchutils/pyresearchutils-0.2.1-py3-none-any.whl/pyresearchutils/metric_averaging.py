from typing import Dict

import numpy as np


class IsBest(object):
    def __init__(self):
        self.min_value = np.inf
        self.max_value = -np.inf
        self.is_last_best = False

    def update_value(self, value: float):
        """
        Update the last best, min value and max value using the current value.
        Args:
            value: A floating point value.

        Returns: None

        """
        self.is_last_best = self.is_best(value) # Update last best
        self.min_value = np.minimum(value, self.min_value)
        self.max_value = np.maximum(value, self.max_value)

    def is_best(self, value) -> bool:
        """
        This function check a given value is best.
        Args:
            value: A floating point value.

        Returns: a boolean stating it this is the best results so far.

        """
        return value <= self.min_value


class SingleMetricAveraging(object):
    def __init__(self):
        self.n: int = 0
        self.accumulator: float = 0

    def update_metric(self, value: float, n: int = 1):
        self.accumulator += value
        self.n += n

    @property
    def result(self) -> float:
        return self.accumulator / self.n


class MetricAveraging(object):
    def __init__(self):
        self.metric_dict: Dict[str, SingleMetricAveraging] = dict()
        self.best_dict: Dict[str, IsBest] = dict()

    def clear(self):
        self.update_best(self.result)
        self.metric_dict.clear()

    def results_str(self):
        # res=self.result
        temp_str = ""
        for k, v in self.result.items():
            temp_str += k + f"={v}, "
        return temp_str

    def _get_current_metric(self, name) -> SingleMetricAveraging:
        if self.metric_dict.get(name) is None:
            self.metric_dict.update({name: SingleMetricAveraging()})
        return self.metric_dict[name]

    def log(self, **kwargs):
        for k, v in kwargs.items():
            smv = self._get_current_metric(k)
            if isinstance(v, (tuple, list)):
                if len(v) == 2:
                    smv.update_metric(v[0], v[1])
                elif len(v) == 1:
                    smv.update_metric(v[0])
                else:
                    raise Exception('Metric Dict is illegal')
            else:
                smv.update_metric(v)

    @property
    def result(self) -> dict:
        return {k: v.result for k, v in self.metric_dict.items()}

    def update_best(self, results_dict: dict):
        for k, v in results_dict.items():
            if self.best_dict.get(k) is None:
                self.best_dict[k] = IsBest()
            self.best_dict[k].update_value(v)

    def is_best(self, name) -> bool:
        if len(self.best_dict) == 0:
            return True
        return self.best_dict[name].is_last_best
