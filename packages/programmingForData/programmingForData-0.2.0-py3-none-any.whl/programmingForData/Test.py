import pandas as pd
import os
from CategoricalEncoder import CategoricalEncoder
from DataTypeConverter import DataTypeConverter
from DateTimeHandler import DateTimeHandler
from BudgetHandler import BudgetHandler
from MissingValueHandler import MissingValueHandler
from Scaler import Scaler
from OutlierHandler import OutlierHandler
from Visualizer import Visualizer
from DataFilter import DataFilter



pd.set_option('display.max_columns', None)

# Veri setini yükle
data = pd.read_csv("C:\\Users\\Beyza\\Desktop\\synthetic_sample_data.csv")


# Veri setinin ilk birkaç satırını görüntüle
print("original data:")
print(data.head())

encoder = CategoricalEncoder()


def test_one_hot_encode():
    # CategoricalEncoder sınıfını kullanarak One-Hot Encoding yapma
    global data
    data = encoder.one_hot_encode(data, 'Genre')
    print("One-Hot Encoding result:")
    print(data.head())


def test_label_encode():
    # CategoricalEncoder sınıfını kullanarak Label Encoding yapma
    global data
    data = encoder.label_encode(data, 'Genre')
    print("\nLabel Encoding result:")
    print(data.head())


converter = DataTypeConverter()


def test_convert_to_numeric():
    global data
    numeric_columns = ['Awards', 'Genre']  # Dönüşüm yapılacak sayısal sütunların listesi
    data = converter.convert_to_numeric(data, numeric_columns)
    print("\nNumerical Conversion result:")
    print(data.head())


def test_convert_to_categorical():
    # DataTypeConverter sınıfını kullanarak kategorik dönüşüm yapma
    global data
    print("\nData Types:")
    print(data.dtypes)
    categorical_columns = ['Genre', 'Shooting Location']  # Dönüşüm yapılacak kategorik sütunların listesi
    data = converter.convert_to_categorical(data, categorical_columns)
    print("\nCategorical conversion result:")
    print(data.head())

    print("\nData Types:")
    print(data.dtypes)


handler = DateTimeHandler()


def test_convert_to_datetime():
    # convert_to_datetime metodu testi
    global data
    data = handler.convert_to_datetime(data, 'Release Date')
    print("\nconvert to datetime Method Test:")
    print(data.head())


def test_extract_date_parts():
    # extract_date_parts metodu testi
    global data
    data = handler.extract_date_parts(data, 'Release Date')
    print("\nextract date parts Method Test:")
    print(data.head())


b_handler = BudgetHandler()


def test_categorize_budget():
    # categorize_budget metodunu çağır
    global data
    data = b_handler.categorize_budget(data, 'Budget in USD')
    print("\nCategorized Data:\n", data.head())


mhandler = MissingValueHandler()


def test_missing_value_handler():
    global data
    print("\nFilling missing values with mean:")
    categorical_columns = ['Rating', 'Budget in USD', 'Awards']
    data = mhandler.fill_mean(data, categorical_columns)
    print(data.head())

    print("\nFilling missing values with median:")
    data = mhandler.fill_median(data, categorical_columns)
    print(data.head)

    print("\nFilling missing values with constant value (0):")
    data = mhandler.fill_constant(data, categorical_columns, 0)
    print(data.head())

    print("\nDropping rows with missing values:")
    data = mhandler.drop_missing(data)
    print(data.head())


ohandler = OutlierHandler()


def test_outlier_handler():
    global data
    print("\nData after removing outliers using IQR method:")
    data = ohandler.iqr_outliers(data, 'Rating')
    print(data.head())

    print("\nData after replacing outliers with median using IQR method:")
    data = ohandler.replace_outliers_with_median(data, 'Budget in USD')
    print(data.head)


scaler = Scaler()


def test_scaler():
    global data
    print("\nMin-Max scaled data:")
    data = scaler.min_max_scale(data)
    print(data.head())

    print("\nStandard scaled data:")
    data = scaler.standard_scale(data)
    print(data.head())


visualizer = Visualizer()


def test_visualizer():
    global data
    print("Running histogram plot test...")
    visualizer.plot_histogram(data, 'Rating', bins=10)

    print("Running boxplot test...")
    visualizer.plot_boxplot(data, 'Budget in USD')

    print("Running scatter plot test...")
    visualizer.plot_scatter(data, 'Budget in USD', 'Rating')

    print("Running correlation matrix plot test...")
    visualizer.plot_correlation_matrix(data)


filter = DataFilter()


def test_data_filter():
    global data
    filtered_by_condition = filter.filter_by_condition(data, 'Rating > 8')
    print("Filtered by Condition (Rating > 8):")
    print(filtered_by_condition[['Movie Id', 'Genre', 'Rating']])  # Display a few relevant columns

    # Test filter_by_columns
    columns_to_display = ['Genre', 'Release Date', 'Rating', 'Shooting Location', 'Budget in USD']
    filtered_by_columns = filter.filter_by_columns(data, columns_to_display)
    print("\nFiltered by Columns (Genre, Release Date, Rating, Shooting Location, Budget in USD):")
    print(filtered_by_columns.head())  # Display the first few rows of filtered data


test_visualizer()
file_path = "C:\\Users\\Beyza\\Desktop\\yenitablo.csv"

#Dosyayı silme
if os.path.exists(file_path):
    os.remove(file_path)

# Yeniden yazma izni alarak kaydetme
data.to_csv(file_path, index=False)