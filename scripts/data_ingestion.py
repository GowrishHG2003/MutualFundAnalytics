import os
import pandas as pd

DATA_FOLDER = "data/raw"

files = sorted([f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")])

print("=" * 80)
print("DATA INGESTION REPORT")
print("=" * 80)

for file in files:
    path = os.path.join(DATA_FOLDER, file)
    df = pd.read_csv(path)

    print(f"\nDataset: {file}")
    print("-" * 50)

    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:", df.duplicated().sum())

print("\nAll datasets loaded successfully.")