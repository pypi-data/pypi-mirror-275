import matplotlib.pyplot as plt

class BarChart:
    def __init__(self, data):
        """BarChartクラスの初期化

        Args:
            data (list): データのリスト
        """
        self.data = data
        self.theme = None

    def apply_theme(self, theme):
        """テーマを適用

        Args:
            theme (Theme): テーマオブジェクト
        """
        self.theme = theme

    def show(self):
        """チャートを表示"""
        if self.theme:
            plt.style.use(self.theme.style)
        plt.bar(range(len(self.data)), self.data)
        plt.show()

class LineChart:
    def __init__(self, data):
        """LineChartクラスの初期化

        Args:
            data (list): データのリスト
        """
        self.data = data
        self.theme = None

    def apply_theme(self, theme):
        """テーマを適用

        Args:
            theme (Theme): テーマオブジェクト
        """
        self.theme = theme

    def show(self):
        """チャートを表示"""
        if self.theme:
            plt.style.use(self.theme.style)
        plt.plot(self.data)
        plt.show()