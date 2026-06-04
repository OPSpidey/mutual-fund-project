import pandas as pd
from pathlib import Path

raw_folder = Path("data/raw")

csv_files = list(raw_folder.glob("*.csv"))

print(f"Found {len(csv_files)} CSV files")

for file in csv_files:
    print("\n" + "=" * 60)
    print("FILE:", file.name)

    df = pd.read_csv(file)

    print("Shape:", df.shape)
    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())