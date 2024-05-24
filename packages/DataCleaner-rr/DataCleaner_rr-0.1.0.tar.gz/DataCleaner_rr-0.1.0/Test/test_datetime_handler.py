from DataCleaner_rr.datetime_handler import DateTimeHandler
import pandas as pd

def test_convert_to_datetime(df):
    column = input("Enter column name: ")
    df = DateTimeHandler.convert_to_datetime(df, column)
    print("Data after converting to datetime:")
    print(df)

def test_extract_date_features(df):
    column = input("Enter column name: ")
    df = DateTimeHandler.extract_date_features(df, column)
    print("Data after extracting date features:")
    print(df)

def test_clean_invalid_dates(df):
    column = input("Enter column name: ")
    default_date = input("Enter default date for invalid entries (YYYY-MM-DD): ")
    df = DateTimeHandler.clean_invalid_dates(df, column, default_date)
    print("Data after cleaning invalid dates:")
    print(df)

if __name__ == "__main__":
    df = pd.read_csv("C:\\Users\\PC\\Downloads\\synthetic_sample_data.csv")
    print(df.head())

    print("Choose an operation to test:")
    print("1. Convert to datetime")
    print("2. Extract date features")
    print("3. Clean invalid dates")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        test_convert_to_datetime(df)
    elif choice == "2":
        test_extract_date_features(df)
    elif choice == "3":
        test_clean_invalid_dates(df)
    else:
        print("Invalid choice.")
