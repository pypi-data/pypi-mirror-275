import unittest
import pandas as pd
import numpy as np
from data_cleaner_byzahid.outlier_handler import OutlierHandler


class TestOutlierHandler(unittest.TestCase):

    def setUp(self):
        data = {
            'A': [1, 2, 3, 4, 100],
            'B': [1, -100, 3, 4, 5],
            'C': [1, 2, 3, 4, 5]
        }
        self.df = pd.DataFrame(data)
        self.handler = OutlierHandler(self.df.copy())

    def test_identify_outliers(self):
        outliers = self.handler.identify_outliers('A')
        expected = pd.Series([False, False, False, False, True], name='A')
        pd.testing.assert_series_equal(outliers, expected)

    def test_remove_outliers(self):
        df_no_outliers = self.handler.remove_outliers(columns=['A', 'B'])
        expected = self.df.drop([1, 4])
        pd.testing.assert_frame_equal(df_no_outliers, expected)

    def test_replace_outliers_with_iqr(self):
        df_replaced = self.handler.replace_outliers_with_iqr(columns=['A', 'B'])
        expected = self.df.copy()
        expected.loc[expected['A'] == 100, 'A'] = expected['A'].median()
        expected.loc[expected['B'] == -100, 'B'] = expected['B'].median()
        pd.testing.assert_frame_equal(df_replaced, expected)


if __name__ == '__main__':
    unittest.main()
