import pandas as pd

# Veriyi CSV dosyasından okuma
data = pd.read_csv("C:\\Users\\PC\\Downloads\\synthetic_sample_data.csv")
print(data.head())  # İlk birkaç satırı görüntüleyin

class MissingValueHandler:
    @staticmethod
    def impute_mean(data, column):
        if column in data.columns and pd.api.types.is_numeric_dtype(data[column]):
            mean_value = data[column].mean()
            data[column].fillna(mean_value, inplace=True)
        return data

    @staticmethod
    def impute_median(data, column):
        if column in data.columns and pd.api.types.is_numeric_dtype(data[column]):
            median_value = data[column].median()
            data[column].fillna(median_value, inplace=True)
        return data

    @staticmethod
    def impute_constant(data, column, constant):
        if column in data.columns and pd.api.types.is_numeric_dtype(data[column]):
            data[column].fillna(constant, inplace=True)
        return data

    @staticmethod
    def delete_missing(data, column):
        if column in data.columns and pd.api.types.is_numeric_dtype(data[column]):
            data.dropna(subset=[column], inplace=True)
        return data

    @staticmethod
    def fill_string_na_all_columns(data, fill_value):
        for column in data.columns:
            if pd.api.types.is_string_dtype(data[column]):
                data[column].fillna(fill_value, inplace=True)
        return data

