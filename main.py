from src.download_data import download_stock_data
from src.preprocess import preprocess_data

data = download_stock_data('AAPL',"2015-01-01","2025-01-01")
print(data.head())
print(data.columns)

data.to_csv("data/AAPL.csv")

scaled_data, scaler = preprocess_data(
    "data/AAPL.csv"
)

print(scaled_data.shape)
print(scaled_data[:5])
print(data.columns)