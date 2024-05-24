import unittest
import pandas as pd
from dataPreprocessing.categorical_encoder import CategoricalEncoder


class TestCategoricalEncoder(unittest.TestCase):


    def setUp(self):
        self.data = pd.DataFrame({
            'category': ['A', 'B', 'A', 'C']
        })

    def test_label_encode(self):
        df, le = CategoricalEncoder.label_encode(self.data.copy(), 'category')
        self.assertTrue(pd.api.types.is_integer_dtype(df['category']))
        self.assertListEqual(list(df['category']), [0, 1, 0, 2])

    def test_one_hot_encode(self):
        df, ohe = CategoricalEncoder.one_hot_encode(self.data.copy(), 'category')
        self.assertTrue(all(col in df.columns for col in ['category_A', 'category_B', 'category_C']))
        self.assertEqual(df['category_A'].iloc[0], 1.0)
        self.assertEqual(df['category_B'].iloc[1], 1.0)
        self.assertEqual(df['category_C'].iloc[3], 1.0)


if __name__ == '__main__':
    unittest.main()
