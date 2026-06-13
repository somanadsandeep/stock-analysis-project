import matplotlib.pyplot as plt
import seaborn as sns

def plot_trends(df, ticker):
    plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.plot(df['Date'], df['MA_20'], label='20-day MA')
    plt.title(f"{ticker} Price Trend")
    plt.legend()
    plt.show()

def plot_correlation(df):
    corr = df[['Open','High','Low','Close','Volume']].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.show()
