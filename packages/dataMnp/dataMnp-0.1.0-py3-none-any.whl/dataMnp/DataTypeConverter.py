import pandas as pd


class DataTypeConverter:
    @staticmethod
    def convert_to_numeric(df, columns, errors='raise'):
        """
        Convert specified columns of the DataFrame to numeric type.
        Parameters:
        df (pd.DataFrame): The input DataFrame.
        columns (list of str): List of column names to be converted to numeric type.
        errors (str): How to handle errors ('raise', 'coerce', 'ignore').
        Returns:
        pd.DataFrame: The DataFrame with specified columns converted to numeric type.
        """
        for column in columns:
            df[column] = pd.to_numeric(df[column], errors=errors)
        return df

    @staticmethod
    def convert_to_categorical(df, columns):
        """
        Convert specified columns of the DataFrame to categorical type.
        Parameters:
        df (pd.DataFrame): The input DataFrame.
        columns (list of str): List of column names to be converted to categorical type.
        Returns:
        pd.DataFrame: The DataFrame with specified columns converted to categorical type.
        """
        for column in columns:
            df[column] = df[column].astype('category')
        return df



