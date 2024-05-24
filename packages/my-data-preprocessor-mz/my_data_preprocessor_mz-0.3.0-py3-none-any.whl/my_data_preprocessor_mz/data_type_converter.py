import pandas as pd
class DataFrameConverter:
    def __init__(self, df):
        self.df = df

    def convert_to_numeric(self, columns):

        self.df[columns] = self.df[columns].apply(pd.to_numeric, errors='coerce')

    def convert_to_categorical(self, columns):

        self.df[columns] = self.df[columns].astype('category')
