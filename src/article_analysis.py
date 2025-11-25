from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def compute_headline_length(df):
    df['headline_length'] = df['headline'].astype(str).apply(len)
    return df

def publisher_stats(df):
    counts = df['publisher'].value_counts()
    mean_length = df.groupby('publisher')['headline_length'].mean().sort_values(ascending=False)
    return counts, mean_length

def daily_hourly_counts(df):
    df['date_only'] = df['date'].dt.date
    daily_counts = df['date_only'].value_counts().sort_index()
    df['hour'] = df['date'].dt.hour
    hourly_counts = df['hour'].value_counts().sort_index()
    return daily_counts, hourly_counts

def extract_keywords(df, max_features=30):
    """
    Extract top keywords from headlines using CountVectorizer.

    Returns:
        vectorizer: CountVectorizer object
        X: document-term matrix
        keywords: array of feature names
    """
    df['headline'] = df['headline'].astype(str)
    vectorizer = CountVectorizer(stop_words='english', max_features=max_features)
    X = vectorizer.fit_transform(df['headline'])
    keywords = vectorizer.get_feature_names_out()
    return vectorizer, X, keywords

def run_lda(X, feature_names, n_topics=5):
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda.fit(X)
    topics = {}
    for i, topic in enumerate(lda.components_):
        topics[i+1] = [feature_names[j] for j in topic.argsort()[-10:]]
    return topics
