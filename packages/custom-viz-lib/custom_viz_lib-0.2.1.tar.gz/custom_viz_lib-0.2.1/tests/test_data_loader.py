import unittest
import pandas as pd
from custom_viz_lib.data_loader import load_csv

class TestDataLoader(unittest.TestCase):
    def test_load_csv(self):
        data = load_csv('sample.csv')
        self.assertIsInstance(data, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()