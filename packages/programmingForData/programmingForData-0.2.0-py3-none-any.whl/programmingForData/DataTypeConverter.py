import pandas as pd


class DataTypeConverter:
    def convert_to_numeric(self, data, columns):
        for col in columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')
        return data

    def convert_to_categorical(self, data, columns):
        for col in columns:
            data[col] = data[col].astype('category')
        return data