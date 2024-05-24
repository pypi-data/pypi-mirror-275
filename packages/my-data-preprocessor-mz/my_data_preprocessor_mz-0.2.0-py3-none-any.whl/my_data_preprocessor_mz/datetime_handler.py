import pandas as pd

class DateTimeManipulator:
    @staticmethod
    def convert_to_datetime(df, columns):

        df_copy = df.copy()
        for column in columns:
            df_copy[column] = pd.to_datetime(df_copy[column], format="%d/%m/%Y", errors='coerce')
        return df_copy

    @staticmethod
    def extract_date_info(df, column):

        df_copy = df.copy()
        df_copy[column] = pd.to_datetime(df_copy[column])
        df_copy['Year'] = df_copy[column].dt.year
        df_copy['Month'] = df_copy[column].dt.month
        df_copy['Day'] = df_copy[column].dt.day
        return df_copy
