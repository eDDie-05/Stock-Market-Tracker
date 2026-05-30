def calculate_pl(ticker, shares, buy_price):
    import yfinance as yf

    stock = yf.Ticker(ticker)
    current = stock.history(period="1d")["Close"].iloc[-1]

    profit = (current - buy_price) * shares
    return profit