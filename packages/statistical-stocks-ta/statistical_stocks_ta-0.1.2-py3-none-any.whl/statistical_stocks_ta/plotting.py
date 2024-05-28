import mplfinance as mpf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
from mplfinance.original_flavor import candlestick_ohlc
from matplotlib.dates import DateFormatter


def plot_analysis(candles):
    fig1 = plot_smc(candles)
    fig2 = plot_mas_and_macd(candles)
    fig3 = plot_patterns_and_supp_res(candles)
    fig4 = plot_rsi_and_bb(candles)
    # fig5 = plot_smc_bis(candles)
    return (
        fig1,
        fig2,
        fig3,
        fig4,
        # fig5
    )


def has_valid_data(series):
    return not series.dropna().empty


def plot_smc(candles):
    fig, ax = plt.subplots()

    if not isinstance(candles.index, pd.DatetimeIndex):
        candles.index = pd.to_datetime(candles.index)

    candles = candles[candles.index.year != 1970]
    candles = candles.dropna(subset=["open", "high", "low", "close"])

    ohlc = candles[["open", "high", "low", "close"]]
    ohlc.reset_index(inplace=True)
    ohlc["ds"] = ohlc["ds"].map(mdates.date2num)

    def add_smc_plot(series, marker, color, label):
        valid_data = series.dropna()
        if not valid_data.empty:
            xdata = valid_data.index.to_numpy()
            ydata = valid_data.values
            if len(xdata) == len(ydata):
                ax.scatter(xdata, ydata, marker=marker, color=color, label=label, s=50)

    candlestick_ohlc(
        ax, ohlc.values, width=0.01, colorup="green", colordown="red", alpha=0.8
    )

    ax.xaxis_date()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))

    if "FVG" in candles.columns:
        fvg_up = candles[candles["FVG"] == 1]["close"]
        fvg_down = candles[candles["FVG"] == -1]["close"]
        add_smc_plot(fvg_up, "^", "black", "FVG Up")
        add_smc_plot(fvg_down, "v", "black", "FVG Down")

    if "Swings" in candles.columns:
        swings_high = candles[candles["Swings"] == 1]["close"]
        swings_low = candles[candles["Swings"] == -1]["close"]
        add_smc_plot(swings_high, "^", "blue", "Swings High")
        add_smc_plot(swings_low, "v", "orange", "Swings Low")

    if "BOS" in candles.columns:
        bos_up = candles[candles["BOS"] == 1]["close"]
        bos_down = candles[candles["BOS"] == -1]["close"]
        add_smc_plot(bos_up, "^", "lime", "BOS Up")
        add_smc_plot(bos_down, "v", "brown", "BOS Down")

    if "OB" in candles.columns:
        ob_up = candles[candles["OB"] > 0]["close"]
        add_smc_plot(ob_up, "o", "cyan", "Order Blocks")

    if "Liquidity" in candles.columns:
        liquidity_up = candles[candles["Liquidity"] == 1]["close"]
        liquidity_down = candles[candles["Liquidity"] == -1]["close"]
        add_smc_plot(liquidity_up, "o", "yellow", "Liquidity Up")
        add_smc_plot(liquidity_down, "o", "purple", "Liquidity Down")

    ax.set_title("SMC Indicators with Candlesticks")
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    ax.legend()

    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig


def plot_rsi_and_bb(candles):
    print("=== Plotting RSI and Bollinger Bands ===")
    apds = []

    if "BB_high" in candles.columns and "BB_low" in candles.columns:
        if has_valid_data(candles["BB_high"]):
            apds.append(
                mpf.make_addplot(
                    candles["BB_high"], color="blue", linestyle="dashed", width=1.2
                )
            )
        if has_valid_data(candles["BB_low"]):
            apds.append(
                mpf.make_addplot(
                    candles["BB_low"], color="blue", linestyle="dashed", width=1.2
                )
            )

    if "RSI" in candles.columns:
        if has_valid_data(candles["RSI"]):
            apds.append(
                mpf.make_addplot(
                    candles["RSI"], panel=1, color="purple", width=1.2, ylabel="RSI"
                )
            )

    fig, axlist = mpf.plot(
        candles,
        type="candle",
        style="charles",
        addplot=apds,
        title="RSI and Bollinger Bands",
        ylabel="Price",
        volume=True,
        ylabel_lower="volume",
        returnfig=True,
    )

    print("=== Plotting RSI and Bollinger Bands completed ===")

    return fig


def plot_mas_and_macd(candles):
    print("=== Plotting MAs and MACD ===")
    apds = []

    if "SMA_Short" in candles.columns and "SMA_Long" in candles.columns:
        if has_valid_data(candles["SMA_Short"]):
            apds.append(
                mpf.make_addplot(
                    candles["SMA_Short"], color="green", linestyle="solid", width=1.2
                )
            )
        if has_valid_data(candles["SMA_Long"]):
            apds.append(
                mpf.make_addplot(
                    candles["SMA_Long"], color="red", linestyle="solid", width=1.2
                )
            )

    if "EMA_Short" in candles.columns and "EMA_Long" in candles.columns:
        if has_valid_data(candles["EMA_Short"]):
            apds.append(
                mpf.make_addplot(
                    candles["EMA_Short"], color="green", linestyle="dotted", width=1.2
                )
            )
        if has_valid_data(candles["EMA_Long"]):
            apds.append(
                mpf.make_addplot(
                    candles["EMA_Long"], color="red", linestyle="dotted", width=1.2
                )
            )

    if "MACD" in candles.columns and "MACD_Signal" in candles.columns:
        if has_valid_data(candles["MACD"]):
            apds.append(
                mpf.make_addplot(
                    candles["MACD"], panel=1, color="blue", width=1.2, ylabel="MACD"
                )
            )
        if has_valid_data(candles["MACD_Signal"]):
            apds.append(
                mpf.make_addplot(
                    candles["MACD_Signal"], panel=1, color="red", width=1.2
                )
            )

    fig, axlist = mpf.plot(
        candles,
        type="candle",
        style="charles",
        addplot=apds,
        title="Moving Averages and MACD",
        ylabel="Price",
        volume=True,
        ylabel_lower="volume",
        returnfig=True,
    )

    print("=== Plotting MAs and MACD completed ===")

    return fig


def plot_patterns_and_supp_res(candles):
    print("=== Plotting Patterns and Support/Resistance ===")
    apds = []

    if "Support_Q" in candles.columns and "Resistance_Q" in candles.columns:
        if has_valid_data(candles["Support_Q"]):
            apds.append(
                mpf.make_addplot(
                    candles["Support_Q"], color="green", linestyle="dashed", width=2.3
                )
            )
        if has_valid_data(candles["Resistance_Q"]):
            apds.append(
                mpf.make_addplot(
                    candles["Resistance_Q"],
                    color="red",
                    linestyle="dashed",
                    width=2.3,
                )
            )

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

    for pattern, color in pattern_colors.items():
        if pattern in candles.columns:
            aligned_series = candles[pattern].replace(0, np.nan)
            aligned_values = candles["close"] * aligned_series

            if has_valid_data(aligned_values):
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

    fig, axlist = mpf.plot(
        candles,
        type="candle",
        style="charles",
        addplot=apds,
        title="Patterns and Support/Resistance",
        ylabel="Price",
        volume=True,
        ylabel_lower="volume",
        returnfig=True,
    )

    print("=== Plotting Patterns and Support/Resistance completed ===")

    return fig


def plot_smc_bis(candles):
    print("=== Plotting SMC with Matplotlib ===")
    print(candles)

    # Ensure there is data to plot
    if candles.empty:
        print("No data available for plotting.")
        return None

    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_title("SMC Indicators")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")

    # Plotting the candlestick chart manually
    def plot_candlestick(ax, data):
        for idx, row in data.iterrows():
            color = "green" if row["close"] >= row["open"] else "red"
            ax.plot([idx, idx], [row["low"], row["high"]], color="black")
            ax.plot([idx, idx], [row["open"], row["close"]], color=color, linewidth=4)

    plot_candlestick(ax, candles)

    # Function to check and add plot if there is valid data
    def add_smc_plot(data, marker, color, label):
        valid_data = data.dropna()
        print(f"Checking {label} data for plotting:")
        print(valid_data)
        if not valid_data.empty:
            ax.scatter(
                candles.index, valid_data, marker=marker, color=color, label=label, s=50
            )
        else:
            print(f"No valid data for {label}")

    # SMC data
    if "FVG_bis" in candles.columns:
        fvg_up = candles["FVG_bis"].apply(lambda x: x if x == 1 else np.nan)
        fvg_down = candles["FVG_bis"].apply(lambda x: x if x == -1 else np.nan)
        add_smc_plot(fvg_up, "^", "green", "FVG Up")
        add_smc_plot(fvg_down, "v", "red", "FVG Down")

    if "Swings_bis" in candles.columns:
        swings_high = candles["Swings_bis"].apply(lambda x: x if x == 1 else np.nan)
        swings_low = candles["Swings_bis"].apply(lambda x: x if x == -1 else np.nan)
        add_smc_plot(swings_high, "^", "blue", "Swings High")
        add_smc_plot(swings_low, "v", "orange", "Swings Low")

    if "BOS_bis" in candles.columns:
        bos_up = candles["BOS_bis"].apply(lambda x: x if x == 1 else np.nan)
        bos_down = candles["BOS_bis"].apply(lambda x: x if x == -1 else np.nan)
        add_smc_plot(bos_up, "^", "lime", "BOS Up")
        add_smc_plot(bos_down, "v", "brown", "BOS Down")

    if "OB_bis" in candles.columns:
        ob_up = candles["OB_bis"].apply(lambda x: x if x == 1 else np.nan)
        ob_down = candles["OB_bis"].apply(lambda x: x if x == -1 else np.nan)
        add_smc_plot(ob_up, "o", "cyan", "OB Up")
        add_smc_plot(ob_down, "o", "magenta", "OB Down")

    if "Liquidity_bis" in candles.columns:
        liquidity_up = candles["Liquidity_bis"].apply(lambda x: x if x == 1 else np.nan)
        liquidity_down = candles["Liquidity_bis"].apply(
            lambda x: x if x == -1 else np.nan
        )
        add_smc_plot(liquidity_up, "o", "yellow", "Liquidity Up")
        add_smc_plot(liquidity_down, "o", "purple", "Liquidity Down")

    # Formatting x-axis to show dates nicely
    ax.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
    fig.autofmt_xdate()

    # Adding legend
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    print("=== Plotting SMC with Matplotlib completed ===")
    return fig
