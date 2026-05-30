import tkinter as tk
from tkinter import messagebox
import yfinance as yf

def get_stock():
    ticker = ticker_entry.get().upper()

    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")

        if data.empty:
            messagebox.showerror("Error", "Stock not found!")
            return

        current_price = data["Close"].iloc[-1]
        high = data["High"].iloc[-1]
        low = data["Low"].iloc[-1]

        result.config(
            text=f"""
Ticker: {ticker}

Current Price: ${current_price:.2f}
Day High: ${high:.2f}
Day Low: ${low:.2f}
"""
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Stock Market Tracker")
root.geometry("400x300")

title = tk.Label(root, text="Stock Market Tracker",
                 font=("Arial", 16, "bold"))
title.pack(pady=10)

ticker_entry = tk.Entry(root, font=("Arial", 14))
ticker_entry.pack(pady=10)

search_btn = tk.Button(root, text="Track Stock",
                       command=get_stock)
search_btn.pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 12))
result.pack(pady=20)

root.mainloop()