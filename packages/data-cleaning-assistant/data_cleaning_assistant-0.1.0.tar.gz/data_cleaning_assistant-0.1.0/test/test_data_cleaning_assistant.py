import unittest
import pandas as pd
from data_cleaning_assistant import DataCleaningAssistant

class TestDataCleaningAssistant(unittest.TestCase):
    def setUp(self):
        data = {
            'A': [1, 2, None, 4, 5],
            'B': [1, 2, 2, None, 5],
            'C': ['2020-01-01', '2020-01-02', None, '2020-01-04', '2020-01-05'],
            'D': [1, 2, 999, 4, 5]
        }
        self.df = pd.DataFrame(data)
        self.dca = DataCleaningAssistant(self.df)
    
    def test_fill_missing_values(self):
        self.dca.fill_missing_values(strategy='median')
        self.assertFalse(self.dca.cleaned_df.isnull().values.any())

    def test_remove_duplicates(self):
        self.dca.remove_duplicates()
        self.assertEqual(len(self.dca.cleaned_df), len(self.df.drop_duplicates()))
    
    # その他のテストを追加...

if __name__ == '__main__':
    unittest.main()
