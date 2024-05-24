import pandas as pd
from DataCleaner_rr.missing_value_handler import MissingValueHandler

# Veriyi CSV dosyasından okuma
data = pd.read_csv("C:\\Users\\PC\\Downloads\\synthetic_sample_data.csv")
print("Original Data:")
print(data.to_string())

# Mean imputation
data_imputed_mean = MissingValueHandler.impute_mean(data.copy())
print("\nData after Mean Imputation:")
print(data_imputed_mean.to_string())

# Median imputation
data_imputed_median = MissingValueHandler.impute_median(data.copy())
print("\nData after Median Imputation:")
print(data_imputed_median.to_string())

# Constant imputation
constant_value = 100  # Sabit değer
data_imputed_constant = MissingValueHandler.impute_constant(data.copy(), constant_value)
print("\nData after Constant Imputation:")
print(data_imputed_constant.to_string())

# Delete rows with missing values
data_deleted_missing = MissingValueHandler.delete_missing(data.copy())
print("\nData after Deleting Missing Values:")
print(data_deleted_missing.to_string())
