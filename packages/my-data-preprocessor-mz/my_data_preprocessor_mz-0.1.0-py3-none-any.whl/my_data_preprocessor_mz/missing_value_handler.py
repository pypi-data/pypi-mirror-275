from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np


class Imputer:
    def __init__(self):
        self.imputer = None

    def impute_missing_values(self, df, strategy='mean', constant_value=None):
        if strategy in ['mean', 'median']:
            numeric_columns = df.select_dtypes(include=[np.number]).columns
            self.imputer = SimpleImputer(strategy=strategy)
            df[numeric_columns] = self.imputer.fit_transform(df[numeric_columns])

        elif strategy == 'constant':
            if constant_value is None:
                raise ValueError("constant_value must be provided for 'constant' strategy")
            self.imputer = SimpleImputer(strategy='constant', fill_value=constant_value)
            df = pd.DataFrame(self.imputer.fit_transform(df), columns=df.columns)

        elif strategy == 'delete':
            df = df.dropna()

        else:
            raise ValueError("Invalid strategy. Use 'mean', 'median', 'constant', or 'delete'.")

        return df
