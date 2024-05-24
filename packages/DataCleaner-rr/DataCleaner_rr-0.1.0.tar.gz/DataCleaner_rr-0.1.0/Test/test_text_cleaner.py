from DataCleaner_rr.text_cleaner import TextCleaner
import pandas as pd

def test_remove_stopwords(df):
    column = input("Enter column name: ")
    df = TextCleaner.remove_stopwords(df, column)
    print("Data after removing stopwords:")
    print(df)

def test_to_lowercase(df):
    column = input("Enter column name: ")
    df = TextCleaner.to_lowercase(df, column)
    print("Data after converting to lowercase:")
    print(df)

def test_remove_punctuation(df):
    column = input("Enter column name: ")
    df = TextCleaner.remove_punctuation(df, column)
    print("Data after removing punctuation:")
    print(df)

def test_lemmatize(df):
    column = input("Enter column name: ")
    df = TextCleaner.lemmatize(df, column)
    print("Data after lemmatizing:")
    print(df)

def test_remove_word(df):
    column = input("Enter column name: ")
    word = input("Enter the word to remove: ")
    df = TextCleaner.remove_word(df, column, word)
    print("Data after removing word:")
    print(df)

def test_to_uppercase(df):
    column = input("Enter column name: ")
    df = TextCleaner.to_uppercase(df, column)
    print("Data after converting to uppercase:")
    print(df)

def test_remove_extra_whitespace(df):
    column = input("Enter column name: ")
    df = TextCleaner.remove_extra_whitespace(df, column)
    print("Data after removing extra whitespace:")
    print(df)

def test_replace_synonyms(df):
    column = input("Enter column name: ")
    word_to_replace = input("Enter the word to replace: ")
    replacement_word = input("Enter the replacement word: ")
    df = TextCleaner.replace_synonyms(df, column, word_to_replace, replacement_word)
    print("Data after replacing synonyms:")
    print(df)

if __name__ == "__main__":
    df = pd.read_csv("C:\\Users\\PC\\Downloads\\synthetic_sample_data.csv")
    print(df.head())

    print("Choose an operation to test:")
    print("1. Remove stopwords")
    print("2. Convert to lowercase")
    print("3. Remove punctuation")
    print("4. Lemmatize text")
    print("5. Remove specific word")
    print("6. Convert to uppercase")
    print("7. Remove extra whitespace")
    print("8. Replace synonyms")
    choice = input("Enter your choice (1-8): ")
    if choice == "1":
        test_remove_stopwords(df)
    elif choice == "2":
        test_to_lowercase(df)
    elif choice == "3":
        test_remove_punctuation(df)
    elif choice == "4":
        test_lemmatize(df)
    elif choice == "5":
        test_remove_word(df)
    elif choice == "6":
        test_to_uppercase(df)
    elif choice == "7":
        test_remove_extra_whitespace(df)
    elif choice == "8":
        test_replace_synonyms(df)
    else:
        print("Invalid choice.")
