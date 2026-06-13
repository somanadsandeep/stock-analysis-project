import pandas as pd

def add_features(df):
    df['Return'] = df['Close'].pct_change()
    df['MA_20'] = df['Close'].rolling(window=20).mean()
    df['Volatility'] = df['Return'].rolling(window=20).std()
    return df.dropna()
