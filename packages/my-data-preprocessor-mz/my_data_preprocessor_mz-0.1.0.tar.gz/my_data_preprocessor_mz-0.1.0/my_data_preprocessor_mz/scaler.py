import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler


class DataScaler:
    def __init__(self):
        self.standard_scaler = StandardScaler()
        self.minmax_scaler = MinMaxScaler()

    def check_numeric(self, df, columns):
        for column in columns:
            if not pd.api.types.is_numeric_dtype(df[column]):
                print(f"Error: Column '{column}' is not numeric.")
                return False
        return True

    def standardize_data(self, df, columns):
        if not self.check_numeric(df, columns):
            return None
        df[columns] = self.standard_scaler.fit_transform(df[columns])
        return df

    def normalize_data(self, df, columns):
        if not self.check_numeric(df, columns):
            return None
        df[columns] = self.minmax_scaler.fit_transform(df[columns])
        return df
