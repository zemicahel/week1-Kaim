import os
import pandas as pd
import numpy as np

try:
    import talib as ta
except ImportError:
    ta = None

def load_stock_data(stock_data_dir, symbols, required_cols=None):
    """
    Load and preprocess stock CSVs into a dictionary of DataFrames.

    Args:
        stock_data_dir (str): path to stock CSV files
        symbols (list): list of stock symbols
        required_cols (list): columns that must exist in CSV

    Returns:
        dict: {symbol: DataFrame}
    """
    if required_cols is None:
        required_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
        
    dfs = {}
    for sym in symbols:
        fp = os.path.join(stock_data_dir, f"{sym}.csv")
        if not os.path.exists(fp):
            continue
        
        df = pd.read_csv(fp)
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df.set_index('Date', inplace=True)
        df = df.sort_index()
        
        if not all(c in df.columns for c in required_cols):
            continue
        
        df[required_cols] = df[required_cols].apply(pd.to_numeric, errors='coerce')
        df = df.ffill().bfill().dropna()
        dfs[sym] = df
    
    return dfs

def compute_technical_indicators(dfs):
    """
    Add SMA, RSI, MACD columns if TA-Lib is available.

    Args:
        dfs (dict): {symbol: DataFrame}

    Returns:
        dict: updated dfs
    """
    if ta is None:
        return dfs
    
    for sym, df in dfs.items():
        df["SMA_20"] = ta.SMA(df["Close"], timeperiod=20)
        df["SMA_50"] = ta.SMA(df["Close"], timeperiod=50)
        df["RSI_14"] = ta.RSI(df["Close"], timeperiod=14)
        
        macd, signal, hist = ta.MACD(df["Close"], fastperiod=12, slowperiod=26, signalperiod=9)
        df["MACD"] = macd
        df["MACD_signal"] = signal
        df["MACD_hist"] = hist
        
    return dfs

def compute_stock_metrics(dfs):
    """
    Compute daily returns, Sharpe ratio, max drawdown.

    Returns:
        dict: {symbol: {"daily_returns":..., "sharpe_ratio":..., "max_drawdown":...}}
    """
    metrics = {}
    for sym, df in dfs.items():
        close = df["Close"]
        daily_returns = close.pct_change().dropna()
        sharpe_ratio = (daily_returns.mean() / daily_returns.std()) * np.sqrt(252)
        cumulative = (1 + daily_returns).cumprod()
        drawdown = cumulative / cumulative.cummax() - 1
        max_drawdown = drawdown.min()
        metrics[sym] = {
            "daily_returns": daily_returns,
            "sharpe_ratio": sharpe_ratio,
            "max_drawdown": max_drawdown
        }
    return metrics


def compute_daily_returns(stock_data: dict) -> dict:
    stock_returns = {}
    for sym, df in stock_data.items():
        df = df.copy()
        df['date'] = df['Date'].dt.date
        df['daily_return'] = df['Close'].pct_change()
        stock_returns[sym] = df[['date','Close','daily_return']]
    return stock_returns

def merge_with_sentiment(stock_returns: dict, daily_sentiment: pd.DataFrame) -> dict:
    merged_data = {}
    for sym, df in stock_returns.items():
        sent_df = daily_sentiment[daily_sentiment['stock']==sym][['date','avg_polarity','article_count']]
        merged = pd.merge(df, sent_df, on='date', how='left')
        merged_data[sym] = merged
    return merged_data
