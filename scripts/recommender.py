"""
Simple Fund Recommender
"""

import pandas as pd

# Load performance data
performance = pd.read_csv("data/processed/07_performance_clean.csv")

risk = input("Risk Appetite (Low/Moderate/High): ").strip()

# Filter by risk category
filtered = performance[
    performance["risk_category"].str.lower() == risk.lower()
]

# Sort by Sharpe Ratio
top_funds = filtered.sort_values(
    by="sharpe_ratio",
    ascending=False
).head(3)

print("\nTop 3 Recommended Funds\n")
print(
    top_funds[
        [
            "scheme_name",
            "category",
            "sharpe_ratio",
            "return_5yr_pct"
        ]
    ]
)