import os
import pandas as pd

def load_news(news_fp: str) -> pd.DataFrame:
    news = pd.read_csv(news_fp)
    news['date'] = pd.to_datetime(news['date'], errors='coerce')
    news = news.dropna(subset=['date'])
    
    if news['date'].dt.tz is None:
        news['date'] = news['date'].dt.tz_localize("UTC")
    
    news['news_date'] = news['date'].dt.tz_convert('UTC').dt.date
    return news

def load_stock_data(stock_data_dir: str, symbols: list) -> dict:
    stock_data = {}
    for sym in symbols:
        fp = os.path.join(stock_data_dir, f"{sym}.csv")
        if os.path.exists(fp):
            df = pd.read_csv(fp)
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            df = df.dropna(subset=['Date', 'Close'])
            df = df.sort_values('Date')
            stock_data[sym] = df
    return stock_data
