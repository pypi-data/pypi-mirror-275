# DataCleaner_rr/outlier_handler.py
import pandas as pd

class OutlierHandler:
    @staticmethod
    def iqr_outliers(data: pd.DataFrame, column: str, threshold: float = 1.5) -> pd.DataFrame:
        if data[column].dtype == 'object':
            raise ValueError(f"Column {column} contains non-numeric data, IQR method cannot be applied.")
        if column not in data.columns:
            raise ValueError(f"Column '{column}' not found in DataFrame.")

        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR

        return data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]

    @staticmethod
    def filter_rare_categories(data: pd.DataFrame, column: str, min_frequency: int = 5) -> pd.DataFrame:
        if data[column].dtype != 'object':
            raise ValueError(f"Column {column} does not contain string data, this method is only for string data.")
        value_counts = data[column].value_counts()
        common_values = value_counts[value_counts >= min_frequency].index
        return data[data[column].isin(common_values)]

    @staticmethod
    def lower_text(data: pd.DataFrame, column: str) -> pd.DataFrame:
        if data[column].dtype != 'object':
            raise ValueError(f"Column {column} does not contain string data, this method is only for string data.")
        # Büyük/küçük harf tutarsızlıklarını düzeltme ve gereksiz boşlukları kaldırma
        data[column] = data[column].str.lower().str.strip()
        return data

    @staticmethod
    def upper_text(data: pd.DataFrame, column: str) -> pd.DataFrame:
        if data[column].dtype != 'object':
            raise ValueError(f"Column {column} does not contain string data, this method is only for string data.")
        # Büyük/küçük harf tutarsızlıklarını düzeltme ve gereksiz boşlukları kaldırma
        data[column] = data[column].str.upper().str.strip()
        return data

#               ----   fonksiyonların çalışırlığını kontrol etme   ----
# CSV dosyasını okuma
file_path = r'C:\Users\PC\Downloads\synthetic_sample_data (4).csv'
df = pd.read_csv(file_path)

print("Orijinal Veri Seti:")
print(df.head())

print("\nMetin Temizlendikten Sonra:")
print(OutlierHandler.lower_text(df, "Genre").head())

print("Orijinal Veri Seti:")
print(df.head())