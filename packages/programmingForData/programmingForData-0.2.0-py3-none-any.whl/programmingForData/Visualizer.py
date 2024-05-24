import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Visualizer:
    def __init__(self):
        sns.set(style="whitegrid")

    def plot_histogram(self, data, column, bins=10):
        plt.figure(figsize=(10, 6))
        sns.histplot(data[column], bins=bins, kde=True)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    def plot_boxplot(self, data, column):
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=data[column])
        plt.title(f'Boxplot of {column}')
        plt.xlabel(column)
        plt.show()

    def plot_scatter(self, data, column1, column2):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=data[column1], y=data[column2])
        plt.title(f'Scatter Plot of {column1} vs {column2}')
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.show()

    def plot_correlation_matrix(self, data):
        plt.figure(figsize=(12, 8))
        # Only select numeric columns for correlation matrix
        numeric_data = data.select_dtypes(include=[float, int])
        corr = numeric_data.corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Correlation Matrix')
        plt.show()