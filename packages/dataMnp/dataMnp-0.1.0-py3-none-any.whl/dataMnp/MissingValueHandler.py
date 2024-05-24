import pandas as pd

class MissingValueHandler:

    @staticmethod
    def impute_mean(df, columns=None):
        """
        Impute missing values with the mean of the column.
        Parameters:
        df (pd.DataFrame): The input DataFrame.
        columns (list, optional): List of column names to impute. If None, all columns are considered.
        Returns:
        pd.DataFrame: DataFrame with missing values imputed with mean.
        """
        if columns is None:
            columns = df.columns
        for col in columns:
            if df[col].dtype == 'float64' or df[col].dtype == 'int64':
                df[col].fillna(df[col].mean(), inplace=True)
        return df

    @staticmethod
    def impute_median(df, columns=None):
        """
        Impute missing values with the median of the column.
        Parameters:
        df (pd.DataFrame): The input DataFrame.
        columns (list, optional): List of column names to impute. If None, all columns are considered.
        Returns:
        pd.DataFrame: DataFrame with missing values imputed with median.
        """
        if columns is None:
            columns = df.columns
        for col in columns:
            if df[col].dtype == 'float64' or df[col].dtype == 'int64':
                df[col].fillna(df[col].median(), inplace=True)
        return df

    @staticmethod
    def impute_constant(df, value, columns=None):
        """
        Impute missing values with a constant value.
        Parameters:
        df (pd.DataFrame): The input DataFrame.
        value (any): The constant value to use for imputation.
        columns (list, optional): List of column names to impute. If None, all columns are considered.
        Returns:
        pd.DataFrame: DataFrame with missing values imputed with the constant value.
        """
        if columns is None:
            columns = df.columns
        for col in columns:
            df[col].fillna(value, inplace=True)
        return df

    @staticmethod
    def delete_missing(df):
        """
        Delete rows with any missing values.
        Parameters:
        df (pd.DataFrame): The input DataFrame.
        Returns:
        pd.DataFrame: DataFrame with rows containing missing values removed.
        """
        return df.dropna()
