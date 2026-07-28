import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

missing = fund_master[
    ~fund_master["amfi_code"].isin(nav_history["amfi_code"])
]

print("Missing AMFI Codes")
print("=" * 40)

if missing.empty:
    print("All AMFI Codes are valid.")
else:
    print(missing)