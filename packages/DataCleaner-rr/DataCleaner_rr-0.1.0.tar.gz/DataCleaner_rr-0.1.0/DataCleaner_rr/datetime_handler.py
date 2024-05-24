# DataCleaner_rr/datetime_handler.py
import pandas as pd

class DateTimeHandler:
    @staticmethod
    def convert_to_datetime(data: pd.DataFrame, column: str) -> pd.DataFrame:
        if column in data.columns:
            try:
                data[column] = pd.to_datetime(data[column], errors='coerce')
                if data[column].isna().all():
                    raise ValueError(f"Column '{column}' does not contain valid datetime values.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data

    @staticmethod
    def extract_date_features(data: pd.DataFrame, column: str) -> pd.DataFrame:
        if column in data.columns:
            if pd.api.types.is_datetime64_any_dtype(data[column]):
                data['year'] = data[column].dt.year
                data['month'] = data[column].dt.month
                data['day'] = data[column].dt.day
            else:
                print(f"Error: Column '{column}' is not in datetime format.")
        else:
            print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data

    @staticmethod
    def find_and_process_datetime_column(data: pd.DataFrame, column: str) -> pd.DataFrame:
        found = False
        for col in data.columns:
            if col == column:
                found = True
                data = DateTimeHandler.convert_to_datetime(data, column)
                if pd.api.types.is_datetime64_any_dtype(data[column]):
                    data = DateTimeHandler.extract_date_features(data, column)
                else:
                    print(f"Error: Column '{column}' is not in datetime format after conversion.")
        if not found:
            print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data

    @staticmethod
    def clean_invalid_dates(data: pd.DataFrame, column: str, default_date: str = "1900-01-01") -> pd.DataFrame:
        if column in data.columns:
            try:
                data[column] = pd.to_datetime(data[column], errors='coerce')
                invalid_dates = data[column].isna()
                data.loc[invalid_dates, column] = default_date
                data[column] = pd.to_datetime(data[column])
            except Exception as e:
                print(f"Error: {e}")
        else:
            print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data





#               ----   fonksiyonların çalışırlığını kontrol etme   ----
# CSV dosyasını okuma
file_path = r'C:\Users\PC\Downloads\synthetic_sample_data (4).csv'
df = pd.read_csv(file_path)



print("Original DataFrame:")
print(df)

# Tarih formatına dönüştürme
df = DateTimeHandler.convert_to_datetime(df, 'Release Date')
print("\nDataFrame with datetime:")
print(df.to_string())

# Tarih özelliklerini çıkartma
df = DateTimeHandler.extract_date_features(df, 'Release Date')
print("\nDataFrame with extracted date features:")
print(df.to_string())

# Tarih formatını kontrol et
df = DateTimeHandler.clean_invalid_dates(df, 'Release Date')

# Tarih sütununu bul ve işle
df = DateTimeHandler.find_and_process_datetime_column(df, 'Release Date')
print("\nDataFrame after processing datetime column:")
print(df.to_string())