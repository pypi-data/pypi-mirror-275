import pandas as pd
import numpy as np


class Scaler:

    def __init__(self, df):
        self.df = df

    def min_max_scale(self, columns=None):
        if columns is None:
            columns = self.df.columns
        for column in columns:
            min_value = self.df[column].min()
            max_value = self.df[column].max()
            self.df[column] = (self.df[column] - min_value) / (max_value - min_value)
        return self.df

    def standard_scale(self, columns=None):
        if columns is None:
            columns = self.df.columns
        for column in columns:
            mean = self.df[column].mean()
            std = self.df[column].std()
            self.df[column] = (self.df[column] - mean) / std
        return self.df
