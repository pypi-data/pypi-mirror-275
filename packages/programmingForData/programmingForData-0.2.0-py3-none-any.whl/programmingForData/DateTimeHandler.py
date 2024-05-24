import pandas as pd


class DateTimeHandler:
    def extract_date_parts(self, data, column):
        data['year'] = data[column].dt.year
        data['month'] = data[column].dt.month
        data['day'] = data[column].dt.day
        return data

    def convert_to_datetime(self, data, column):
        data[column] = pd.to_datetime(data[column], dayfirst=True)
        return data