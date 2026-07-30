import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Convert transaction date
df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")

# Remove invalid dates
df = df.dropna(subset=["transaction_date"])

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Standardize KYC status
df["kyc_status"] = (
    df["kyc_status"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Convert amount to numeric
df["amount_inr"] = pd.to_numeric(df["amount_inr"], errors="coerce")

# Keep only valid transaction amounts
df = df[df["amount_inr"] > 0]

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("✅ Investor Transactions cleaned successfully!")