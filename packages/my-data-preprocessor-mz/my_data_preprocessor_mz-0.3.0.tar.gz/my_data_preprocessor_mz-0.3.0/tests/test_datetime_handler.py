import unittest
import pandas as pd
from my_data_preprocessor_mz.datetime_handler import DateTimeManipulator

class TestDateTimeManipulator(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Date': ['03/03/2019', '04/04/2020', '05/05/2021']
        })

    def test_convert_to_datetime(self):
        df_converted = DateTimeManipulator.convert_to_datetime(self.df, columns=['Date'])
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(df_converted['Date']))

    def test_extract_date_info(self):
        df_converted = DateTimeManipulator.convert_to_datetime(self.df, columns=['Date'])
        df_date_info = DateTimeManipulator.extract_date_info(df_converted, column='Date')
        self.assertIn('Year', df_date_info.columns)
        self.assertIn('Month', df_date_info.columns)
        self.assertIn('Day', df_date_info.columns)

if __name__ == '__main__':
    unittest.main()