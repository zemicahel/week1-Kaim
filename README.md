10 Academy: Artificial Intelligence Mastery - Week 1 Challenge: Predicting Price Moves with News Sentiment

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-green.svg)](requirements.txt)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub Actions CI](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME/actions/workflows/unittests.yml/badge.svg)](https://github.com/zemicahel/week1-Kaim/actions/workflows/unittests.yml)

Project Overview

This repository contains the solution for the 10 Academy Week 1 Challenge: "Predicting Price Moves with News Sentiment." The project aims to analyze a corpus of financial news data to discover correlations between news sentiment and stock market movements. This challenge refines skills in Data Engineering (DE), Financial Analytics (FA), and Machine Learning Engineering (MLE).

The core objectives are:
1.  Sentiment Analysis: Quan Establish statistical correlations between news sentiment and corresponding stock price movements, considering publication dates.
3.  Investment Strategies: Leverage insights from the analysis to suggest predictive investment strategies.

---

Current Progress: Interim Submission (Covering Task 1 & Task 2)

As of the interim submission deadline, this project has successfully completed:

Task 1: Git and GitHub & Exploratory Data Analysis (EDA) 
       Setup of a reproducible Python data science environment.
       Implementation of Git for version control with a clear branching strategy (`master`, `task-1`, `task-2`,`File Structure`).
       Comprehensive EDA on a dummy financial news dataset, identifying key trends in headline length, publisher activity, publication frequency, and common keywords.
Task 2: Quantitative Analysis using PyNance and TA-Lib 
       Loading and rigorous preparation of historical stock price data for 6 major tech stocks (AAPL, AMZN,GOOG, META, MSFT, NVDA) from CSV files.
       Application of standard technical indicators (Simple Moving Averages, Relative Strength Index, MACD) using the `TA-Lib` library.
       Demonstrative use of `PyNance` for broader financial metrics context.
       Visualization of stock price movements alongside calculated technical indicators.

---

Repository Structure

.
├── .vscode/    VS Code settings (e.g., for consistent formatting)
├── .github/
│ └── workflows/
│ ├── unittests.yml    GitHub Actions for Continuous Integration (CI)
├── data/ 
│ ├── AAPL.csv
│ ├── AMZN.GOOG.csv
│ ├── META.csv
│ ├── MSFT.csv
│ └── NVDA.csv
├── notebooks/    Jupyter notebooks for interactive development and analysis
│ └── task-1.ipynb 
│ └── task-2.ipynb
├── src/    Source code for modular functions
│ ├── init.py
├── scripts
├── tests/    Unit tests for functions in src/
│ ├── init.py
├── .gitignore    Specifies intentionally untracked files
├── requirements.txt    Lists project dependencies
├── README.md    This file

code
Code
download
content_copy
expand_less

Setup and Installation

To set up the project locally, follow these steps:

1. Clone the Repository:

    git clone https://github.com/zemicahel/week1-Kaim.git


2.  Create a Virtual Environment:
    It's recommended to use a virtual environment to manage dependencies.

    python -m venv venv
    source venv/bin/activate     On Windows: `venv\Scripts\activate`

3
    Install all required Python packages.  Note:  `TA-Lib` requires a system-level installation first.
         TA-Lib System Installation (Linux/macOS): 
        ```bash
        wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
        tar -xzf ta-lib-0.4.0-src.tar.gz
        cd ta-lib/
        ./configure --prefix=/usr/local
        make
        sudo make install
        cd ..
        rm -rf ta-lib ta-lib-0.4.0-src.tar.gz
        ```
          (For Windows, refer to the official TA-Lib-Python documentation for installation instructions: [TA-Lib Python](https://github.com/TA-Lib/ta-lib-python))  

          Python Package Installation: 
        ```bash
        pip install -r requirements.txt
        ```

4.   Data Setup: 
         Create a directory named `data/` in the project root.
         Place your individual stock CSV files (e.g., `AAPL.csv`, `AMZN.csv`,`GOOG.csv`, `META.csv`, `MSFT.csv`, `NVDA.csv`) into this `data/` directory. Ensure they have the headers `Date`, `Open`, `High`, `Low`, `Close`, `Volume`.

5.   Run Jupyter Notebook: 
    ```bash
    jupyter notebook
    ```
    Navigate to `notebooks/Week1_Challenge_Analysis.ipynb` to execute the code and view the analysis.

---

 Git Workflow (Task 1 Adherence)

The project adheres to a structured Git workflow:

      `master` branch:  Represents the stable, production-ready version of the code.
      `task-1` branch:  Dedicated to initial setup and Exploratory Data Analysis.
      `task-2` branch:  Dedicated to quantitative analysis, including data loading, preparation, and technical indicator calculation.
      Feature Branches:  For further development, new branches will be created from `main` for specific features or tasks.
      Pull Requests (PRs):  All work from feature/task branches is merged into `main` via PRs, facilitating code review and ensuring quality.
      Regular Commits:  Work is committed frequently with descriptive commit messages.

---

     Deliverables & Tasks Completed (Interim)

       Task 1: Git and GitHub & EDA

      Setup:  Reproducible Python environment with `requirements.txt` and `venv`.
      Version Control:  Established a GitHub repository, used branches (`task-1` and `task-2`), and maintained a consistent commit history.
      EDA: 
          Descriptive Statistics:  Analyzed headline lengths, publisher distribution, and temporal patterns of news publication (daily and hourly frequencies).
          Text Analysis:  Performed basic keyword extraction to identify prominent themes in financial news headlines.
          Visualizations:  Generated informative plots for news frequency and publisher contributions.

       Task 2: Quantitative Analysis using PyNance and TA-Lib

      Data Loading & Preparation: 
         Successfully loaded historical `Open`, `High`, `Low`, `Close`, `Volume` data for `AAPL`, `AMZN.GOOG`, `META`, `MSFT`, `NVDA` from CSV files.
         Implemented robust data cleaning, including date parsing, indexing, sorting, type conversion, and handling of missing values.
      Technical Indicators (TA-Lib): 
         Calculated  Simple Moving Averages (SMA)  (20-day and 50-day) for trend identification.
         Computed the  Relative Strength Index (RSI)  (14-day) to gauge overbought/oversold conditions.
         Derived  Moving Average Convergence Divergence (MACD)  (12, 26, 9) for momentum and trend-following signals.
      Financial Metrics (PyNance): 
         Acknowledged `PyNance`'s role in broader financial analysis and data fetching, demonstrating its potential for calculating general financial metrics like daily returns on the prepared stock data.
      Visualizations: 
         Created insightful plots showing stock close prices overlaid with SMAs, as well as separate charts for RSI and MACD, illustrating the impact and behavior of these indicators.

---

     Learning Objectives Addressed

By completing Task 1 and Task 2, the following learning objectives have been met:

     Configure a reproducible Python data-science environment with GitHub integration.
     Perform Exploratory Data Analysis (EDA) on text and time series data.
     Compute technical indicators (MA, RSI, MACD) using TA-Lib.
     Visualize data to understand the impact of different indicators on stock prices.

---

     Future Work (Task 3 and Final Submission)

      Date Alignment:  Precisely align news sentiment data with corresponding stock price movements.
      Sentiment Analysis:  Perform detailed sentiment analysis on news headlines using NLP libraries like `nltk` and `TextBlob`.
      Correlation Analysis:  Statistically measure the correlation between news sentiment scores and daily stock returns.
      Investment Strategies:  Develop and propose actionable investment strategies based on the identified correlations.
      Reporting:  Compile a comprehensive final report suitable for publication as a Medium Blog post.

---

     License


     Contact

For any questions or feedback, please reach out to:

      Your Name/GitHub Handle  ([GitHub Profile Link](https://github.com/zemicahel))

---