import unittest
from custom_viz_lib.theme import DarkTheme, LightTheme

class TestTheme(unittest.TestCase):
    def test_dark_theme(self):
        self.assertEqual(DarkTheme.style, 'dark_background')

    def test_light_theme(self):
        self.assertEqual(LightTheme.style, 'default')

if __name__ == '__main__':
    unittest.main()