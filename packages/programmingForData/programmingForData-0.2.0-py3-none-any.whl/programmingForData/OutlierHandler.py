import pandas as pd


class OutlierHandler:
    def __init__(self):
        pass

    def iqr_outliers(self, data, column, threshold=1.5):
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (IQR * threshold)
        upper_bound = Q3 + (IQR * threshold)
        return data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]

    def replace_outliers_with_median(self, data, column, threshold=1.5):
        median = data[column].median()
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (IQR * threshold)
        upper_bound = Q3 + (IQR * threshold)
        data.loc[(data[column] < lower_bound) | (data[column] > upper_bound), column] = median
        return data