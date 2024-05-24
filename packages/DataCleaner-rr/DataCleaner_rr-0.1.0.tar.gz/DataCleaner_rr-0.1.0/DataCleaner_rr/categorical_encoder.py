# DataCleaner_rr/categorical_encoder.py
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pandas as pd

class CategoricalEncoder:
    @staticmethod
    def label_encode(data: pd.DataFrame, column: str) -> pd.DataFrame:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        return data

    @staticmethod
    def one_hot_encode(data: pd.DataFrame, column: str) -> pd.DataFrame:
        if column in data.columns:
            ohe = OneHotEncoder(sparse_output=False)
            encoded = ohe.fit_transform(data[[column]])
            df_encoded = pd.DataFrame(encoded, columns=ohe.get_feature_names_out([column]))
            data = pd.concat([data, df_encoded], axis=1).drop(columns=[column])
        else:
            print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data


#               ----   fonksiyonların çalışırlığını kontrol etme   ----
# CSV dosyasını okuma
file_path = r'C:\Users\PC\Downloads\synthetic_sample_data (4).csv'
df = pd.read_csv(file_path)


print("Original DataFrame:")
print(df)

# label encoding
try:
    print("\nDataFrame with labels:")
    print(CategoricalEncoder.label_encode(df, "Genre").to_string())
except Exception as e:
    print(f"An error occurred during label encoding: {e}")

# one-hot encoding
try:
    data = pd.read_csv(file_path)  # Orijinal dataframe'i tekrar yükleyin
    print("\nDataFrame with one-hot encoding:")
    print(CategoricalEncoder.one_hot_encode(data, "Genre").to_string())
except Exception as e:
    print(f"An error occurred during one-hot encoding: {e}")