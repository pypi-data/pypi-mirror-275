import unittest
from custom_viz_lib.chart import BarChart, LineChart
from custom_viz_lib.theme import DarkTheme

class TestBarChart(unittest.TestCase):
    def test_bar_chart(self):
        data = [1, 2, 3]
        chart = BarChart(data)
        chart.apply_theme(DarkTheme())
        chart.show()  # 実際の表示を確認するための手動テストが必要

class TestLineChart(unittest.TestCase):
    def test_line_chart(self):
        data = [1, 2, 3]
        chart = LineChart(data)
        chart.apply_theme(DarkTheme())
        chart.show()  # 実際の表示を確認するための手動テストが必要

if __name__ == '__main__':
    unittest.main()