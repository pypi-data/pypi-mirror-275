import unittest
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler, PowerTransformer, QuantileTransformer
from data_preprocessing_lib_byarat import Scaler

class TestScaler(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [2, 4, 6, 8, 10],
            'C': [1, 4, 9, 16, 25]
        })

    def test_min_max_scale(self):
        df_result = Scaler.min_max_scale(self.df.copy(), 'A')
        self.assertAlmostEqual(df_result['A'].min(), 0.0)
        self.assertAlmostEqual(df_result['A'].max(), 1.0)

    def test_standard_scale(self):
        df_result = Scaler.standard_scale(self.df.copy(), 'A')
        self.assertAlmostEqual(df_result['A'].mean(), 0.0, places=1)
        self.assertAlmostEqual(df_result['A'].std(), 1.0, places=1)

    def test_robust_scale(self):
        df_result = Scaler.robust_scale(self.df.copy(), 'A')
        self.assertAlmostEqual(df_result['A'].median(), 0.0, places=1)

    def test_max_abs_scale(self):
        df_result = Scaler.max_abs_scale(self.df.copy(), 'A')
        self.assertAlmostEqual(df_result['A'].max(), 1.0)

    def test_scale_to_range(self):
        df_result = Scaler.scale_to_range(self.df.copy(), 'A', feature_range=(10, 20))
        self.assertAlmostEqual(df_result['A'].min(), 10.0)
        self.assertAlmostEqual(df_result['A'].max(), 20.0)

    def test_log_scale(self):
        df_result = Scaler.log_scale(self.df.copy(), 'A')
        self.assertTrue(np.all(df_result['A'] > 0))

    def test_z_score(self):
        df_result = Scaler.z_score(self.df.copy(), 'A')
        self.assertAlmostEqual(df_result['A'].mean(), 0.0, places=1)
        self.assertAlmostEqual(df_result['A'].std(), 1.0, places=1)

    def test_box_cox_scale(self):
        df = self.df.copy()
        df['A'] = df['A'].apply(lambda x: x + 1)  # Box-Cox requires positive values
        df_result = Scaler.box_cox_scale(df.copy(), 'A')
        self.assertAlmostEqual(df_result['A'].mean(), 0.0, places=1)

    def test_yeo_johnson_scale(self):
        df_result = Scaler.yeo_johnson_scale(self.df.copy(), 'A')
        self.assertAlmostEqual(df_result['A'].mean(), 0.0, places=1)

    def test_quantile_transform(self):
        df_result = Scaler.quantile_transform(self.df.copy(), 'A')
        self.assertAlmostEqual(df_result['A'].min(), 0.0)
        self.assertAlmostEqual(df_result['A'].max(), 1.0)

    def test_inverse_log_scale(self):
        df = self.df.copy()
        df['A'] = np.log1p(df['A'])
        df_result = Scaler.inverse_log_scale(df.copy(), 'A')
        self.assertTrue(np.allclose(df_result['A'], self.df['A']))

    def test_square_root_scale(self):
        df_result = Scaler.square_root_scale(self.df.copy(), 'A')
        self.assertTrue(np.all(df_result['A'] >= 0))

    def test_reciprocal_scale(self):
        df = self.df.copy()
        df['A'] = df['A'].apply(lambda x: x + 1)  # Avoid division by zero
        df_result = Scaler.reciprocal_scale(df.copy(), 'A')
        self.assertTrue(np.all(df_result['A'] > 0))

if __name__ == '__main__':
    unittest.main()
