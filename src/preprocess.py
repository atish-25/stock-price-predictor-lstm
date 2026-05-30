import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def preprocess_data(csv_path):

    data = pd.read_csv(csv_path)

    close_prices = data["Close"].values

    scaler = MinMaxScaler(feature_range=(0, 1))

    scaled_data = scaler.fit_transform(
        close_prices.reshape(-1, 1)
    )

    return scaled_data, scaler