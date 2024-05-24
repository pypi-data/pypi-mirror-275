class MissingValueHandler:
    def __init__(self):
        pass

    def fill_mean(self, data, columns):
        for column in columns:
            mean_value = data[column].mean()
            data[column] = data[column].fillna(mean_value)
        return data

    def fill_median(self, data, columns):
        for column in columns:
            median_value = data[column].median()
            data[column] = data[column].fillna(median_value)
        return data

    def fill_constant(self, data, columns, constant):
        for column in columns:
            data[column] = data[column].fillna(constant)
        return data

    def drop_missing(self, data):
        return data.dropna()