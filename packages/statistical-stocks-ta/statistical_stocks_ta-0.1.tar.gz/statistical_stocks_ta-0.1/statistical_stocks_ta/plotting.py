import mplfinance as mpf
import numpy as np


def plot_analysis(candles):
    print("=== Plotting analysis ===")

    # Stores additional plots as a list of dictionaries for mplfinance
    apds = []

    # Bollinger Bands
    if "BB_High" in candles.columns and "BB_Low" in candles.columns:
        apds.append(
            mpf.make_addplot(
                candles["BB_High"], color="blue", linestyle="dashed", width=1.2
            )
        )
        apds.append(
            mpf.make_addplot(
                candles["BB_Low"], color="blue", linestyle="dashed", width=1.2
            )
        )

    # Support and Resistance levels
    if "Support_Q" in candles.columns and "Resistance_Q" in candles.columns:
        apds.append(
            mpf.make_addplot(
                candles["Support_Q"], color="yellow", linestyle="dashed", width=1.2
            )
        )
        apds.append(
            mpf.make_addplot(
                candles["Resistance_Q"], color="orange", linestyle="dashed", width=1.2
            )
        )

    # Moving Averages
    if "SMA_Short" in candles.columns and "SMA_Long" in candles.columns:
        apds.append(
            mpf.make_addplot(
                candles["SMA_Short"], color="green", linestyle="solid", width=1.2
            )
        )
        apds.append(
            mpf.make_addplot(
                candles["SMA_Long"], color="red", linestyle="solid", width=1.2
            )
        )

    if "EMA_Short" in candles.columns and "EMA_Long" in candles.columns:
        apds.append(
            mpf.make_addplot(
                candles["EMA_Short"], color="green", linestyle="dotted", width=1.2
            )
        )
        apds.append(
            mpf.make_addplot(
                candles["EMA_Long"], color="red", linestyle="dotted", width=1.2
            )
        )

    # MACD and RSI
    if "MACD" in candles.columns and "MACD_Signal" in candles.columns:
        apds.append(
            mpf.make_addplot(
                candles["MACD"], panel=2, color="blue", width=1.2, ylabel="MACD"
            )
        )
        apds.append(
            mpf.make_addplot(candles["MACD_Signal"], panel=2, color="red", width=1.2)
        )

    if "RSI" in candles.columns:
        apds.append(
            mpf.make_addplot(
                candles["RSI"], panel=1, color="purple", width=1.2, ylabel="RSI"
            )
        )

    # Dynamic Pattern Plotting
    pattern_colors = {
        "Bullish_Divergence": "green",
        "Bearish_Divergence": "red",
        "Bullish_Reversal": "blue",
        "Bearish_Reversal": "black",
        "Doji": "gold",
        "Bearish_Engulfing": "cyan",
        "Bullish_Engulfing": "magenta",
        "Flag": "magenta",
        "Triangle": "brown",
        "Channel_Up": "green",
        "Channel_Down": "red",
    }

    print(pattern_colors.items())

    for pattern, color in pattern_colors.items():
        if pattern in candles.columns:
            aligned_series = candles[pattern].replace(
                0, np.nan
            )  # Replace non-occurrences with NaN
            aligned_values = (
                candles["Close"] * aligned_series
            )  # Multiply by Close to keep price points, NaN elsewhere

            if not aligned_values.dropna().empty:
                apds.append(
                    mpf.make_addplot(
                        aligned_values,
                        scatter=True,
                        markersize=100,
                        marker="o",
                        color=color,
                        secondary_y=False,
                    )
                )

    # Plotting with mplfinance
    mpf.plot(
        candles,
        type="candle",
        style="charles",
        addplot=apds,
        title="Comprehensive Stock Analysis",
        ylabel="Price",
        volume=True,
        ylabel_lower="Volume",
    )

    print("=== Plotting completed ===")
