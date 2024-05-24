import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np


class Scaler:

    @staticmethod
    def standardize_data(data):

        mean = np.mean(data, axis=0)
        std = np.std(data, axis=0)
        scaled_data = (data - mean) / std
        return pd.DataFrame(scaled_data, columns=data.columns)

    @staticmethod
    def standardize_data2(data):

        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(data)
        return pd.DataFrame(scaled_data, columns=data.columns)

    @staticmethod
    def normalize_data(data):

        min_vals = np.min(data, axis=0)
        max_vals = np.max(data, axis=0)
        scaled_data = (data - min_vals) / (max_vals - min_vals)
        return pd.DataFrame(scaled_data, columns=data.columns)

    @staticmethod
    def normalize_data2(data):
        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(data)
        return pd.DataFrame(scaled_data, columns=data.columns)
