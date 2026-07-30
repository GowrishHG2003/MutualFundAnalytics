import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///database/bluestock_mf.db")

# Load cleaned CSV files
nav = pd.read_csv("data/processed/02_nav_history_clean.csv")
transactions = pd.read_csv("data/processed/08_investor_transactions_clean.csv")
performance = pd.read_csv("data/processed/07_scheme_performance_clean.csv")

# Store them as tables
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("✅ SQLite Database created successfully!")
print("Database file: database/bluestock_mf.db")