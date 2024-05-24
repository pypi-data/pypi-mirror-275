import unittest
import pandas as pd
from my_data_preprocessor_mz.scaler import DataScaler

class TestDataScaler(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': [5, 6, 7, 8]
        })
        self.scaler = DataScaler()

    def test_standardize_data(self):
        df_scaled = self.scaler.standardize_data(self.df.copy(), columns=['A', 'B'])
        self.assertAlmostEqual(df_scaled['A'].mean(), 0, places=1)
        self.assertAlmostEqual(df_scaled['B'].mean(), 0, places=1)

    def test_normalize_data(self):
        df_scaled = self.scaler.normalize_data(self.df.copy(), columns=['A', 'B'])
        self.assertAlmostEqual(df_scaled['A'].min(), 0, places=1)
        self.assertAlmostEqual(df_scaled['A'].max(), 1, places=1)
        self.assertAlmostEqual(df_scaled['B'].min(), 0, places=1)
        self.assertAlmostEqual(df_scaled['B'].max(), 1, places=1)

if __name__ == '__main__':
    unittest.main()