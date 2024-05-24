class DataFilter:
    def filter_by_condition(self, data, condition):
        return data.query(condition)

    def filter_by_columns(self, data, columns):
        return data[columns]