# test_missing_value_handler.py
from DataCleaner_rr.missing_value_handler import MissingValueHandler
import pandas as pd

def test_impute_mean(df):
    column = input("Enter column name: ")
    df = MissingValueHandler.impute_mean(df, column)
    print("Data after imputing mean:")
    print(df)

def test_impute_median(df):
    column = input("Enter column name: ")
    df = MissingValueHandler.impute_median(df, column)
    print("Data after imputing median:")
    print(df)

def test_impute_constant(df):
    column = input("Enter column name: ")
    constant = input("Enter constant value: ")
    df = MissingValueHandler.impute_constant(df, column, constant)
    print("Data after imputing constant:")
    print(df)

def test_delete_missing(df):
    column = input("Enter column name: ")
    df = MissingValueHandler.delete_missing(df, column)
    print("Data after deleting missing values:")
    print(df)

if __name__ == "__main__":
    df = pd.read_csv("C:\\Users\\PC\\Downloads\\synthetic_sample_data.csv")
    print(df.head())

    print("Choose an operation to test:")
    print("1. Impute mean")
    print("2. Impute median")
    print("3. Impute constant")
    print("4. Delete missing values")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        test_impute_mean(df)
    elif choice == "2":
        test_impute_median(df)
    elif choice == "3":
        test_impute_constant(df)
    elif choice == "4":
        test_delete_missing(df)
    else:
        print("Invalid choice.")
