import unittest
import pandas as pd
from my_data_preprocessor_mz.data_type_converter import DataFrameConverter

class TestDataFrameConverter(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'A': ['1', '2', '3', '4'],
            'B': ['5', '6', '7', '8'],
            'C': ['9', '10', '11', '12']
        })
        self.converter = DataFrameConverter(self.df)

    def test_convert_to_numeric(self):
        self.converter.convert_to_numeric(columns=['A', 'B'])
        self.assertTrue(pd.api.types.is_numeric_dtype(self.converter.df['A']))
        self.assertTrue(pd.api.types.is_numeric_dtype(self.converter.df['B']))

    def test_convert_to_categorical(self):
        self.converter.convert_to_categorical(columns=['C'])
        self.assertTrue(pd.api.types.is_categorical_dtype(self.converter.df['C']))

if __name__ == '__main__':
    unittest.main()