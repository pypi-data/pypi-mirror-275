import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.tsa.stattools import adfuller
from sklearn.cluster import DBSCAN
from smartmoneyconcepts import smc


def compute_smc(
    candles,
    fvg_zscore_threshold=3.14,
    swing_length=50,
    adf_p_value_threshold=0.05,
    volume_quantile_threshold=0.95,
    volatility_window=20,
    liquidity_window=50,
):
    """
    Compute Smart Money Concepts (SMC) from candlestick data.

    Parameters:
    - candles (pd.DataFrame): DataFrame containing columns 'open', 'high', 'low', 'close', and 'volume'.
    - fvg_zscore_threshold (float): Z-score threshold for identifying Fair Value Gaps.
    - swing_length (int): Window length for calculating Swing Highs and Lows.
    - adf_p_value_threshold (float): P-value threshold for the ADF test in BOS calculation.
    - volume_quantile_threshold (float): Quantile threshold for identifying high-volume periods in OB calculation.
    - volatility_window (int): Window length for calculating volatility.
    - liquidity_window (int): Window length for calculating liquidity.

    Returns:
    - pd.DataFrame: DataFrame with additional columns representing the computed SMC concepts.
    """

    print("=== Computing Advanced SMC ===")

    # Copy the original DataFrame to avoid modifying it
    candles_copy = candles.copy()

    # Ensure the index is a DatetimeIndex
    if not isinstance(candles_copy.index, pd.DatetimeIndex):
        candles_copy.index = pd.to_datetime(candles_copy.index)
        print("Converted index to DatetimeIndex")

    # Ensure no NaN values in the primary columns before computation
    required_columns = ["open", "high", "low", "close", "volume"]
    for col in required_columns:
        if col not in candles_copy.columns:
            raise ValueError(f"Missing required column: {col}")
        if candles_copy[col].isnull().any():
            print(f"Filling NaN values in column: {col}")
            candles_copy[col].ffill(inplace=True)
            candles_copy[col].bfill(inplace=True)

    # Fair Value Gap (FVG) calculation using z-scores
    candles_copy["gap"] = candles_copy["close"].diff()
    candles_copy["gap_z"] = np.abs(stats.zscore(candles_copy["gap"].fillna(0)))
    candles_copy["FVG"] = np.where(
        candles_copy["gap_z"] > fvg_zscore_threshold, 1, np.nan
    )
    candles_copy["FVG_Top"] = candles_copy.apply(
        lambda row: row["high"] if row["FVG"] == 1 else None, axis=1
    )
    candles_copy["FVG_Bottom"] = candles_copy.apply(
        lambda row: row["low"] if row["FVG"] == 1 else None, axis=1
    )
    candles_copy["FVG"] = candles_copy["FVG"].fillna(0)
    num_fvg = candles_copy["FVG"].sum()
    print(f"Number of Fair Value Gaps (FVG) found: {num_fvg}")

    # Swing Highs and Lows calculation using local maxima/minima with a statistical filter
    candles_copy["Swing_High"] = (
        candles_copy["high"]
        == candles_copy["high"].rolling(window=swing_length, center=True).max()
    ).astype(int)
    candles_copy["Swing_Low"] = (
        candles_copy["low"]
        == candles_copy["low"].rolling(window=swing_length, center=True).min()
    ).astype(int)

    print("Intermediate Swing Highs:")
    print(candles_copy[["high", "Swing_High"]].dropna().head(10))

    print("Intermediate Swing Lows:")
    print(candles_copy[["low", "Swing_Low"]].dropna().head(10))

    candles_copy["Swing_High"] = candles_copy["Swing_High"].where(
        (candles_copy["Swing_High"] == 1)
        & (
            candles_copy["high"]
            > candles_copy["high"].mean() + candles_copy["high"].std()
        )
    )
    candles_copy["Swing_Low"] = candles_copy["Swing_Low"].where(
        (candles_copy["Swing_Low"] == 1)
        & (candles_copy["low"] < candles_copy["low"].mean() - candles_copy["low"].std())
    )

    print("Filtered Swing Highs:")
    print(candles_copy[["high", "Swing_High"]].dropna().head(10))

    print("Filtered Swing Lows:")
    print(candles_copy[["low", "Swing_Low"]].dropna().head(10))

    candles_copy["Swings"] = candles_copy["Swing_High"].replace(
        {0: np.nan}
    ) - candles_copy["Swing_Low"].replace({0: np.nan})
    candles_copy["Swings_Level"] = candles_copy.apply(
        lambda row: (
            row["high"]
            if row["Swing_High"] == 1
            else (row["low"] if row["Swing_Low"] == 1 else None)
        ),
        axis=1,
    )

    num_swing_highs = candles_copy["Swing_High"].sum()
    num_swing_lows = candles_copy["Swing_Low"].sum()
    print(f"Number of Swing Highs found: {num_swing_highs}")
    print(f"Number of Swing Lows found: {num_swing_lows}")
    print(
        candles_copy[["Swing_High", "Swing_Low", "Swings", "Swings_Level"]]
        .dropna()
        .head(10)
    )

    # Break of Structure (BOS) calculation using ADF test
    min_sample_size = 35  # Define a minimum sample size for ADF test

    def structural_break_test(series):
        if len(series) < min_sample_size:
            return False
        try:
            adf_stat, p_value, _, _, _, _ = adfuller(series.dropna())
            return p_value < adf_p_value_threshold
        except (ValueError, OverflowError, ZeroDivisionError) as e:
            print(f"ADF test error: {e}")
            return False

    candles_copy["BOS"] = 0
    for idx in range(min_sample_size, len(candles_copy)):
        if structural_break_test(candles_copy["close"].iloc[: idx + 1]):
            if candles_copy["close"].iloc[idx] > candles_copy["close"].iloc[idx - 1]:
                candles_copy.loc[candles_copy.index[idx], "BOS"] = 1
            else:
                candles_copy.loc[candles_copy.index[idx], "BOS"] = -1

    num_bos = candles_copy["BOS"].abs().sum()
    print(f"Number of Break of Structures (BOS) found: {num_bos}")
    print(candles_copy[["BOS"]].dropna().head(10))

    # Order Blocks (OB) calculation using clustering
    volume_threshold = candles_copy["volume"].quantile(volume_quantile_threshold)
    candles_copy["OB"] = 0
    high_volume_indices = candles_copy[candles_copy["volume"] > volume_threshold].index
    if len(high_volume_indices) > 0:
        clustering = DBSCAN(eps=1.5, min_samples=5).fit(
            candles_copy.loc[high_volume_indices, ["volume"]]
        )
        candles_copy.loc[high_volume_indices, "OB"] = np.where(
            clustering.labels_ != -1, clustering.labels_ + 1, 0
        )  # Ensure only valid clusters are labeled

    num_ob = candles_copy["OB"].max()
    print(f"Number of Order Blocks (OB) found: {num_ob}")

    # Liquidity calculation using volatility clustering
    candles_copy["returns"] = candles_copy["close"].pct_change(fill_method=None)
    candles_copy["volatility"] = (
        candles_copy["returns"].rolling(window=volatility_window).std()
    )
    average_volatility = candles_copy["volatility"].mean()
    candles_copy["volatility_zscore"] = (
        candles_copy["volatility"] - average_volatility
    ) / candles_copy["volatility"].std()

    # Set more stringent thresholds for identifying low and high volatility periods
    low_volatility_threshold = (
        -1.3
    )  # Adjust this value to make the threshold more strict
    high_volatility_threshold = (
        2.6  # Adjust this value to make the threshold more strict
    )

    candles_copy["Liquidity"] = candles_copy["volatility_zscore"].apply(
        lambda x: (
            1
            if x < low_volatility_threshold
            else (-1 if x > high_volatility_threshold else 0)
        )
    )

    num_liquidity_up = (candles_copy["Liquidity"] == 1).sum()
    num_liquidity_down = (candles_copy["Liquidity"] == -1).sum()
    print(f"Number of Up Liquidity periods found: {num_liquidity_up}")
    print(f"Number of Down Liquidity periods found: {num_liquidity_down}")
    print(candles_copy["Liquidity"].head())

    # Ensure no NaN values after all computations
    candles_copy.ffill(inplace=True)
    candles_copy.bfill(inplace=True)

    # Ensure the index is a DatetimeIndex
    if not isinstance(candles_copy.index, pd.DatetimeIndex):
        candles_copy.index = pd.to_datetime(candles_copy.index)

    # Drop rows where the index year is 1970
    candles_copy = candles_copy[candles_copy.index.year != 1970]

    # Drop rows where any of the required columns are NaN
    candles_copy = candles_copy.dropna(subset=["open", "high", "low", "close"])

    print("=== SMC Computation Completed ===")
    return candles_copy


def compute_smc_bis(candles):
    print("=== Computing SMC ===")

    # Data validation and preprocessing
    required_columns = ["open", "close", "high", "low", "volume"]
    for col in required_columns:
        assert col in candles.columns, f"Candles data is missing required column: {col}"

    # Initialize additional columns with NaNs
    for col in [
        "FVG_bis",
        "FVG_Top_bis",
        "FVG_Bottom_bis",
        "FVG_MitigatedIndex",
        "Swings_bis",
        "Swings_Level",
        "BOS_bis",
        "CHOCH",
        "BOS_Level",
        "BOS_BrokenIndex",
        "OB_bis",
        "OB_Top_bis",
        "OB_Bottom_bis",
        "OB_Volume",
        "OB_Percentage",
        "Liquidity_bis",
        "Liquidity_Level",
        "Liquidity_End",
        "Liquidity_Swept",
    ]:
        candles[col] = np.nan

    # Compute Fair Value Gaps (FVG)
    print("Input data for FVG:")
    print(candles.head())
    fvg = smc.fvg(candles, join_consecutive=False)
    if not fvg.empty:
        print(f"FVG: {fvg.describe()}")
        candles["FVG_bis"] = fvg["FVG"]
        candles["FVG_Top_bis"] = fvg["Top"]
        candles["FVG_Bottom_bis"] = fvg["Bottom"]
        candles["FVG_MitigatedIndex"] = fvg["MitigatedIndex"]
    else:
        print("FVG: No data found")

    # Compute Swing Highs and Lows
    print("Input data for Swings:")
    print(candles.head())
    swings = smc.swing_highs_lows(candles, swing_length=50)
    if not swings.empty:
        print(f"Swings: {swings.describe()}")
        candles["Swings_bis"] = swings["HighLow"]
        candles["Swings_Level"] = swings["Level"]
    else:
        print("Swings: No data found")

    # Compute Break of Structure (BOS) and Change of Character (CHOCH)
    if not swings.empty:
        print("Input data for BOS and CHOCH:")
        print(candles.head())
        bos_choch = smc.bos_choch(candles, swings, close_break=True)
        if not bos_choch.empty:
            print(f"BOS and CHOCH: {bos_choch.describe()}")
            candles["BOS_bis"] = bos_choch["BOS"]
            candles["CHOCH"] = bos_choch["CHOCH"]
            candles["BOS_Level"] = bos_choch["Level"]
            candles["BOS_BrokenIndex"] = bos_choch["BrokenIndex"]
        else:
            print("BOS and CHOCH: No data found")
    else:
        print("Swings data required for BOS and CHOCH computation is missing")

    # Compute Order Blocks (OB)
    if not swings.empty:
        print("Input data for Order Blocks:")
        print(candles.head())
        ob = smc.ob(candles, swings, close_mitigation=False)
        if not ob.empty:
            print(f"Order Blocks: {ob.describe()}")
            candles["OB_bis"] = ob["OB"]
            candles["OB_Top_bis"] = ob["Top"]
            candles["OB_Bottom_bis"] = ob["Bottom"]
            candles["OB_Volume"] = ob["OBVolume"]
            candles["OB_Percentage"] = ob["Percentage"]
        else:
            print("Order Blocks: No data found")
    else:
        print("Swings data required for Order Blocks computation is missing")

    # Compute Liquidity
    if not swings.empty:
        print("Input data for Liquidity:")
        print(candles.head())
        liquidity = smc.liquidity(candles, swings, range_percent=0.01)
        if not liquidity.empty:
            print(f"Liquidity: {liquidity.describe()}")
            candles["Liquidity_bis"] = liquidity["Liquidity"]
            candles["Liquidity_Level"] = liquidity["Level"]
            candles["Liquidity_End"] = liquidity["End"]
            candles["Liquidity_Swept"] = liquidity["Swept"]
        else:
            print("Liquidity: No data found")
    else:
        print("Swings data required for Liquidity computation is missing")

    # Post-processing and filtering
    candles = replace_nans_with_zero(candles)

    print("=== SMC Computation Completed ===")
    return candles


def replace_nans_with_zero(candles):
    # Replace NaNs with 0
    columns_to_replace = [
        "FVG_bis",
        "FVG_Top_bis",
        "FVG_Bottom_bis",
        "FVG_MitigatedIndex",
        "Swings_bis",
        "Swings_Level",
        "BOS_bis",
        "CHOCH",
        "BOS_Level",
        "BOS_BrokenIndex",
        "OB_bis",
        "OB_Top_bis",
        "OB_Bottom_bis",
        "OB_Volume",
        "OB_Percentage",
        "Liquidity_bis",
        "Liquidity_Level",
        "Liquidity_End",
        "Liquidity_Swept",
    ]
    candles[columns_to_replace] = candles[columns_to_replace].fillna(0)
    return candles


# Example usage (assuming you have a DataFrame `candles` with the necessary columns):
# candles = pd.read_csv('path_to_your_data.csv', index_col=0, parse_dates=True)
# computed_candles = compute_smc(candles)
# print(computed_candles.head())
