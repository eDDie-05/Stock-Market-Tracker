def refresh():
    update_prices()
    root.after(10000, refresh)