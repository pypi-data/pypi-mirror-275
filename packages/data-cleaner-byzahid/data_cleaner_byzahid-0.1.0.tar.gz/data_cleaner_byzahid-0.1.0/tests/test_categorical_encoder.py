import unittest
import pandas as pd
from data_cleaner_byzahid.categorical_encoder import CategoricalEncoder


class TestCategoricalEncoder(unittest.TestCase):

    def setUp(self):
        self.encoder = CategoricalEncoder()

    def test_one_hot_encoding(self):
        data = pd.DataFrame({'color': ['red', 'blue', 'green', 'blue', 'red']})
        self.encoder.fit_one_hot(data)
        transformed_data = self.encoder.transform_one_hot(data)
        self.assertEqual(transformed_data.shape, (5, 3))

    def test_label_encoding(self):
        data = pd.Series(['red', 'blue', 'green', 'blue', 'red'])
        self.encoder.fit_label(data)
        transformed_data = self.encoder.transform_label(data)
        self.assertTrue((transformed_data == [2, 0, 1, 0, 2]).all())


if __name__ == '__main__':
    unittest.main()
