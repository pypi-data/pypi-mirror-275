import unittest
import pandas as pd
from my_package.my_module import clean_missing_values

class TestMyModule(unittest.TestCase):

    def test_clean_missing_values_mean(self):
        df = pd.DataFrame({'A': [1, 2, None], 'B': [None, 2, 3]})
        cleaned_df = clean_missing_values(df, strategy='mean')
        self.assertEqual(cleaned_df.isnull().sum().sum(), 0)

    def test_clean_missing_values_median(self):
        df = pd.DataFrame({'A': [1, 2, None], 'B': [None, 2, 3]})
        cleaned_df = clean_missing_values(df, strategy='median')
        self.assertEqual(cleaned_df.isnull().sum().sum(), 0)

if __name__ == '__main__':
    unittest.main()
