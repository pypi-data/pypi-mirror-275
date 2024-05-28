import numpy as np
from ta.volatility import BollingerBands
from ta.trend import SMAIndicator, EMAIndicator
from ta.momentum import RSIIndicator
from ta.trend import MACD


def calculate_bollinger_bands(candles, window=20, std_dev=2):
    indicator_bb = BollingerBands(
        close=candles["Close"], window=window, window_dev=std_dev
    )
    candles["BB_High"] = indicator_bb.bollinger_hband()
    candles["BB_Low"] = indicator_bb.bollinger_lband()
    return candles


def calculate_moving_averages(candles, short_window=20, long_window=50):
    sma_short = SMAIndicator(close=candles["Close"], window=short_window)
    sma_long = SMAIndicator(close=candles["Close"], window=long_window)
    ema_short = EMAIndicator(close=candles["Close"], window=short_window)
    ema_long = EMAIndicator(close=candles["Close"], window=long_window)
    candles["SMA_Short"] = sma_short.sma_indicator()
    candles["SMA_Long"] = sma_long.sma_indicator()
    candles["EMA_Short"] = ema_short.ema_indicator()
    candles["EMA_Long"] = ema_long.ema_indicator()
    return candles


def calculate_rsi(candles, window=14):
    rsi = RSIIndicator(close=candles["Close"], window=window)
    candles["RSI"] = rsi.rsi()
    return candles


def calculate_macd(candles):
    macd = MACD(close=candles["Close"])
    candles["MACD"] = macd.macd()
    candles["MACD_Signal"] = macd.macd_signal()
    candles["MACD_Diff"] = macd.macd_diff()
    return candles
