import unittest
import pandas as pd
from data_cleaner_byzahid.feature_engineer import FeatureEngineer


class TestFeatureEngineer(unittest.TestCase):
    def setUp(self):
        data = {
            'A': [1, 2, 3, 4, 5],
            'B': [5, 4, 3, 2, 1],
            'date': pd.date_range('2021-01-01', periods=5)
        }
        self.df = pd.DataFrame(data)
        self.fe = FeatureEngineer(self.df)

    def test_add_polynomial_features(self):
        df = self.fe.add_polynomial_features('A', degree=3)
        self.assertIn('A_poly_2', df.columns)
        self.assertIn('A_poly_3', df.columns)
        self.assertEqual(df['A_poly_2'][0], 1 ** 2)
        self.assertEqual(df['A_poly_3'][1], 2 ** 3)

    def test_add_interaction_features(self):
        df = self.fe.add_interaction_features('A', 'B')
        self.assertIn('A_x_B', df.columns)
        self.assertEqual(df['A_x_B'][0], 1 * 5)
        self.assertEqual(df['A_x_B'][1], 2 * 4)


if __name__ == '__main__':
    unittest.main()
