import unittest
import pandas as pd
from my_data_preprocessor_mz.outlier_handler import OutlierHandler

class TestOutlierHandler(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 100]  # 100 is an outlier
        })
        self.handler = OutlierHandler(self.df)

    def test_identify_and_correct_outliers(self):
        outliers_rows, outliers_columns = self.handler.identify_and_correct_outliers('A')
        self.assertIn(4, outliers_rows)
        self.assertEqual(outliers_columns.count('A'), 1)
        self.assertFalse(self.df['A'].isnull().any())  # Outlier should be replaced by median

if __name__ == '__main__':
    unittest.main()