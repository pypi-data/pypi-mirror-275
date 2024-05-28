# statistical_ta.py

import pandas as pd
import ccxt

from support_resistance import quantile_regression_support_resistance
from indicators import (
    calculate_bollinger_bands,
    calculate_moving_averages,
    calculate_rsi,
    calculate_macd,
)
from patterns import identify_patterns
from plotting import plot_analysis


def fetch_data(symbol="SOL/USDT", timeframe="1h", limit=300):
    exchange = ccxt.binance({"rateLimit": 1200, "enableRateLimit": True})
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    data = pd.DataFrame(
        ohlcv, columns=["Date", "Open", "High", "Low", "Close", "Volume"]
    )
    data["Date"] = pd.to_datetime(data["Date"], unit="ms")
    data.set_index("Date", inplace=True)
    return data


def analyze_candles(
    candles,
    calc_bollinger_bands=True,
    bb_settings={"window": 20, "std_dev": 2},
    calc_moving_averages=True,
    ma_settings={"short_window": 20, "long_window": 50},
    calc_rsi=True,
    rsi_settings={"window": 14},
    calc_macd=True,
    macd_settings={},
    detect_patterns=True,
    pattern_settings={},
    plot=True,
    plot_settings={},
):
    if calc_bollinger_bands:
        candles = calculate_bollinger_bands(candles, **bb_settings)

    if calc_moving_averages:
        candles = calculate_moving_averages(candles, **ma_settings)

    if calc_rsi:
        candles = calculate_rsi(candles, **rsi_settings)

    if calc_macd:
        candles = calculate_macd(candles, **macd_settings)

    if detect_patterns:
        candles = identify_patterns(candles, **pattern_settings)

    if plot:
        plot_analysis(candles, **plot_settings)

    return candles


def main():
    candles = fetch_data()
    candles = analyze_candles(candles)


if __name__ == "__main__":
    main()
