# Statistical Stocks TA

The `statistical-stocks-ta` provides a comprehensive suite of tools for technical analysis and visualization of financial time series data. This package supports the calculation of various technical indicators, pattern detection, plotting analysis, and more.

## Installation

To install the package, you can use `pip`:

```bash
pip install statistical-stocks-ta
```

## Usage

### Fetching Data

First, fetch the OHLCV data using the `fetch_data` function:

```python
from statistical_ta import fetch_data

data = fetch_data(symbol='SOL/USDT', timeframe='1h', limit=300)
```

## Functions

### analyze_candles

Analyzes the given OHLCV data using various technical indicators and patterns.

```python
import pandas as pd
from statistical_ta import analyze_candles

candles = pd.read_csv('data.csv')
candles = analyze_candles(candles)
```

### Parameters:

- `candles` (DataFrame): DataFrame containing the OHLCV data.
- `calc_bollinger_bands` (bool, optional): Whether to calculate Bollinger Bands. Default is True.
- `bb_settings` (dict, optional): Settings for Bollinger Bands calculation. Default is `{"window": 20, "std_dev": 2}`.
- `calc_moving_averages` (bool, optional): Whether to calculate moving averages. Default is True.
- `ma_settings` (dict, optional): Settings for moving averages calculation. Default is `{"short_window": 20, "long_window": 50}`.
- `calc_rsi` (bool, optional): Whether to calculate RSI. Default is True.
- `rsi_settings` (dict, optional): Settings for RSI calculation. Default is `{"window": 14}`.
- `calc_macd` (bool, optional): Whether to calculate MACD. Default is True.
- `macd_settings` (dict, optional): Settings for MACD calculation. Default is `{}`.
- `detect_patterns` (bool, optional): Whether to detect patterns. Default is True.
- `pattern_settings` (dict, optional): Settings for pattern detection. Default is `{}`.
- `plot` (bool, optional): Whether to plot the analysis. Default is True.
- `plot_settings` (dict, optional): Settings for plotting. Default is `{}`.

### calculate_bollinger_bands

Calculates Bollinger Bands for the given data.

```python
import pandas as pd
from indicators import calculate_bollinger_bands

candles = pd.read_csv('data.csv')
candles = calculate_bollinger_bands(candles)
```

### Parameters:

- `candles` (DataFrame): DataFrame containing the OHLCV data.
- `window` (int, optional): The number of periods to use for the moving average. Default is 20.
- `std_dev` (int, optional): The number of standard deviations to use for the bands. Default is 2.

### calculate_moving_averages

Calculates simple and exponential moving averages for the given data.

```python
import pandas as pd
from indicators import calculate_moving_averages

candles = pd.read_csv('data.csv')
candles = calculate_moving_averages(candles)
```

### Parameters:

- `candles` (DataFrame): DataFrame containing the OHLCV data.
- `short_window` (int, optional): The number of periods for the short moving average. Default is 20.
- `long_window` (int, optional): The number of periods for the long moving average. Default is 50.

### calculate_rsi

Calculates the Relative Strength Index (RSI) for the given data.

```python
import pandas as pd
from indicators import calculate_rsi

candles = pd.read_csv('data.csv')
candles = calculate_rsi(candles)
```

### Parameters:

- `candles` (DataFrame): DataFrame containing the OHLCV data.
- `window` (int, optional): The number of periods to use for the RSI calculation. Default is 14.

### calculate_macd

Calculates the Moving Average Convergence Divergence (MACD) for the given data.

```python
import pandas as pd
from indicators import calculate_macd

candles = pd.read_csv('data.csv')
candles = calculate_macd(candles)
```

### Parameters:

- `candles` (DataFrame): DataFrame containing the OHLCV data.

### detect_flags

Detects flag patterns in the given data.

```python
import pandas as pd
from patterns import detect_flags

candles = pd.read_csv('data.csv')
candles = detect_flags(candles)
```

### Parameters:

- `candles` (DataFrame): DataFrame containing the OHLCV data.
- `trend_window` (int, optional): The number of periods to define the prior trend. Default is 20.
- `flag_window` (int, optional): The number of periods for the flag pattern. Default is 5.
- `breakout_threshold` (float, optional): The threshold for breakout detection. Default is 0.1.

### identify_patterns

Identifies various candlestick patterns in the given data.

```python
import pandas as pd
from patterns import identify_patterns

candles = pd.read_csv('data.csv')
candles = identify_patterns(candles)
```

### Parameters:

- `candles` (DataFrame): DataFrame containing the OHLCV data.
- `doji_threshold` (float, optional): The threshold for detecting Doji candles. Default is 0.1.
- `buffer_factor` (float, optional): The factor for adjusting buffer in channel detection. Default is 0.5.
- `rolling_window` (int, optional): The window size for rolling calculations. Default is 10.
- `channel_window_range` (tuple, optional): The range for channel window size. Default is (10, 15).
- `flag_sensitivity` (float, optional): Sensitivity for flag detection. Default is 0.8.

### plot_analysis

Plots the analysis of the given data using `mplfinance`.

```python
import pandas as pd
from plotting import plot_analysis

candles = pd.read_csv('data.csv')
plot_analysis(candles)
```

### Parameters:

- `candles` (DataFrame): DataFrame containing the OHLCV data.

### quantile_regression_support_resistance

Calculates support and resistance levels using quantile regression.

```python
import pandas as pd
from support_resistance import quantile_regression_support_resistance

candles = pd.read_csv('data.csv')
candles = quantile_regression_support_resistance(candles)
```

### Parameters:

- `candles` (DataFrame): DataFrame containing the OHLCV data.
- `quantiles` (list, optional): List of quantiles to calculate. Default is `[0.10, 0.90]`.
