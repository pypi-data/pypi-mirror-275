from DataCleaner_rr.scaler import Scaler
import pandas as pd

def test_min_max_scale(df):
    columns = input("Enter column names (comma-separated): ").split(",")
    df = Scaler.min_max_scale(df, columns)
    print("Data after Min-Max Scaling:")
    print(df)

def test_standard_scale(df):
    columns = input("Enter column names (comma-separated): ").split(",")
    df = Scaler.standard_scale(df, columns)
    print("Data after Standard Scaling:")
    print(df)

def test_robust_scale(df):
    columns = input("Enter column names (comma-separated): ").split(",")
    df = Scaler.robust_scale(df, columns)
    print("Data after Robust Scaling:")
    print(df)

def test_normalize(df):
    columns = input("Enter column names (comma-separated): ").split(",")
    df = Scaler.normalize(df, columns)
    print("Data after Normalization:")
    print(df)

def test_binarize(df):
    column = input("Enter column name: ")
    threshold = float(input("Enter threshold value: "))
    df = Scaler.binarize_column(df, column, threshold)
    print("Data after Binarization:")
    print(df)

if __name__ == "__main__":
    df = pd.read_csv("C:\\Users\\PC\\Downloads\\synthetic_sample_data.csv")
    print(df.head())

    print("Choose an operation to test:")
    print("1. Min-Max Scale")
    print("2. Standard Scale")
    print("3. Robust Scale")
    print("4. Normalize")
    print("5. Binarize")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        test_min_max_scale(df)
    elif choice == "2":
        test_standard_scale(df)
    elif choice == "3":
        test_robust_scale(df)
    elif choice == "4":
        test_normalize(df)
    elif choice == "5":
        test_binarize(df)
    else:
        print("Invalid choice.")
