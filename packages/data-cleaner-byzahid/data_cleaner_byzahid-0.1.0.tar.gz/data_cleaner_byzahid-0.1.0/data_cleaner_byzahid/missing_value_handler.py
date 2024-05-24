import pandas as pd
import numpy as np


class MissingValueHandler:

    def __init__(self, df):
        self.df = df

    def identify_missing(self):
        return self.df.isnull()

    def impute_mean(self, columns=None):
        if columns is None:
            columns = self.df.columns
        for column in columns:
            self.df[column].fillna(self.df[column].mean(), inplace=True)
        return self.df

    def impute_median(self, columns=None):
        if columns is None:
            columns = self.df.columns
        for column in columns:
            self.df[column].fillna(self.df[column].median(), inplace=True)
        return self.df

    def impute_constant(self, value, columns=None):
        if columns is None:
            columns = self.df.columns
        self.df.fillna(value, inplace=True)
        return self.df

    def drop_missing(self, axis=0, how='any'):
        self.df.dropna(axis=axis, how=how, inplace=True)
        return self.df
