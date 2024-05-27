import numpy as np
from torch.utils.data.dataset import Dataset


class NumpyDataset(Dataset):
    def __init__(self, data, label, transform, metadata=None, extend=None):
        self.data = data
        self.label = label
        self.metadata = metadata
        self.transform = transform
        self.n = len(data)
        self.extend = extend

    def set_transform(self, transform):
        self.transform = transform

    def __getitem__(self, index):
        index = index % self.n
        d = self.data[index]
        if self.transform is not None:
            d = self.transform(d)
        l = self.label[index]
        if self.metadata is None:
            return d, l
        else:
            return d, l, self.metadata[index]

    def __len__(self):
        return self.n if self.extend is None else self.extend

    def get_min_max_vector(self):
        x = np.stack(self.data)
        return np.min(x, axis=0).astype("float32"), (np.max(x, axis=0) - np.min(x, axis=0)).astype("float32")
