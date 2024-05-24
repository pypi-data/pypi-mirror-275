import unittest
import pandas as pd
from dataPreprocessing.feature_engineer import FeatureEngineer


class TestFeatureEngineer(unittest.TestCase):


    def setUp(self):
        self.data = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': [4, 3, 2, 1]
        })

    def test_add_difference(self):
        df = FeatureEngineer.add_difference(self.data.copy(), 'A', 'B', 'A_minus_B')
        self.assertIn('A_minus_B', df.columns)
        self.assertListEqual(list(df['A_minus_B']), [-3, -1, 1, 3])

    def test_add_product(self):
        df = FeatureEngineer.add_product(self.data.copy(), 'A', 'B', 'A_times_B')
        self.assertIn('A_times_B', df.columns)
        self.assertListEqual(list(df['A_times_B']), [4, 6, 6, 4])

    def test_add_sum(self):
        df = FeatureEngineer.add_sum(self.data.copy(), 'A', 'B', 'A_plus_B')
        self.assertIn('A_plus_B', df.columns)
        self.assertListEqual(list(df['A_plus_B']), [5, 5, 5, 5])

    def test_add_square(self):
        df = FeatureEngineer.add_square(self.data.copy(), 'A', 'A_squared')
        self.assertIn('A_squared', df.columns)
        self.assertListEqual(list(df['A_squared']), [1, 4, 9, 16])


if __name__ == '__main__':
    unittest.main()
