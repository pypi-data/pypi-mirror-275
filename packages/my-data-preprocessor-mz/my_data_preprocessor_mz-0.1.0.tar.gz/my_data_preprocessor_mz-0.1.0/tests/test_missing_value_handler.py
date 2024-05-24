import unittest
import pandas as pd
import numpy as np
from my_data_preprocessor_mz.missing_value_handler import Imputer

class TestImputer(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, np.nan, 4],
            'B': [np.nan, 2, 3, 4]
        })
        self.imputer = Imputer()

    def test_impute_missing_values_mean(self):
        df_imputed = self.imputer.impute_missing_values(self.df.copy(), strategy='mean')
        self.assertFalse(df_imputed.isnull().values.any())

    def test_impute_missing_values_constant(self):
        df_imputed = self.imputer.impute_missing_values(self.df.copy(), strategy='constant', constant_value=0)
        self.assertFalse(df_imputed.isnull().values.any())
        self.assertEqual(df_imputed.loc[0, 'B'], 0)

    def test_impute_missing_values_delete(self):
        df_imputed = self.imputer.impute_missing_values(self.df.copy(), strategy='delete')
        self.assertEqual(df_imputed.shape[0], 2)

if __name__ == '__main__':
    unittest.main()