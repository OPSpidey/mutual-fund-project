from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

nav = pd.read_csv(
    "data/processed/02_nav_history_clean.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("NAV Loaded")


transactions = pd.read_csv(
    "data/processed/08_transactions_clean.csv"
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("fact_transactions loaded")


performance = pd.read_csv(
    "data/processed/07_performance_clean.csv"
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("fact_performance loaded")