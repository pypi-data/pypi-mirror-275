import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import pandas as pd

class TextCleaner:
    @staticmethod
    def remove_stopwords(text):
        """
        removes common English stopwords from the input text.

        Parameters:
        text (str) – The input text.

        Returns:
        A string with stopwords removed.
        """
        stop_words = set(stopwords.words('english'))
        return ' '.join([word for word in text.split() if word.lower() not in stop_words])

    @staticmethod
    def to_lowercase(text):
        """
        This method converts all characters in the input text to lowercase.

        Parameters:
        text (str) – The input text.

        Returns:
        A string with all characters in lowercase.
        """
        return text.lower()

    @staticmethod
    def remove_punctuation(text):
        """
        This method removes all punctuation characters from the input text.

        Parameters:
        text (str) – The input text.

        Returns:
        A string with all punctuation removed.
        """
        return text.translate(str.maketrans('', '', string.punctuation))

    @staticmethod
    def lemmatize(text):

        """
        This method lemmatizes each word in the input text, converting words to their base or dictionary form.

        Parameters:
        text (str) – The input text.

        Returns:
        A string with all words lemmatized.
        """
        
        lemmatizer = WordNetLemmatizer()
        return ' '.join([lemmatizer.lemmatize(word) for word in text.split()])

    @staticmethod
    def clean_text(text):

        """
        This method applies the text cleaning methods (to_lowercase, remove_punctuation, lemmatize, remove_stopwords) sequentially to the input text.

        Parameters:
        text (str) - The input text.

        Returns:
        A cleaned string with all text processing methods applied.
        """

        text = TextCleaner.to_lowercase(text)
        text = TextCleaner.remove_punctuation(text)
        text = TextCleaner.lemmatize(text)
        text = TextCleaner.remove_stopwords(text)
        return text

    @staticmethod
    def clean_columns(df, columns):
        
        """
        This method applies the clean_text method to each cell in the specified columns of a DataFrame.

        Parameters:
        df (pandas.DataFrame) – The DataFrame containing the data.
        columns (list) – A list of column names in the DataFrame to be cleaned.

        Returns:
        The DataFrame with the specified columns cleaned.

        """

        if all(col in df.columns for col in columns):
            for column in columns:
                df[column] = df[column].astype(str).apply(TextCleaner.clean_text)
            return df
        else:
            missing_columns = [col for col in columns if col not in df.columns]
            print(f"Columns {missing_columns} not found in DataFrame. Cleaning skipped.")
            return df

