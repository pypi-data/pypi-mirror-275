import pandas as pd


class DateTimeHandler:
    def __init__(self, date_column):
        self.date_column = date_column

    def convert_to_datetime(self, df, format=None):
        df[self.date_column] = pd.to_datetime(df[self.date_column], format=format, errors='coerce')
        return df

    def extract_date_parts(self, df):
        df['year'] = df[self.date_column].dt.year
        df['month'] = df[self.date_column].dt.month
        df['day'] = df[self.date_column].dt.day
        df['hour'] = df[self.date_column].dt.hour
        df['minute'] = df[self.date_column].dt.minute
        df['second'] = df[self.date_column].dt.second
        return df

    def filter_by_date_range(self, df, start_date, end_date):
        mask = (df[self.date_column] >= pd.to_datetime(start_date)) & (df[self.date_column] <= pd.to_datetime(end_date))
        return df.loc[mask]

    def add_days(self, df, days):
        df[self.date_column] = df[self.date_column] + pd.to_timedelta(days, unit='d')
        return df
