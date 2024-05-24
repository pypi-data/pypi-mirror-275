from DataCleaner_rr.data_type_converter import DataTypeConverter
import pandas as pd

def test_to_numeric(df):
    column = input("Enter column name: ")
    df = DataTypeConverter.to_numeric(df, column)
    print("Data after converting to numeric:")
    print(df)

def test_to_categorical(df):
    column = input("Enter column name: ")
    df = DataTypeConverter.to_categorical(df, column)
    print("Data after converting to categorical:")
    print(df)

if __name__ == "__main__":
    df = pd.read_csv("C:\\Users\\PC\\Downloads\\synthetic_sample_data.csv")
    print(df.head())

    print("Choose an operation to test:")
    print("1. Convert to numeric")
    print("2. Convert to categorical")
    choice = input("Enter your choice (1-2): ")
    if choice == "1":
        test_to_numeric(df)
    elif choice == "2":
        test_to_categorical(df)
    else:
        print("Invalid choice.")
