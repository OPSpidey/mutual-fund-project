"""
clean_transactions.py

Purpose:
Clean transactions dataset and prepare processed output.
"""
import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Fix dates
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Valid values
valid_txn = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

df = df[
    df["transaction_type"].isin(valid_txn)
]

# Amount validation
df = df[df["amount_inr"] > 0]

print(df["kyc_status"].value_counts())

df.to_csv(
    "data/processed/08_transactions_clean.csv",
    index=False
)
print(df.head())
print(df.shape)
print(df.info())
print("test")