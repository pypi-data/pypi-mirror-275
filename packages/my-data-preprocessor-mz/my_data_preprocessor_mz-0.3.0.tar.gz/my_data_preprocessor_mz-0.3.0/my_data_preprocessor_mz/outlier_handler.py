import numpy as np
from sklearn.impute import SimpleImputer


class OutlierHandler:
    def __init__(self, df):
        self.df = df

    def identify_and_correct_outliers(self, column, threshold=1.5):
        """
        Identify and correct outliers in a DataFrame column using the IQR method.

        :param column: Column name to check for outliers
        :param threshold: Multiplier for the IQR to define outliers
        :return: List of rows and columns with outliers
        """
        outliers_rows = []
        outliers_columns = []

        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR

        # Identify outliers
        outliers_mask = (self.df[column] < lower_bound) | (self.df[column] > upper_bound)
        outliers_rows = self.df[outliers_mask].index.tolist()
        outliers_columns = [column] * outliers_mask.sum()

        # Replace outliers with NaN
        self.df.loc[outliers_mask, column] = np.nan

        # Correct outliers by imputing NaN values with median
        imputer = SimpleImputer(strategy='median')
        self.df[[column]] = imputer.fit_transform(self.df[[column]])

        return outliers_rows, outliers_columns
