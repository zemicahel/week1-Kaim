from textblob import TextBlob
import pandas as pd

def compute_sentiment(text: str) -> pd.Series:
    if not isinstance(text, str) or text.strip() == "":
        return pd.Series({"polarity": None, "subjectivity": None})
    tb = TextBlob(text)
    return pd.Series({"polarity": tb.sentiment.polarity, "subjectivity": tb.sentiment.subjectivity})

def aggregate_daily_sentiment(news: pd.DataFrame) -> pd.DataFrame:
    news['mapped_date'] = pd.to_datetime(news['mapped_date']).dt.date
    daily_sentiment = (
        news.groupby(['stock', 'mapped_date'])
            .agg(
                avg_polarity=('polarity', 'mean'),
                avg_subjectivity=('subjectivity', 'mean'),
                article_count=('headline', 'count')
            )
            .reset_index()
            .rename(columns={'mapped_date':'date'})
    )
    return daily_sentiment
