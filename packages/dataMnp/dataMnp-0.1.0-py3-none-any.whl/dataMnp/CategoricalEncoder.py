import pandas as pd
from sklearn.preprocessing import LabelEncoder

class CategoricalEncoder:


    @staticmethod
    def one_hot_encode(df, columns):
        """
        Perform one-hot encoding on specified columns of the DataFrame.

        Parameters:
        df (pd.DataFrame): The input DataFrame.
        columns (list of str): List of column names to be one-hot encoded.

        Returns:
        pd.DataFrame: The DataFrame with one-hot encoded columns.
        """
        return pd.get_dummies(df, columns=columns)

    @staticmethod
    def label_encode(df, columns):
        """
        Perform label encoding on specified columns of the DataFrame.
        Parameters:
        df (pd.DataFrame): The input DataFrame.
        columns (list of str): List of column names to be label encoded.
        Returns:
        pd.DataFrame: The DataFrame with label encoded columns.
        """
        le = LabelEncoder()
        for column in columns:
            df[column] = le.fit_transform(df[column])
        return df
