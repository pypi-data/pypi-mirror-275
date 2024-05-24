# DataCleaner_rr/data_type_converter.py
import pandas as pd

class DataTypeConverter:
    @staticmethod
    def to_numeric(data: pd.DataFrame, column: str) -> pd.DataFrame:
        data[column] = pd.to_numeric(data[column], errors='coerce')
        return data

    @staticmethod
    def to_categorical(data: pd.DataFrame, column: str) -> pd.DataFrame:
        data[column] = data[column].astype('category')
        return data



#               ----   fonksiyonların çalışırlığını kontrol etme   ----
# CSV dosyasını okuma
file_path = r'C:\Users\PC\Downloads\synthetic_sample_data (4).csv'
df = pd.read_csv(file_path)

print("Original DataFrame:")
print(df)

# 'numeric_column' sütununu sayısal türe dönüştürme
print("\nDataFrame with 'numeric_column' converted to numeric:")
print(DataTypeConverter.to_numeric(df, "Genre").to_string())

# 'categorical_column' sütununu kategorik türe dönüştürme
print("\nDataFrame with 'categorical_column' converted to categorical:")
print(DataTypeConverter.to_categorical(df,"Rating").to_string())