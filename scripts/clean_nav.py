import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Remove rows where date is invalid
df = df.dropna(subset=["date"])

# Sort by AMFI code and date
df = df.sort_values(["amfi_code", "date"])

# Remove duplicate rows
df = df.drop_duplicates()

# Convert NAV to numeric
df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

# Forward-fill missing NAV values for each fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Keep only valid NAV values
df = df[df["nav"] > 0]

# Save cleaned data
df.to_csv("data/processed/02_nav_history_clean.csv", index=False)

print("Cleaned Shape:", df.shape)
print("✅ NAV History cleaned successfully!")