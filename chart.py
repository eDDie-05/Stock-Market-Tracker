import yfinance as yf
import matplotlib.pyplot as plt

def show_chart(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="6mo")

    plt.figure(figsize=(10,5))
    plt.plot(data.index, data["Close"])
    plt.title(f"{ticker} Price Chart")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()