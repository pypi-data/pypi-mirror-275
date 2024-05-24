import math
import numpy as np
import pandas as pd
import sklearn.preprocessing
import torch


def label_encoder(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encode categorical features (String) into integers (int).
    """
    cat_feats = [col for col in df.columns if df[col].dtypes == np.dtype('object')]
    for col in cat_feats:
        df[col] = sklearn.preprocessing.LabelEncoder().fit_transform(df[col])
    return df


def gen_scale_pos_weight(y_train) -> float:
    """
    This function computes a scaling factor to balance positive and negative samples.
    It's particularly useful when dealing with skewed datasets.
    """
    total_positive_samples = sum(y_train)
    total_negative_samples = len(y_train) - sum(y_train)
    scale_pos_weight = total_negative_samples / total_positive_samples
    return scale_pos_weight


class DataLoader:
    def __init__(self, lst: list = []):
        self.i = 0
        self._data = lst

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, lst: list):
        self._data = lst

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self._data):
            self.i += 1
            return self._data[self.i - 1]
        else:
            raise StopIteration


def data_iter(data: list, batch_size: int) -> DataLoader:
    """Split the original input data list into batches."""
    lst = []
    batch_num = math.floor(len(data) / batch_size)
    for i in range(batch_num):
        start, end = batch_size * i, batch_size * (i + 1)
        X = torch.tensor([e[0] for e in data[start:end]])
        y = torch.tensor([e[1] for e in data[start:end]])
        lst.append((X, y))

    return DataLoader(lst)