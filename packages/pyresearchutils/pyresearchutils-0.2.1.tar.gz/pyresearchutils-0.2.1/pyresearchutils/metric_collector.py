class MetricCollector(object):
    def __init__(self):
        self.data_dict = dict()

    def clear(self):
        self.data_dict.clear()

    def insert(self, **kwargs):
        for k, v in kwargs.items():
            if self.data_dict.get(k) is None:
                self.data_dict.update({k: [v]})
            else:
                self.data_dict[k].append(v)

    def __getitem__(self, item):
        return self.data_dict[item]
