
📈 Financial News Sentiment & Stock Prediction

![alt text](https://img.shields.io/badge/python-3.9+-blue.svg)


![alt text](https://img.shields.io/badge/License-MIT-yellow.svg)


![alt text](https://img.shields.io/badge/Status-Active%20Development-green)


![alt text](https://img.shields.io/badge/code%20style-black-000000.svg)

10 Academy: Artificial Intelligence Mastery - Week 1 Challenge
Unlocking market alpha through Natural Language Processing and Technical Analysis.

📖 Project Overview

This project bridges the gap between Financial Analytics (FA) and Machine Learning Engineering (MLE). It analyzes a massive corpus of financial news headlines to quantify sentiment and explores statistical correlations with stock market movements for major tech giants (AAPL, AMZN, GOOG, META, MSFT, NVDA).

The Core Hypothesis:
Does positive news sentiment reliably predict an uptick in stock prices, and can we identify specific keywords or topics that drive market volatility?

🚀 Key Features

Sentiment Analysis: NLP pipelines using TextBlob and NLTK to score headline polarity.

Topic Modeling: Latent Dirichlet Allocation (LDA) to discover hidden themes in financial news.

Technical Analysis: Calculation of RSI, MACD, and SMA using TA-Lib and PyNance.

Correlation Engine: Statistical mapping of sentiment scores against daily stock returns.

Modular Architecture: Clean, reusable Python scripts located in src/.

📂 Repository Structure
code
Code
download
content_copy
expand_less
├── .github/workflows/   # CI/CD pipelines (GitHub Actions)
├── data/                # Raw and processed datasets
│   ├── raw_analyst_ratings.csv
│   └── AAPL.csv
│   └── AMZN.csv
│   └── GOOG.csv
│   └── META.csv
│   └── MSFT.csv
│   └── NVDA.csv
├── notebooks/           # Interactive analysis (Jupyter)
│   ├── 01_data_preparation.ipynb
│   ├── 02_sentiment_analysis.ipynb
│   └── 03_correlation_analysis.ipynb
├── src/                 # Source code modules
│   ├── article_analysis.py    # NLP, keyword extraction, LDA
│   ├── data_processing.py     # Data cleaning & loading
│   ├── sentiment_analysis.py  # Polarity computation
│   ├── stock_analysis.py      # Technical indicators (RSI, MACD)
│   └── visualization.py       # Plotting utilities
├── tests/               # Unit tests
├── .gitignore
├── README.md
└── requirements.txt
🛠 Installation & Setup

Follow these steps to set up a reproducible environment.

1. Clone the Repository
code
Bash
download
content_copy
expand_less
git clone https://github.com/zemicahel/week1-Kaim.git
cd week1-Kaim
2. Virtual Environment

It is best practice to run this project in a virtual environment.

code
Bash
download
content_copy
expand_less
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
3. Install TA-Lib (Prerequisite)

This project relies on TA-Lib for financial indicators. This is a system-level dependency.

Linux/macOS:

code
Bash
download
content_copy
expand_less
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib/
./configure --prefix=/usr/local
make
sudo make install

Windows:
Please download the appropriate .whl file for your Python version from this unofficial repository and install via pip (e.g., pip install TA_Lib‑0.4.24‑cp39‑cp39‑win_amd64.whl).

4. Install Python Dependencies
code
Bash
download
content_copy
expand_less
pip install -r requirements.txt
📊 Workflow & Methodology

The project is executed in three distinct phases, mirroring the notebooks in the notebooks/ directory.

Phase 1: Data Engineering & EDA

Objective: Ingest raw news data and historical stock prices.

Tools: Pandas, Matplotlib.

Insights: Analyzed publication frequency (daily/hourly), publisher activity, and headline length distributions.

Phase 2: Sentiment & Topic Analysis

Objective: Convert text into numerical data.

Tools: TextBlob, Scikit-Learn (CountVectorizer, LDA).

Process:

Clean text (lowercase, stopword removal).

Compute Polarity scores (-1 to +1).

Extract Top Keywords and cluster headlines into Topics (e.g., "Earnings Reports", "FDA Approvals").

Phase 3: Quantitative Analysis & Correlation

Objective: Merge sentiment data with market data.

Tools: TA-Lib, PyNance, Seaborn.

Process:

Calculate Daily Returns (pct_change).

Compute Technical Indicators: SMA (Trend), RSI (Momentum), MACD (Trend Following).

Align data by date and calculate Pearson correlation coefficients.

📉 Visualizations & Results

(Note: Run the notebooks to generate interactive versions of these plots)

Analysis	Description
Headline Frequency	Time-series analysis showing spikes in news volume correlating with market events.
Sentiment Distribution	Histograms displaying the lean of news (Positive vs. Negative) per stock.
Stock Indicators	Charts overlaying SMA, RSI, and MACD on price data to identify buy/sell signals.
Correlation Heatmap	A matrix visualizing the statistical relationship between Sentiment Score and Daily Returns.
🔮 Future Work

Deep Learning: Implement LSTM or BERT models for more nuanced sentiment detection (beyond simple polarity).

Intraday Analysis: Move from daily aggregation to minute-level alignment to capture immediate market reactions.

Portfolio Strategy: Backtest a trading strategy that buys/sells based on the generated sentiment signals.

🤝 Contributing

Contributions are welcome! Please follow the standard Git workflow:

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License

Distributed under the MIT License. See LICENSE for more information.

📞 Contact

Zemicahel

![alt text](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)


![alt text](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)