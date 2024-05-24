from DataCleaner_rr.categorical_encoder import CategoricalEncoder
import pandas as pd

def test_label_encode(df):
    column = input("Enter column name: ")
    df = CategoricalEncoder.label_encode(df, column)
    print("Data after label encoding:")
    print(df)

def test_one_hot_encode(df):
    column = input("Enter column name: ")
    df = CategoricalEncoder.one_hot_encode(df, column)
    print("Data after one-hot encoding:")
    print(df)

if __name__ == "__main__":
    df = pd.read_csv("C:\\Users\\PC\\Downloads\\synthetic_sample_data.csv")
    print(df.head())

    print("Choose an operation to test:")
    print("1. Label Encode")
    print("2. One-Hot Encode")
    choice = input("Enter your choice (1-2): ")
    if choice == "1":
        test_label_encode(df)
    elif choice == "2":
        test_one_hot_encode(df)
    else:
        print("Invalid choice.")
