import pandas as pd
import numpy as np


class OutlierHandler:

    def __init__(self, df):
        self.df = df

    def identify_outliers(self, column, threshold=1.5):
        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR
        return (self.df[column] < lower_bound) | (self.df[column] > upper_bound)

    def remove_outliers(self, columns=None, threshold=1.5):
        if columns is None:
            columns = self.df.columns
        mask = pd.Series(False, index=self.df.index)
        for column in columns:
            mask |= self.identify_outliers(column, threshold)
        return self.df[~mask]

    def replace_outliers_with_iqr(self, columns=None, threshold=1.5):
        if columns is None:
            columns = self.df.columns
        for column in columns:
            outliers = self.identify_outliers(column, threshold)
            median = self.df[column].median()
            self.df.loc[outliers, column] = median
        return self.df
