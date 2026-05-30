# Stock Tracker
A small Python project with a Tkinter stock tracker UI, a chart helper, and a dark-mode Tkinter demo.

## Prerequisites
- Python 3.10+ (tested with Python 3.12)
- `pip` and `venv`

## Setup
From the project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install yfinance matplotlib
```

If you are not using a virtual environment on Ubuntu/Debian, you may need:

```bash
python -m pip install --user --break-system-packages yfinance matplotlib
```

## Run the app
Launch the main stock tracker UI:

```bash
python main.py
```

## Use the chart helper
`chart.py` exposes a function `show_chart(ticker)`:

```bash
python -c "from chart import show_chart; show_chart('AAPL')"
```

## Dark mode demo
Run the dark-mode Tkinter demo script:

```bash
python .venv/dark_mode.py
```
