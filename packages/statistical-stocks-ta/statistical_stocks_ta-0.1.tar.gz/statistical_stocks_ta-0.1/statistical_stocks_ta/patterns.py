import numpy as np


def detect_flags(candles, trend_window=20, flag_window=5, breakout_threshold=0.1):
    # Initialize flag column with None
    candles["Flag"] = None

    # Calculate returns to identify strong movements
    candles["Returns"] = candles["Close"].pct_change()

    # Loop through candles
    for i in range(trend_window + flag_window, len(candles)):
        # Define the prior trend
        trend_period = candles.iloc[i - trend_window - flag_window : i - flag_window]
        trend_up = trend_period["Returns"].sum() > 0
        trend_down = trend_period["Returns"].sum() < 0

        # Defining the flag consolidation
        flag_period = candles.iloc[i - flag_window : i]
        max_high = flag_period["High"].max()
        min_low = flag_period["Low"].min()
        range_c = max_high - min_low

        # Flag validation conditions
        within_range = (
            flag_period["High"] < max_high + (range_c * breakout_threshold)
        ) & (flag_period["Low"] > min_low - (range_c * breakout_threshold))

        # Check if all candles in flag window meet the range condition
        if within_range.all():
            # Check for breakout
            current_candle = candles.iloc[i]
            if trend_up and current_candle["Close"] > max_high:
                candles.at[candles.index[i], "Flag"] = "bullish"
            elif trend_down and current_candle["Close"] < min_low:
                candles.at[candles.index[i], "Flag"] = "bearish"

    return candles


def identify_patterns(
    candles,
    doji_threshold=0.1,
    buffer_factor=0.5,
    rolling_window=10,
    channel_window_range=(10, 15),
    flag_sensitivity=0.8,
):
    # Detecting Doji candles
    candles["Doji"] = np.where(
        (
            abs(candles["Close"] - candles["Open"]) / (candles["High"] - candles["Low"])
            < doji_threshold
        )
        & (
            (candles["High"] - candles["Low"])
            > candles["Close"].rolling(window=rolling_window).std()
        ),
        1,
        0,
    )

    print("Doji candles: ", candles["Doji"].sum())

    # Detecting Engulfing patterns
    candles["Bullish_Engulfing"] = np.where(
        (candles["Close"].shift(1) < candles["Open"].shift(1))
        & (candles["Open"] < candles["Close"].shift(1))
        & (candles["Close"] > candles["Open"].shift(1)),
        1,
        0,
    )

    print("Bullish Engulfing: ", candles["Bullish_Engulfing"].sum())

    candles["Bearish_Engulfing"] = np.where(
        (candles["Open"].shift(1) < candles["Close"].shift(1))
        & (candles["Open"] > candles["Close"].shift(1))
        & (candles["Close"] < candles["Open"].shift(1)),
        1,
        0,
    )

    print("Bearish Engulfing: ", candles["Bearish_Engulfing"].sum())

    def dynamic_window(candles):
        # Example of dynamic window based on recent volatility
        returns = candles["Close"].pct_change()
        vol = returns.rolling(window=rolling_window).std()
        scaled_window = (
            (20 / vol)
            .fillna(20)
            .astype(int)
            .clip(lower=channel_window_range[0], upper=channel_window_range[1])
        )
        return scaled_window

    # Window calculation and channel identification
    window = dynamic_window(candles)
    channel_up = np.zeros(len(candles), dtype=int)
    channel_down = np.zeros(len(candles), dtype=int)

    for i in range(len(candles)):
        if i >= window.iloc[i]:
            roll_high = candles["High"].iloc[i - window.iloc[i] : i].max()
            roll_low = candles["Low"].iloc[i - window.iloc[i] : i].min()

            std_dev = candles["Close"].iloc[i - window.iloc[i] : i].std()
            buffer = buffer_factor * std_dev  # Adjust buffer factor

            channel_up[i] = 1 if candles["High"].iloc[i] >= roll_high + buffer else 0
            channel_down[i] = 1 if candles["Low"].iloc[i] <= roll_low - buffer else 0

    candles["Channel_Up"] = channel_up
    candles["Channel_Down"] = channel_down
    print("Channel Up: ", candles["Channel_Up"].sum())
    print("Channel Down: ", candles["Channel_Down"].sum())

    return candles
