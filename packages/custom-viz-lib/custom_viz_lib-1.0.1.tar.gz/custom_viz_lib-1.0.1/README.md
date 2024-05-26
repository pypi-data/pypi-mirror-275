# Custom Viz Lib

A customizable data visualization library

## Overview

Custom Viz Lib is a library for easily creating interactive and customizable data visualizations.

## Features

- Create interactive graphs and charts
- Customizable themes and styles
- Support for data storytelling

## Customization Details

### Chart Types
- `BarChart`: Bar Chart
- `LineChart`: Line Chart

### Themes
- `DarkTheme`: Dark Theme
- `LightTheme`: Light Theme

### Data Loading
- `load_csv(file_path)`: Function to load data from a CSV file

### Utilities
- `normalize_data(data)`: Function to normalize data to a range of 0 to 1

## Installation

```bash
pip install custom_viz_lib
```

## Usage
```python
from custom_viz_lib import chart, theme

# Load data
data = [...]

# Create a chart
bar_chart = chart.BarChart(data)
bar_chart.apply_theme(theme.DarkTheme())
bar_chart.show()
```

## Example 1: Using in Google Colab to create a bar chart
```python
!pip install custom_viz_lib

from custom_viz_lib.chart import BarChart
from custom_viz_lib.theme import DarkTheme

# Sample data
data = [1, 2, 3, 4, 5]
chart = BarChart(data)
chart.apply_theme(DarkTheme())
chart.show()
```

## Example 2: Using in Google Colab to create a line chart
```python
!pip install custom_viz_lib

from custom_viz_lib.chart import LineChart
from custom_viz_lib.theme import LightTheme

# Sample data
data = [10, 20, 15, 25, 30]
chart = LineChart(data)
chart.apply_theme(LightTheme())
chart.show()
```

## Example 3: Using in Google Colab to load data from a CSV file and create a bar chart
```python
!pip install custom_viz_lib

import pandas as pd
from custom_viz_lib.chart import BarChart
from custom_viz_lib.theme import DarkTheme
from custom_viz_lib.data_loader import load_csv

# Path to CSV file
file_path = 'path/to/your/data.csv'

# Load data
data = load_csv(file_path)['column_name'].tolist()
chart = BarChart(data)
chart.apply_theme(DarkTheme())
chart.show()
```

## Example 4: Using in Google Colab to normalize data and create a line chart
```python
!pip install custom_viz_lib

from custom_viz_lib.chart import LineChart
from custom_viz_lib.theme import LightTheme
from custom_viz_lib.utils import normalize_data

# Sample data
data = [10, 20, 15, 25, 30]

# Normalize data
normalized_data = normalize_data(data)
chart = LineChart(normalized_data)
chart.apply_theme(LightTheme())

chart.show()
```

## License
This project is licensed under the MIT License.