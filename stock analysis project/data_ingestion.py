import yfinance as yf
from database import get_connection

def fetch_stock_data(ticker, start, end):
    print(yf.Ticker(ticker).info['longName'])
    df = yf.download(ticker, start=start, end=end, auto_adjust=True)
    if isinstance(df.columns, type(df.columns)) and hasattr(df.columns, 'levels'):
        df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]
    df.reset_index(inplace=True)
    return df

def save_to_db(df, ticker):
    conn = get_connection()
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO stocks (ticker, date, open, high, low, close, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            ticker,
            str(row['Date'])[:10],
            float(row['Open']),
            float(row['High']),
            float(row['Low']),
            float(row['Close']),
            int(row['Volume'])
        ))
    conn.commit()
    conn.close()
