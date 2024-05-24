import unittest
import pandas as pd
from data_preprocessing_lib_byarat import CategoricalEncoder

class TestCategoricalEncoder(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'category_column': ['A', 'B', 'A', 'C'],
            'target_column': [1, 2, 1, 2]
        })

    def test_one_hot_encode(self):
        df_result = CategoricalEncoder.one_hot_encode(self.df.copy(), 'category_column')
        self.assertIn('category_column_A', df_result.columns)
        self.assertIn('category_column_B', df_result.columns)
        self.assertIn('category_column_C', df_result.columns)
        self.assertEqual(df_result['category_column_A'].sum(), 2)
        self.assertEqual(df_result['category_column_B'].sum(), 1)
        self.assertEqual(df_result['category_column_C'].sum(), 1)

    def test_label_encode(self):
        df_result = CategoricalEncoder.label_encode(self.df.copy(), 'category_column')
        self.assertTrue(pd.api.types.is_numeric_dtype(df_result['category_column']))

    def test_ordinal_encode(self):
        df_result = CategoricalEncoder.ordinal_encode(self.df.copy(), 'category_column')
        self.assertTrue(pd.api.types.is_numeric_dtype(df_result['category_column']))

    def test_frequency_encode(self):
        df_result = CategoricalEncoder.frequency_encode(self.df.copy(), 'category_column')
        self.assertIn('category_column_freq_encode', df_result.columns)
        self.assertAlmostEqual(df_result['category_column_freq_encode'].sum(), 1.0)

    def test_target_encode(self):
        df_result = CategoricalEncoder.target_encode(self.df.copy(), 'category_column', 'target_column')
        self.assertIn('category_column_target_encode', df_result.columns)
        self.assertAlmostEqual(df_result['category_column_target_encode'].sum(), 6.0)

    def test_binary_encode(self):
        df_result = CategoricalEncoder.binary_encode(self.df.copy(), 'category_column')
        self.assertTrue(all(col.startswith('category_column_bin_') for col in df_result.columns if 'category_column_bin_' in col))
        self.assertEqual(df_result.shape[1], 3)  # Original column replaced by binary columns

if __name__ == '__main__':
    unittest.main()
