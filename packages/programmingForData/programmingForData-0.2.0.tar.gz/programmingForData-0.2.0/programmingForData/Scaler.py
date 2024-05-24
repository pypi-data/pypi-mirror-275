import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


class Scaler:
    def __init__(self):
        self.min_max_scaler = MinMaxScaler()
        self.standard_scaler = StandardScaler()

    def min_max_scale(self, data):
        numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
        return pd.DataFrame(self.min_max_scaler.fit_transform(data[numerical_columns]), columns=numerical_columns, index=data.index)

    def standard_scale(self, data):
        numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
        return pd.DataFrame(self.standard_scaler.fit_transform(data[numerical_columns]), columns=numerical_columns, index=data.index)