import sqlite3

conn = sqlite3.connect("stocks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS watchlist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS portfolio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT,
    shares REAL,
    buy_price REAL
)
""")

conn.commit()