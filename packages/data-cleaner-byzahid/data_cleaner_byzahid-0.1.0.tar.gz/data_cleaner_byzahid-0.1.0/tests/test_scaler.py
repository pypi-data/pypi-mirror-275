import unittest
import pandas as pd
from data_cleaner_byzahid.scaler import Scaler


class TestScaler(unittest.TestCase):

    def setUp(self):
        data = {
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50],
            'C': [100, 200, 300, 400, 500]
        }
        self.df = pd.DataFrame(data)
        self.scaler = Scaler(self.df.copy())

    def test_min_max_scale(self):
        df_scaled = self.scaler.min_max_scale(columns=['A', 'B'])
        expected = self.df.copy()
        expected['A'] = (expected['A'] - 1) / (5 - 1)
        expected['B'] = (expected['B'] - 10) / (50 - 10)
        pd.testing.assert_frame_equal(df_scaled, expected)

    def test_standard_scale(self):
        df_scaled = self.scaler.standard_scale(columns=['A', 'B'])
        expected = self.df.copy()
        expected['A'] = (expected['A'] - expected['A'].mean()) / expected['A'].std()
        expected['B'] = (expected['B'] - expected['B'].mean()) / expected['B'].std()
        pd.testing.assert_frame_equal(df_scaled, expected)


if __name__ == '__main__':
    unittest.main()
