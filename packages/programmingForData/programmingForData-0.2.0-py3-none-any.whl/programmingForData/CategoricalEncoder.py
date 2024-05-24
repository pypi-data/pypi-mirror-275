import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder


class CategoricalEncoder:
    def __init__(self):
        self.one_hot_encoder = OneHotEncoder()
        self.label_encoder = LabelEncoder()

    def one_hot_encode(self, data, column):
        encoded = self.one_hot_encoder.fit_transform(data[[column]])
        # One-Hot Encoding işleminden dönen veriyi NumPy dizisine dönüştür
        encoded_array = encoded.toarray()
        # One-Hot Encoding işleminden dönen sütun adlarını belirle
        column_names = [f"{column}_{value}" for value in self.one_hot_encoder.categories_[0]]
        return pd.DataFrame(encoded_array, columns=column_names, index=data.index)

    def label_encode(self, data, column):
        data[column] = self.label_encoder.fit_transform(data[column])
        return data