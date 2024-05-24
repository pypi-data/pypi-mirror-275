import unittest
import pandas as pd
from data_cleaner_byzahid.date_time_handler import DateTimeHandler

class TestDateTimeHandler(unittest.TestCase):

    def setUp(self):
        """
        Create a sample dataframe for testing.
        """
        data = {
            'date': ['2024-05-20 12:45:35', '2023-06-14 15:30:00', '2022-07-25 09:15:20']
        }
        self.df = pd.DataFrame(data)
        self.handler = DateTimeHandler(date_column='date')

    def test_convert_to_datetime(self):
        df = self.handler.convert_to_datetime(self.df)
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(df['date']))

    def test_extract_date_parts(self):
        df = self.handler.convert_to_datetime(self.df)
        df = self.handler.extract_date_parts(df)
        self.assertIn('year', df.columns)
        self.assertIn('month', df.columns)
        self.assertIn('day', df.columns)
        self.assertIn('hour', df.columns)
        self.assertIn('minute', df.columns)
        self.assertIn('second', df.columns)

    def test_filter_by_date_range(self):
        """
        Test the filter_by_date_range method.
        """
        df = self.handler.convert_to_datetime(self.df)
        df_filtered = self.handler.filter_by_date_range(df, '2023-01-01', '2024-01-01')
        self.assertEqual(len(df_filtered), 1)
        self.assertEqual(df_filtered.iloc[0]['date'], pd.Timestamp('2023-06-14 15:30:00'))

    def test_add_days(self):
        """
        Test the add_days method.
        """
        df = self.handler.convert_to_datetime(self.df)
        df = self.handler.add_days(df, 10)
        self.assertEqual(df.iloc[0]['date'], pd.Timestamp('2024-05-30 12:45:35'))

if __name__ == '__main__':
    unittest.main()
