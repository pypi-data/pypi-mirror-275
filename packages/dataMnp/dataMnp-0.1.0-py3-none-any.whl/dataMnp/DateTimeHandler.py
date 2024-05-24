import pandas as pd

class DateTimeHandler:

    @staticmethod
    def extract_date(df, column):
        """
        Extracts year, month, day, hour, minute, and second from a datetime column.
        Parameters:
        df (pd.DataFrame): The input DataFrame.
        column (str): The name of the column containing datetime values.
        Returns:
        pd.DataFrame: The DataFrame with new columns for year, month, day, hour, minute, and second.
        """
        df[column] = pd.to_datetime(df[column])
        df[f'{column}_year'] = df[column].dt.year
        df[f'{column}_month'] = df[column].dt.month
        df[f'{column}_day'] = df[column].dt.day
        df[f'{column}_hour'] = df[column].dt.hour
        df[f'{column}_minute'] = df[column].dt.minute
        df[f'{column}_second'] = df[column].dt.second
        return df


    @staticmethod
    def calculate_time_difference(df, start_column, end_column, unit='days'):
        """
        Calculates the time difference between two datetime columns in a DataFrame.
        Parameters:
        df (pd.DataFrame): The input DataFrame.
        start_column (str): The name of the start datetime column.
        end_column (str): The name of the end datetime column.
        unit (str): The unit for the time difference ('days', 'hours', 'minutes', 'seconds').
        Returns:
        pd.DataFrame: DataFrame with a new column for the time difference.
        """
        df[start_column] = pd.to_datetime(df[start_column])
        df[end_column] = pd.to_datetime(df[end_column])
        diff = df[end_column] - df[start_column]

        if unit == 'days':
            df[f'{start_column}_to_{end_column}_diff_{unit}'] = diff.dt.days
        elif unit == 'hours':
            df[f'{start_column}_to_{end_column}_diff_{unit}'] = diff.dt.total_seconds() / 3600
        elif unit == 'minutes':
            df[f'{start_column}_to_{end_column}_diff_{unit}'] = diff.dt.total_seconds() / 60
        elif unit == 'seconds':
            df[f'{start_column}_to_{end_column}_diff_{unit}'] = diff.dt.total_seconds()
        else:
            raise ValueError("Invalid unit. Choose from 'days', 'hours', 'minutes', or 'seconds'.")

        return df