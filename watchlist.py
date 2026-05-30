def add_watchlist(ticker):
    cursor.execute(
        "INSERT OR IGNORE INTO watchlist (ticker) VALUES (?)",
        (ticker,)
    )
    conn.commit()