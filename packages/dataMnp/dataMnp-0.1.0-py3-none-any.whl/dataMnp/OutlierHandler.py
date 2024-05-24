import pandas as pd

class OutlierHandler:

    @staticmethod
    def delete_missing(df):
        """
        Delete rows with missing values from the DataFrame.
        Parameters:
        - df: pandas DataFrame
            The DataFrame containing the data.
        Returns:
        - df: pandas DataFrame
            DataFrame with rows containing missing values removed.
        """
        return df.dropna()

    @staticmethod
    def remove_outliers_iqr(df, threshold=1.5):
        """
        Remove outliers from the DataFrame using the interquartile range method.
        Parameters:
        - df: pandas DataFrame
            The DataFrame containing the data.
        - threshold: float, optional (default=1.5)
            The threshold value to determine outliers.
        Returns:
        - df: pandas DataFrame
            DataFrame with outliers removed.
        """
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR
        return df[~((df < lower_bound) | (df > upper_bound)).any(axis=1)]


