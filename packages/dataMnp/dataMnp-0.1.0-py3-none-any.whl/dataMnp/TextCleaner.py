import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

class TextCleaner:

    @staticmethod
    def remove_stopwords(df, column):
        """
        Remove stopwords from the specified column in the DataFrame.
        Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column from which to remove stopwords.
        Returns:
        pd.DataFrame: DataFrame with stopwords removed from the specified column.
        """
        stop_words = set(stopwords.words('english'))
        df[column] = df[column].apply(
            lambda x: ' '.join([word for word in word_tokenize(x) if word.lower() not in stop_words]))
        return df

    @staticmethod
    def lowercase(df, column):
        """
        Convert all text in the specified column to lowercase.
        Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to convert to lowercase.
        Returns:
        pd.DataFrame: DataFrame with all text in the specified column converted to lowercase.
        """
        df[column] = df[column].str.lower()
        return df

    @staticmethod
    def remove_punctuation(df, column):
        """
        Remove punctuation from the specified column in the DataFrame.
        Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column from which to remove punctuation.
        Returns:
        pd.DataFrame: DataFrame with punctuation removed from the specified column.
        """
        df[column] = df[column].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))
        return df

    @staticmethod
    def lemmatize(df, column):
        """
        Lemmatize all words in the specified column in the DataFrame.
        Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to lemmatize.
        Returns:
        pd.DataFrame: DataFrame with all words in the specified column lemmatized.
        """
        lemmatizer = WordNetLemmatizer()
        df[column] = df[column].apply(lambda x: ' '.join([lemmatizer.lemmatize(word) for word in word_tokenize(x)]))
        return df
