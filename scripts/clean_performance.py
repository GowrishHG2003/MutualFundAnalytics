import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Convert numeric columns
numeric_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing numeric values
df = df.dropna(subset=numeric_columns)

# Keep expense ratio between 0.1 and 2.5
df = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]

# Save cleaned dataset
df.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("✅ Scheme Performance cleaned successfully!")