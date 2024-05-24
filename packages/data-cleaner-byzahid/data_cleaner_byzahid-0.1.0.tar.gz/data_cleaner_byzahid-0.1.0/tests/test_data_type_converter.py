import unittest
import pandas as pd
from data_cleaner_byzahid.data_type_converter import DataTypeConverter  # Replace with the actual module name


class TestDataTypeConverter(unittest.TestCase):
    def setUp(self):
        # Create a DataFrame for testing
        self.data = pd.DataFrame({
            'A': ['1', '2', '3', '4'],
            'B': ['a', 'b', 'c', 'd'],
            'C': ['1.1', '2.2', '3.3', '4.4'],
            'D': ['10', '20', '30', 'NaN']
        })
        self.converter = DataTypeConverter()

    def test_convert_to_numeric(self):
        # Test numeric conversion
        result = self.converter.convert_to_numeric(self.data.copy(), ['A', 'C'])
        self.assertTrue(pd.api.types.is_numeric_dtype(result['A']))
        self.assertTrue(pd.api.types.is_numeric_dtype(result['C']))

        # Test error handling with 'coerce'
        result = self.converter.convert_to_numeric(self.data.copy(), ['D'], errors='coerce')
        self.assertTrue(pd.api.types.is_numeric_dtype(result['D']))
        self.assertTrue(result['D'].isna().iloc[3])  # Check if NaN is properly coerced

    def test_convert_to_categorical(self):
        # Test categorical conversion
        result = self.converter.convert_to_categorical(self.data.copy(), ['B'])
        self.assertTrue(pd.api.types.is_categorical_dtype(result['B']))

    def test_invalid_column(self):
        # Test with invalid column
        with self.assertRaises(KeyError):
            self.converter.convert_to_numeric(self.data.copy(), ['X'])
        with self.assertRaises(KeyError):
            self.converter.convert_to_categorical(self.data.copy(), ['Y'])


if __name__ == '__main__':
    unittest.main()
