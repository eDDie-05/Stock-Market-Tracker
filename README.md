# Stock Market Tracker — Python

A desktop stock-lookup application built with Tkinter and yfinance. The main window accepts a ticker symbol and displays the latest available daily closing price, high and low returned by the data provider.

## Features
- Tkinter desktop interface
- Ticker-symbol lookup
- Daily price, high and low display
- Separate chart and portfolio-related helper modules in the repository

## Requirements
- Python 3.10 or newer
- Tkinter
- yfinance
- Matplotlib (for chart-related functionality)

## Setup
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell
.venv\\Scripts\\Activate.ps1
python -m pip install yfinance matplotlib
```

## Run the main application
```bash
python main.py
```

## Main files
- `main.py` — desktop ticker lookup
- `chart.py` — chart helper
- `database.py`, `portfolio.py`, `watchlist.py`, `export_portfolio.py`, `news_feed.py`, `crypto_tracking.py`, `refresh.py` — supporting modules

## Important notes
- Market data is supplied by an external provider and may be delayed, incomplete or unavailable.
- This is an educational information tool, not financial advice or a trading platform.
- Do not commit virtual environments, personal database files or API credentials. Review the existing `.venv` and database files before keeping the repository public.
