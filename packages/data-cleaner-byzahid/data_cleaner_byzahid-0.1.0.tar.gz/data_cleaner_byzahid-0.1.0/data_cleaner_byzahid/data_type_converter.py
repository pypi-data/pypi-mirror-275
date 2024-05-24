import pandas as pd


class DataTypeConverter:
    def __init__(self):
        pass

    def convert_to_numeric(self, data, columns, errors='raise'):

        for column in columns:
            data[column] = pd.to_numeric(data[column], errors=errors)
        return data

    def convert_to_categorical(self, data, columns):

        for column in columns:
            data[column] = data[column].astype('category')
        return data
