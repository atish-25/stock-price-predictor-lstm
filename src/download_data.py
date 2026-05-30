import yfinance as yf
def download_stock_data(ticker, start_date, end_date):
    
    stock = yf.download(ticker, start=start_date, end=end_date)
    return stock