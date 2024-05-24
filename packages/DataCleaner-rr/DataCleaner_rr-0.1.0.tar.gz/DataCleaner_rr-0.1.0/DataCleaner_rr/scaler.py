from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, Normalizer, Binarizer
import pandas as pd

class Scaler:
    @staticmethod
    def min_max_scale(data: pd.DataFrame, columns: list) -> pd.DataFrame:
        for column in columns:
            if column in data.columns:
                if pd.api.types.is_numeric_dtype(data[column]):
                    scaler = MinMaxScaler()
                    data[column] = scaler.fit_transform(data[[column]])
                else:
                    print(f"Error: Column '{column}' does not contain numeric values.")
            else:
                print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data

    @staticmethod
    def standard_scale(data: pd.DataFrame, columns: list) -> pd.DataFrame:
        for column in columns:
            if column in data.columns:
                if pd.api.types.is_numeric_dtype(data[column]):
                    scaler = StandardScaler()
                    data[column] = scaler.fit_transform(data[[column]])
                else:
                    print(f"Error: Column '{column}' does not contain numeric values.")
            else:
                print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data

    @staticmethod
    def robust_scale(data: pd.DataFrame, columns: list) -> pd.DataFrame:
        for column in columns:
            if column in data.columns:
                if pd.api.types.is_numeric_dtype(data[column]):
                    scaler = RobustScaler()
                    data[column] = scaler.fit_transform(data[[column]])
                else:
                    print(f"Error: Column '{column}' does not contain numeric values.")
            else:
                print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data

    @staticmethod
    def normalize(data: pd.DataFrame, columns: list) -> pd.DataFrame:
        for column in columns:
            if column in data.columns:
                if pd.api.types.is_numeric_dtype(data[column]):
                    scaler = Normalizer()
                    data[column] = scaler.fit_transform(data[[column]])
                else:
                    print(f"Error: Column '{column}' does not contain numeric values.")
            else:
                print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data

    def binarize_column(data: pd.DataFrame, column: str, threshold: float) -> pd.DataFrame:
        if column in data.columns:
            if pd.api.types.is_numeric_dtype(data[column]):
                binarizer = Binarizer(threshold=threshold)
                data[column] = binarizer.transform(data[[column]])
            else:
                print(f"Warning: Column '{column}' does not contain numeric values.")
        else:
            print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data

    @staticmethod
    def scale_column(data: pd.DataFrame, column: str, method: str = 'standard') -> pd.DataFrame:
        if column not in data.columns:
            raise ValueError(f"Column '{column}' does not exist in the dataframe.")

        column_dtype = data[column].dtype
        if column_dtype != 'int64' and column_dtype != 'float64':
            raise ValueError(f"Column '{column}' does not contain numeric values.")

        scalers = {
            'minmax': MinMaxScaler(),
            'standard': StandardScaler(),
            'robust': RobustScaler(),
            'normalize': Normalizer()
        }
        if method in scalers:
            scaler = scalers[method]
            data[[column]] = scaler.fit_transform(data[[column]])
        else:
            raise ValueError(f"Scaling method '{method}' is not supported.")
        return data


#               ----   fonksiyonların çalışırlığını kontrol etme   ----
# CSV dosyasını okuma
file_path = r'C:\Users\PC\Downloads\synthetic_sample_data (4).csv'
df = pd.read_csv(file_path)



print("Original DataFrame:")
print(df)

# Binarize fonksiyonu
df = Scaler.binarize_column(df, 'Rating', 6.7)
print("\nDataFrame with datetime:")
print(df.to_string())