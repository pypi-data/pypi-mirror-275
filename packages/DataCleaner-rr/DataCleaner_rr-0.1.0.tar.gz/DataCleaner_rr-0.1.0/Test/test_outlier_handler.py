# test_outlier_handler.py

from DataCleaner_rr.outlier_handler import OutlierHandler
import pandas as pd

def test_iqr_outliers(df):
    column = input("Enter column name: ")
    threshold = float(input("Enter the threshold value for IQR outliers detection: "))
    df = OutlierHandler.iqr_outliers(df, column, threshold)
    print("Data after handling IQR outliers:")
    print(df)

def test_filter_rare_categories(df):
    column = input("Enter column name: ")
    min_frequency = int(input("Enter the minimum frequency for rare categories: "))
    df = OutlierHandler.filter_rare_categories(df, column, min_frequency)
    print("Data after filtering rare categories:")
    print(df)

def test_lower_text(df):
    column = input("Enter column name: ")
    df = OutlierHandler.lower_text(df, column)
    print("Data after converting text to lower case:")
    print(df)

def test_upper_text(df):
    column = input("Enter column name: ")
    df = OutlierHandler.upper_text(df, column)
    print("Data after converting text to upper case:")
    print(df)

if __name__ == "__main__":
    df = pd.read_csv("C:\\Users\\PC\\Downloads\\synthetic_sample_data.csv")
    print(df.head())

    print("Choose an operation to test:")
    print("1. IQR outliers")
    print("2. Filter rare categories")
    print("3. Lower text")
    print("4. Upper text")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        test_iqr_outliers(df)
    elif choice == "2":
        test_filter_rare_categories(df)
    elif choice == "3":
        test_lower_text(df)
    elif choice == "4":
        test_upper_text(df)
    else:
        print("Invalid choice.")
