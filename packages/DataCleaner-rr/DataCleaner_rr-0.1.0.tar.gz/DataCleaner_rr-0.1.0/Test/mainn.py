# main.py

from DataCleaner_rr.missing_value_handler import MissingValueHandler
from DataCleaner_rr.outlier_handler import OutlierHandler
from DataCleaner_rr.scaler import Scaler
from DataCleaner_rr.text_cleaner import TextCleaner
from DataCleaner_rr.data_type_converter import DataTypeConverter
from DataCleaner_rr.categorical_encoder import CategoricalEncoder
from DataCleaner_rr.datetime_handler import DateTimeHandler
import pandas as pd

def menu():
    print("Data Preprocessing Operations:")
    print("1. Handle missing values")
    print("2. Handle outliers")
    print("3. Scale data")
    print("4. Clean text")
    print("5. Convert data types")
    print("6. Encode categorical data")
    print("7. Handle datetime data")
    print("8. Exit")


def handle_missing_values_menu(df):
    print("1. Impute mean")
    print("2. Impute median")
    print("3. Impute constant")
    print("4. Delete missing values")
    choice = input("Enter your choice: ")
    column = input("Enter column name or its number: ")
    if column.isdigit():
        column = df.columns[int(column) - 1]
    if choice == "1":
        df = MissingValueHandler.impute_mean(df, column)
    elif choice == "2":
        df = MissingValueHandler.impute_median(df, column)
    elif choice == "3":
        constant = input("Enter constant value: ")
        df = MissingValueHandler.impute_constant(df, column, constant)
    elif choice == "4":
        df = MissingValueHandler.delete_missing(df, column)
    print("Data after handling missing values:")
    print(df.to_string())


def handle_outliers_menu(df):
    print("1. IQR outliers")
    print("2. Filter rare categories")
    print("3. Lower text")
    print("4. Upper text")
    choice = input("Enter your choice: ")
    column = input("Enter column name or its number: ")
    if column.isdigit():
        column = df.columns[int(column) - 1]
    if choice == "1":
        threshold = float(input("Enter the threshold value for IQR outliers detection: "))
        df = OutlierHandler.iqr_outliers(df, column, threshold)
    elif choice == "2":
        min_frequency = int(input("Enter the minimum frequency for rare categories: "))
        df = OutlierHandler.filter_rare_categories(df, column, min_frequency)
    elif choice == "3":
        df = OutlierHandler.lower_text(df, column)
    elif choice == "4":
        df = OutlierHandler.upper_text(df, column)
    print("Data after handling outliers:")
    print(df.to_string())


def handle_scaling_menu(df):
    print("1. Min-Max Scale")
    print("2. Standard Scale")
    print("3. Robust Scale")
    print("4. Normalize")
    print("5. Binarize")
    choice = input("Enter your choice: ")
    columns = input("Enter column names or their numbers (comma-separated): ").split(",")
    columns = [df.columns[int(col.strip()) - 1] if col.strip().isdigit() else col.strip() for col in columns]

    if choice == "1":
        df = Scaler.min_max_scale(df, columns)
    elif choice == "2":
        df = Scaler.standard_scale(df, columns)
    elif choice == "3":
        df = Scaler.robust_scale(df, columns)
    elif choice == "4":
        df = Scaler.normalize(df, columns)
    elif choice == "5":
        column = input("Enter column name or its number: ")
        if column.isdigit():
            column = df.columns[int(column) - 1]
        threshold = float(input("Enter threshold value: "))
        df = Scaler.binarize_column(df, column, threshold)
    print("Data after scaling:")
    print(df.to_string())


def handle_text_cleaning_menu(df):
    print("1. Remove stopwords")
    print("2. Convert to lowercase")
    print("3. Remove punctuation")
    print("4. Lemmatize text")
    print("5. Remove specific word")
    print("6. Convert to uppercase")
    print("7. Remove extra whitespace")
    print("8. Replace synonyms")
    choice = input("Enter your choice: ")
    column = input("Enter column name or its number: ")
    if column.isdigit():
        column = df.columns[int(column) - 1]

    if choice == "1":
        df = TextCleaner.remove_stopwords(df, column)
    elif choice == "2":
        df = TextCleaner.to_lowercase(df, column)
    elif choice == "3":
        df = TextCleaner.remove_punctuation(df, column)
    elif choice == "4":
        df = TextCleaner.lemmatize(df, column)
    elif choice == "5":
        word = input("Enter the word to remove: ")
        df = TextCleaner.remove_word(df, column, word)
    elif choice == "6":
        df = TextCleaner.to_uppercase(df, column)
    elif choice == "7":
        df = TextCleaner.remove_extra_whitespace(df, column)
    elif choice == "8":
        word_to_replace = input("Enter the word to replace: ")
        replacement_word = input("Enter the replacement word: ")
        df = TextCleaner.replace_synonyms(df, column, word_to_replace, replacement_word)
    print("Data after text cleaning:")
    print(df.to_string())


def handle_data_type_conversion_menu(df):
    print("1. Convert to numeric")
    print("2. Convert to categorical")
    choice = input("Enter your choice: ")
    column = input("Enter column name or its number: ")
    if column.isdigit():
        column_index = int(column) - 1
        if column_index >= 0 and column_index < len(df.columns):
            column = df.columns[column_index]
        else:
            print(f"Error: Invalid column index {column}.")
            return
    elif column not in df.columns:
        print(f"Error: Column '{column}' does not exist in the dataframe.")
        return

    if choice == "1":
        df = DataTypeConverter.to_numeric(df, column)
    elif choice == "2":
        df = DataTypeConverter.to_categorical(df, column)
    print("Data after converting data types:")
    print(df.to_string())



def handle_categorical_encoding_menu(df):
    print("1. Label Encode")
    print("2. One-Hot Encode")
    choice = input("Enter your choice: ")
    column = input("Enter column name or its number: ")

    # Sütun adının veya indeksinin doğruluğunu kontrol et
    if column.isdigit():
        column_index = int(column) - 1
        if column_index >= 0 and column_index < len(df.columns):
            column = df.columns[column_index]
        else:
            print(f"Error: Invalid column index {column}.")
            return
    elif column not in df.columns:
        print(f"Error: Column '{column}' does not exist in the dataframe.")
        return

    if choice == "1":
        df = CategoricalEncoder.label_encode(df, column)
    elif choice == "2":
        df = CategoricalEncoder.one_hot_encode(df, column)

    print("Data after encoding categorical data:")
    print(df.to_string())


def handle_datetime_menu(df):
    print("1. Convert to datetime")
    print("2. Extract date features")
    print("3. Clean invalid dates")
    choice = input("Enter your choice: ")
    column = input("Enter column name or its number: ")
    if column.isdigit():
        column = df.columns[int(column) - 1]

    if choice == "1":
        df = DateTimeHandler.convert_to_datetime(df, column)
    elif choice == "2":
        df = DateTimeHandler.extract_date_features(df, column)
    elif choice == "3":
        default_date = input("Enter default date for invalid entries (YYYY-MM-DD): ")
        df = DateTimeHandler.clean_invalid_dates(df, column, default_date)
    print("Data after handling datetime data:")
    print(df.to_string())



def main():
    df = pd.read_csv("C:\\Users\\PC\\Downloads\\synthetic_sample_data (2).csv")
    print(df.to_string())

    while True:
        menu()
        choice = input("Enter your choice (1-9): ")
        if choice == "1":
            handle_missing_values_menu(df)
        elif choice == "2":
            handle_outliers_menu(df)
        elif choice == "3":
            handle_scaling_menu(df)
        elif choice == "4":
            handle_text_cleaning_menu(df)
        elif choice == "5":
            handle_data_type_conversion_menu(df)
        elif choice == "6":
            handle_categorical_encoding_menu(df)
        elif choice == "7":
            handle_datetime_menu(df)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
