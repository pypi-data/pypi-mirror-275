import unittest
import pandas as pd
from dataPreprocessing.outlier_handler import OutlierHandler

class TestOutlierHandler(unittest.TestCase):


    def setUp(self):
        self.data = pd.DataFrame({
            'A': [1, 2, 3, 4, 100],
            'B': [1, 2, 3, 4, 5]
        })

    def test_outlier_removal(self):
        handler = OutlierHandler(method="iqr", threshold=1.5)
        transformed = handler.fit_transform(self.data)
        expected = pd.DataFrame({
            'A': [1, 2, 3, 4, 7],
            'B': [1, 2, 3, 4, 5]
        })
        # Ensure expected types match the original DataFrame
        expected['A'] = expected['A'].astype(self.data['A'].dtype)
        expected['B'] = expected['B'].astype(self.data['B'].dtype)
        pd.testing.assert_frame_equal(transformed, expected)

    def test_invalid_method(self):
        with self.assertRaises(ValueError):
            handler = OutlierHandler(method="invalid_method")
            handler.fit(self.data)

    def test_custom_threshold(self):
        handler = OutlierHandler(method="iqr", threshold=3)
        transformed = handler.fit_transform(self.data)
        expected = pd.DataFrame({
            'A': [1, 2, 3, 4, 10],
            'B': [1, 2, 3, 4, 5]
        })
        # Ensure expected types match the original DataFrame
        expected['A'] = expected['A'].astype(self.data['A'].dtype)
        expected['B'] = expected['B'].astype(self.data['B'].dtype)
        pd.testing.assert_frame_equal(transformed, expected)

if __name__ == '__main__':
    unittest.main()
