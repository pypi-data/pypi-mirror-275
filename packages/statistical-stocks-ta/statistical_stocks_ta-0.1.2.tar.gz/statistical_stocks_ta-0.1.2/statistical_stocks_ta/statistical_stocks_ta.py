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
from smc import compute_smc, compute_smc_bis
from patterns import identify_patterns
from plotting import plot_analysis, plot_smc
import matplotlib.pyplot as plt


def fetch_data(symbol="ETH/USDT", timeframe="4h", limit=300):
    exchange = ccxt.binance({"rateLimit": 1200, "enableRateLimit": True})
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    data = pd.DataFrame(ohlcv, columns=["ds", "open", "high", "low", "close", "volume"])
    data["ds"] = pd.to_datetime(data["ds"], unit="ms")
    data.set_index("ds", inplace=True)
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
    smc=True,
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

    if smc:
        candles = compute_smc(candles)

    if plot:
        fig1, fig2, fig3, fig4 = plot_analysis(candles, **plot_settings)

    return candles


def main():
    candles = fetch_data()
    candles = identify_patterns(candles)
    candles = calculate_rsi(candles)
    candles = calculate_macd(candles)
    candles = calculate_moving_averages(candles)
    candles = calculate_bollinger_bands(candles)
    candles = quantile_regression_support_resistance(candles)
    candles = compute_smc(candles)
    # candles = compute_smc_bis(candles)
    # Check if the DataFrame is not empty
    if candles.empty:
        print("No data available after SMC computation.")
        return
    fig1, _, _, _ = plot_analysis(candles)
    plt.show()


if __name__ == "__main__":
    main()
