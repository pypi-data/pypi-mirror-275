import unittest
import pandas as pd
import numpy as np
from data_cleaner_byzahid.missing_value_handler import MissingValueHandler


class TestMissingValueHandler(unittest.TestCase):

    def setUp(self):
        data = {
            'A': [1, 2, np.nan, 4, 5],
            'B': [np.nan, 2, 3, 4, 5],
            'C': [1, 2, 3, 4, np.nan]
        }
        self.df = pd.DataFrame(data)
        self.handler = MissingValueHandler(self.df.copy())

    def test_identify_missing(self):
        missing = self.handler.identify_missing()
        expected = pd.DataFrame({
            'A': [False, False, True, False, False],
            'B': [True, False, False, False, False],
            'C': [False, False, False, False, True]
        })
        pd.testing.assert_frame_equal(missing, expected)

    def test_impute_mean(self):
        df_imputed = self.handler.impute_mean()
        expected = self.df.copy()
        expected['A'].fillna(expected['A'].mean(), inplace=True)
        expected['B'].fillna(expected['B'].mean(), inplace=True)
        expected['C'].fillna(expected['C'].mean(), inplace=True)
        pd.testing.assert_frame_equal(df_imputed, expected)

    def test_impute_median(self):
        df_imputed = self.handler.impute_median()
        expected = self.df.copy()
        expected['A'].fillna(expected['A'].median(), inplace=True)
        expected['B'].fillna(expected['B'].median(), inplace=True)
        expected['C'].fillna(expected['C'].median(), inplace=True)
        pd.testing.assert_frame_equal(df_imputed, expected)

    def test_impute_constant(self):
        df_imputed = self.handler.impute_constant(0)
        expected = self.df.copy()
        expected.fillna(0, inplace=True)
        pd.testing.assert_frame_equal(df_imputed, expected)

    def test_drop_missing(self):
        df_dropped = self.handler.drop_missing(axis=0, how='any')
        expected = self.df.dropna(axis=0, how='any')
        pd.testing.assert_frame_equal(df_dropped, expected)


if __name__ == '__main__':
    unittest.main()
