import pandas as pd

class FeatureEngineer:

    @staticmethod
    def change_scientific_notation(dataframe, column):
        """
        Convert values in the specified column from scientific notation to standard decimal notation.
        Parameters:
        dataframe (pd.DataFrame) : The DataFrame containing the data.
        column (str) : The name of the column with values in scientific notation.
        Raises:
        ValueError : If the column does not exist in the DataFrame.
        TypeError : If the column is not of numeric type.
        """
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(dataframe[column]):
            raise TypeError(f"Column '{column}' is not numeric.")
        dataframe[column] = dataframe[column].apply(lambda x: "{:,.0f}".format(x))

    @staticmethod
    def multiply2Col(df, columns):
        """
        Multiplies pairs of columns and adds the result as new columns in the DataFrame.
        Parameters:
        df (pd.DataFrame): The input DataFrame.
        columns (list of tuple): List of tuples where each tuple contains two column names to be multiplied.
        Returns:
        pd.DataFrame: DataFrame with new columns containing the product of the specified columns.
        """
        for col1, col2 in columns:
            new_column_name = f'{col1}_x_{col2}'
            df[new_column_name] = df[col1] * df[col2]
        return df