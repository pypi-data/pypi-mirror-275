import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# NLTK verilerini indir (ilk kez kullanıldığında gereklidir)
nltk.download('stopwords')
nltk.download('wordnet')

class TextCleaner:
    @staticmethod
    def remove_stopwords(data: pd.DataFrame, column: str) -> pd.DataFrame:
        if column in data.columns:
            if pd.api.types.is_string_dtype(data[column]):
                stop_words = set(stopwords.words('english'))
                data[column] = data[column].apply(lambda x: ' '.join([word for word in str(x).split() if word not in stop_words]))
            else:
                print(f"Warning: Column '{column}' is not of type string.")
        else:
            print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data

    @staticmethod
    def to_lowercase(data: pd.DataFrame, column: str) -> pd.DataFrame:
        if column in data.columns:
            if pd.api.types.is_string_dtype(data[column]):
                data[column] = data[column].str.lower()
            else:
                print(f"Warning: Column '{column}' is not of type string.")
        else:
            print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data

    @staticmethod
    def remove_punctuation(data: pd.DataFrame, column: str) -> pd.DataFrame:
        if column in data.columns:
            if pd.api.types.is_string_dtype(data[column]):
                data[column] = data[column].apply(lambda x: re.sub(r'[^\w\s]', '', str(x)))
            else:
                print(f"Warning: Column '{column}' is not of type string.")
        else:
            print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data

    @staticmethod
    def lemmatize(data: pd.DataFrame, column: str) -> pd.DataFrame:
        if column in data.columns:
            if pd.api.types.is_string_dtype(data[column]):
                lemmatizer = WordNetLemmatizer()
                data[column] = data[column].apply(lambda x: ' '.join([lemmatizer.lemmatize(word) for word in str(x).split()]))
            else:
                print(f"Warning: Column '{column}' is not of type string.")
        else:
            print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data

    @staticmethod
    def remove_word(data: pd.DataFrame, column: str, word: str) -> pd.DataFrame:
        if column in data.columns:
            if pd.api.types.is_string_dtype(data[column]):
                data[column] = data[column].apply(
                    lambda x: ' '.join([w for w in str(x).split() if w.lower() != word.lower()]))
            else:
                print(f"Warning: Column '{column}' is not of type string.")
        else:
            print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data


    @staticmethod
    def to_uppercase(data: pd.DataFrame, column: str) -> pd.DataFrame:
        if column in data.columns:
            if pd.api.types.is_string_dtype(data[column]):
                data[column] = data[column].str.upper()
            else:
                print(f"Warning: Column '{column}' is not of type string.")
        else:
            print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data


    @staticmethod
    def remove_extra_whitespace(data: pd.DataFrame, column: str) -> pd.DataFrame:
        if column in data.columns:
            if pd.api.types.is_string_dtype(data[column]):
                data[column] = data[column].apply(lambda x: ' '.join(str(x).split()))
            else:
                print(f"Warning: Column '{column}' is not of type string.")
        else:
            print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data

    @staticmethod
    def replace_synonyms(data: pd.DataFrame, column: str, word_to_replace: str, replacement_word: str) -> pd.DataFrame:
        if column in data.columns:
            if pd.api.types.is_string_dtype(data[column]):
                # Kelimenin tam olarak eşleşmesini kontrol etmek için düzenli ifade oluştur
                pattern = re.compile(rf'\b{re.escape(word_to_replace)}\b')
                # Düzenli ifadeyi kullanarak kelimeyi değiştir
                data[column] = data[column].apply(lambda x: pattern.sub(replacement_word, str(x)))
            else:
                print(f"Warning: Column '{column}' is not of type string.")
        else:
            print(f"Error: Column '{column}' does not exist in the dataframe.")
        return data



#               ----   fonksiyonların çalışırlığını kontrol etme   ----
# CSV dosyasını okuma
file_path = r'C:\Users\PC\Downloads\synthetic_sample_data (4).csv'
df = pd.read_csv(file_path)

print("original one:")
print(df.to_string())


print("\nStopwords'leri Kaldırılmış Veri Seti:")
print(TextCleaner.remove_stopwords(df,"Summary").to_string())


print("original one:")
print(df.to_string())


print("\nDataFrame with punctuation removed::")
print(TextCleaner.remove_punctuation(df,"Summary").to_string())


print("\nDataFrame with lemmatized words:")
print(TextCleaner.lemmatize(df,"Summary").to_string())


print("\nDataFrame with removed words:")
print(TextCleaner.remove_word(df,"Summary", "develop").to_string())


print("\nDataFrame with uppercase words:")
print(TextCleaner.to_uppercase(df,"Summary").to_string())


print("\nDataFrame with synonyms:")
print(TextCleaner.replace_synonyms(df,"Summary","A","the").to_string())

