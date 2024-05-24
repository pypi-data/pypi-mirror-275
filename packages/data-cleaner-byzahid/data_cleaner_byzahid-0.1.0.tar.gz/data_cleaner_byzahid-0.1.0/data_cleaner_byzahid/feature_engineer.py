import pandas as pd
import numpy as np


class FeatureEngineer:
    def __init__(self, df):
        self.df = df

    def add_polynomial_features(self, column, degree=2):
        for d in range(2, degree + 1):
            self.df[f'{column}_poly_{d}'] = self.df[column] ** d
        return self.df

    def add_interaction_features(self, column1, column2):
        self.df[f'{column1}_x_{column2}'] = self.df[column1] * self.df[column2]
        return self.df
