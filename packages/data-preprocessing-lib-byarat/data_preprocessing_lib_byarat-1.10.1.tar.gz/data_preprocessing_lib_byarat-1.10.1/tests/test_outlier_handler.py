import unittest
import pandas as pd
import numpy as np
from data_preprocessing_lib_byarat import OutlierHandler

class TestOutlierHandler(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 100],
            'B': [1, 1, 2, 2, 2]
        })

    def test_iqr_outlier_detection(self):
        df_result = OutlierHandler.iqr_outlier_detection(self.df.copy(), 'A')
        self.assertEqual(df_result.shape[0], 4)

    def test_detect_outliers_iqr(self):
        outliers = OutlierHandler.detect_outliers_iqr(self.df.copy(), 'A')
        self.assertEqual(outliers.shape[0], 1)

    def test_remove_outliers(self):
        df_result = OutlierHandler.remove_outliers(self.df.copy(), 'A')
        self.assertEqual(df_result.shape[0], 4)

    def test_z_score_outlier_detection(self):
        df_result = OutlierHandler.z_score_outlier_detection(self.df.copy(), 'A')
        self.assertEqual(df_result.shape[0], 4)

    def test_detect_outliers_z_score(self):
        outliers = OutlierHandler.detect_outliers_z_score(self.df.copy(), 'A')
        self.assertEqual(outliers.shape[0], 1)

    def test_remove_outliers_z_score(self):
        df_result = OutlierHandler.remove_outliers_z_score(self.df.copy(), 'A')
        self.assertEqual(df_result.shape[0], 4)

    def test_mad_outlier_detection(self):
        df_result = OutlierHandler.mad_outlier_detection(self.df.copy(), 'A')
        self.assertEqual(df_result.shape[0], 4)

    def test_detect_outliers_mad(self):
        outliers = OutlierHandler.detect_outliers_mad(self.df.copy(), 'A')
        self.assertEqual(outliers.shape[0], 1)

    def test_remove_outliers_mad(self):
        df_result = OutlierHandler.remove_outliers_mad(self.df.copy(), 'A')
        self.assertEqual(df_result.shape[0], 4)

    def test_mahalanobis_outlier_detection(self):
        df_result = OutlierHandler.mahalanobis_outlier_detection(self.df.copy(), 'A')
        self.assertEqual(df_result.shape[0], 4)

    def test_detect_outliers_mahalanobis(self):
        outliers = OutlierHandler.detect_outliers_mahalanobis(self.df.copy(), 'A')
        self.assertEqual(outliers.shape[0], 1)

    def test_remove_outliers_mahalanobis(self):
        df_result = OutlierHandler.remove_outliers_mahalanobis(self.df.copy(), 'A')
        self.assertEqual(df_result.shape[0], 4)

    def test_tukeys_fences_outlier_detection(self):
        df_result = OutlierHandler.tukeys_fences_outlier_detection(self.df.copy(), 'A')
        self.assertEqual(df_result.shape[0], 4)

    def test_detect_outliers_tukeys_fences(self):
        outliers = OutlierHandler.detect_outliers_tukeys_fences(self.df.copy(), 'A')
        self.assertEqual(outliers.shape[0], 1)

    def test_remove_outliers_tukeys_fences(self):
        df_result = OutlierHandler.remove_outliers_tukeys_fences(self.df.copy(), 'A')
        self.assertEqual(df_result.shape[0], 4)

    def test_isolation_forest_outlier_detection(self):
        df_result = OutlierHandler.isolation_forest_outlier_detection(self.df.copy(), 'A')
        self.assertEqual(df_result.shape[0], 4)

    def test_detect_outliers_isolation_forest(self):
        outliers = OutlierHandler.detect_outliers_isolation_forest(self.df.copy(), 'A')
        self.assertEqual(outliers.shape[0], 1)

    def test_remove_outliers_isolation_forest(self):
        df_result = OutlierHandler.remove_outliers_isolation_forest(self.df.copy(), 'A')
        self.assertEqual(df_result.shape[0], 4)

    def test_local_outlier_factor_detection(self):
        df_result = OutlierHandler.local_outlier_factor_detection(self.df.copy(), 'A')
        self.assertEqual(df_result.shape[0], 4)

    def test_detect_outliers_local_outlier_factor(self):
        outliers = OutlierHandler.detect_outliers_local_outlier_factor(self.df.copy(), 'A')
        self.assertEqual(outliers.shape[0], 1)

    def test_remove_outliers_local_outlier_factor(self):
        df_result = OutlierHandler.remove_outliers_local_outlier_factor(self.df.copy(), 'A')
        self.assertEqual(df_result.shape[0], 4)

    def test_dbscan_outlier_detection(self):
        df_result = OutlierHandler.dbscan_outlier_detection(self.df.copy(), 'A')
        self.assertEqual(df_result.shape[0], 4)

    def test_detect_outliers_dbscan(self):
        outliers = OutlierHandler.detect_outliers_dbscan(self.df.copy(), 'A')
        self.assertEqual(outliers.shape[0], 1)

    def test_remove_outliers_dbscan(self):
        df_result = OutlierHandler.remove_outliers_dbscan(self.df.copy(), 'A')
        self.assertEqual(df_result.shape[0], 4)

if __name__ == '__main__':
    unittest.main()
