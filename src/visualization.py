import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_palette("viridis")
plt.style.use("seaborn-v0_8-darkgrid")

def plot_price_with_sma(df, sym):
    plt.figure(figsize=(12,6))
    plt.plot(df["Close"], label="Close Price")
    if "SMA_20" in df:
        plt.plot(df["SMA_20"], label="SMA 20")
    if "SMA_50" in df:
        plt.plot(df["SMA_50"], label="SMA 50")
    plt.title(f"{sym} – Close Price + SMAs")
    plt.legend()
    plt.show()

def plot_rsi(df, sym):
    if "RSI_14" not in df:
        return
    plt.figure(figsize=(12,4))
    plt.plot(df["RSI_14"])
    plt.axhline(70, linestyle='--')
    plt.axhline(30, linestyle='--')
    plt.title(f"{sym} – RSI (14)")
    plt.show()

def plot_macd(df, sym):
    if "MACD" not in df:
        return
    plt.figure(figsize=(12,5))
    plt.plot(df["MACD"], label="MACD")
    plt.plot(df["MACD_signal"], label="Signal")
    plt.bar(df.index, df["MACD_hist"], alpha=0.4)
    plt.title(f"{sym} – MACD")
    plt.legend()
    plt.show()

def plot_correlation_heatmap(dfs):
    close_prices = pd.DataFrame({sym: dfs[sym]["Close"] for sym in dfs})
    plt.figure(figsize=(10,6))
    sns.heatmap(close_prices.pct_change().corr(), annot=True, cmap="viridis")
    plt.title("Stock Returns Correlation Heatmap")
    plt.show()


def scatter_sentiment_vs_return(df: pd.DataFrame, sym: str):
    plt.figure(figsize=(8,5))
    plt.scatter(df['avg_polarity'], df['daily_return'], alpha=0.6)
    plt.title(f"{sym} Daily Return vs. News Sentiment")
    plt.xlabel("Average Daily Polarity")
    plt.ylabel("Daily Return")
    plt.axhline(0, color='gray', linestyle='--')
    plt.show()

def time_series_sentiment_vs_return(df: pd.DataFrame, sym: str):
    plt.figure(figsize=(12,4))
    plt.plot(df['date'], df['daily_return'], label='Daily Return')
    plt.plot(df['date'], df['avg_polarity'], label='Average Sentiment')
    plt.title(f"{sym} Daily Returns vs News Sentiment Over Time")
    plt.xlabel("Date")
    plt.legend()
    plt.show()
def plot_daily_counts(daily_counts):
    daily_counts.plot(kind='line', figsize=(12,5))
    plt.title("Articles Published Per Day")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.grid(True)
    plt.show()

def plot_hourly_counts(hourly_counts):
    hourly_counts.plot(kind='bar', figsize=(12,5))
    plt.title("Articles Published by Hour of Day")
    plt.xlabel("Hour")
    plt.ylabel("Count")
    plt.show()