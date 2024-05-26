# Custom Viz Lib

カスタマイズ可能なデータビジュアライゼーションライブラリ

## 概要

Custom Viz Libは、インタラクティブでカスタマイズ可能なデータビジュアライゼーションを簡単に作成するためのライブラリです。

## 特徴

- インタラクティブなグラフとチャートの作成
- カスタマイズ可能なテーマとスタイル
- データストーリーテリングのサポート

## インストール

```bash
pip install custom_viz_lib
```

## 使い方
```python
from custom_viz_lib import chart, theme

# データの読み込み
data = [...]

# チャートの作成
bar_chart = chart.BarChart(data)
bar_chart.apply_theme(theme.DarkTheme())
bar_chart.show()
```

## ライセンス
This project is licensed under the MIT License.