import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud
from matplotlib import colors
import numpy as np
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

def plot_keyword_analysis(keywords_matrix, keywords, top_n=20, save_path=None):
    """
    Plots a Bar Chart of top keywords and a WordCloud side-by-side.
    """
    # Calculate frequencies
    word_freq = np.asarray(keywords_matrix.sum(axis=0)).flatten()
    word_freq_dict = {keywords[i]: word_freq[i] for i in range(len(keywords))}
    sorted_word_freq = sorted(word_freq_dict.items(), key=lambda x: x[1], reverse=True)

    plt.figure(figsize=(15, 10))

    # 1. Top Keywords Bar Chart
    plt.subplot(2, 1, 1)
    words = [x[0] for x in sorted_word_freq[:top_n]]
    frequencies = [x[1] for x in sorted_word_freq[:top_n]]

    plt.barh(range(len(words)), frequencies, align='center')
    plt.yticks(range(len(words)), words)
    plt.xlabel('Frequency')
    plt.title(f'Top {top_n} Keywords in Headlines')
    plt.gca().invert_yaxis()

    # 2. Generate Wordcloud
    plt.subplot(2, 1, 2)
    colormap = colors.LinearSegmentedColormap.from_list('custom_cmap', ['#1f77b4', '#ff7f0e', '#2ca02c'])
    wordcloud = WordCloud(width=800, height=400, background_color='white', 
                          max_words=100, colormap=colormap, 
                          contour_width=1, contour_color='steelblue')
    wordcloud.generate_from_frequencies(word_freq_dict)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Wordcloud of Headline Keywords')

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Keyword analysis saved to {save_path}")
    plt.show()

def plot_lda_heatmap(topics, save_path=None):
    """
    Creates a binary heatmap indicating which words appear in which topic.
    """
    # Collect all unique words across all topics
    all_words = set()
    for words in topics.values():
        all_words.update(words)
    all_words = sorted(list(all_words))

    # Create a DataFrame for easy plotting
    # Rows = Topics, Cols = Words
    data = []
    topic_labels = []
    
    for topic_id, words in topics.items():
        row = [1 if word in words else 0 for word in all_words]
        data.append(row)
        topic_labels.append(f"Topic {topic_id}")

    df_heatmap = pd.DataFrame(data, columns=all_words, index=topic_labels)

    # Plot
    plt.figure(figsize=(18, 6))
    sns.set(font_scale=1.2)
    sns.heatmap(df_heatmap, cmap="YlGnBu", cbar=False, linewidths=.5)
    
    plt.title("LDA Topics (Words per Topic)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"LDA Heatmap saved to {save_path}")
    plt.show()