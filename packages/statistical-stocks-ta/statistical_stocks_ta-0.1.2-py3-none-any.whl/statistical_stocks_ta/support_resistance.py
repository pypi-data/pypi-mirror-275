import numpy as np
from sklearn.linear_model import QuantileRegressor


def quantile_regression_support_resistance(candles, quantiles=[0.10, 0.90]):
    print("=== Starting quantile regression for support and resistance ===")
    x = np.arange(len(candles)).reshape(-1, 1)
    y = candles["close"].values

    for q in quantiles:
        model = QuantileRegressor(quantile=q).fit(x, y)
        pred = model.predict(x)
        key = "Support_Q" if q < 0.5 else "Resistance_Q"
        candles[key] = pred
    print("=== Quantile regression completed ===")
    return candles
