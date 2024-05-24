import pandas as pd

class scaler:

    @staticmethod
    def min_max_scaling(df, columns=None):
        """
        Apply min-max scaling to specified columns in the DataFrame.
        Parameters:
        - df: pandas DataFrame
            The DataFrame containing the data.
        - columns: list, optional
            List of column names to apply min-max scaling. If None, scale all columns with numerical data.
        Returns:
        - df: pandas DataFrame
            DataFrame with specified columns scaled using min-max scaling.
        """
        if columns is None:
            columns = df.select_dtypes(include=['float64', 'int64']).columns
        for col in columns:
            df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
        return df

    @staticmethod
    def standard_scaling(df, columns=None):
        """
        Apply standard scaling (z-score normalization) to specified columns in the DataFrame.
        Parameters:
        - df: pandas DataFrame
            The DataFrame containing the data.
        - columns: list, optional
            List of column names to apply standard scaling. If None, scale all columns with numerical data.
        Returns:
        - df: pandas DataFrame
            DataFrame with specified columns scaled using standard scaling.
        """
        if columns is None:
            columns = df.select_dtypes(include=['float64', 'int64']).columns
        for col in columns:
            df[col] = (df[col] - df[col].mean()) / df[col].std()
        return df
