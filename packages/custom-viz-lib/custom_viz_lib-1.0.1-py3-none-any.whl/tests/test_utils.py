import unittest
from custom_viz_lib.utils import normalize_data

class TestUtils(unittest.TestCase):
    def test_normalize_data(self):
        data = [1, 2, 3]
        normalized = normalize_data(data)
        self.assertEqual(normalized, [0.0, 0.5, 1.0])

if __name__ == '__main__':
    unittest.main()