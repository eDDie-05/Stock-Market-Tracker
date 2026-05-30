import pandas as pd

def export_csv():
    df = pd.read_sql_query(
        "SELECT * FROM portfolio",
        conn
    )
    df.to_csv("portfolio.csv", index=False)