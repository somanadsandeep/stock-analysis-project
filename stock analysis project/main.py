from database import create_tables
from data_ingestion import fetch_stock_data, save_to_db
from preprocessing import add_features
from visualization import plot_trends, plot_correlation
from modeling import train_model

def run_pipeline(ticker="AAPL", start="2020-01-01", end="2026-01-01"):
    create_tables()
    df = fetch_stock_data(ticker, start, end)
    save_to_db(df, ticker)
    
    df = add_features(df)
    plot_trends(df, ticker)
    plot_correlation(df)
    
    model, predictions, mse = train_model(df)
    print(f"Model trained with MSE: {mse}")

if __name__ == "__main__":
    ticker = input("Enter the stock ticker name: ")
    start = input("Enter the start date in the format of yyyy-dd-mm: ")
    end = input("Enter the start date in the format of yyyy-dd-mm: ")
    run_pipeline()
