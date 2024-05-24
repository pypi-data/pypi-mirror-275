import pandas as pd


class BudgetHandler:
    def categorize_budget(self, data, column):
        bins = [0, 1000000, 10000000, 50000000, 100000000, float('inf')]
        labels = ['Very Low', 'Low', 'Medium', 'High', 'Very High']
        data['budget_category'] = pd.cut(data[column], bins=bins, labels=labels)
        return data