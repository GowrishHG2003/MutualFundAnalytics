import requests
import pandas as pd
import os

# AMFI Code for HDFC Top 100 Direct
AMFI_CODE = 125497

url = f"https://api.mfapi.in/mf/{AMFI_CODE}"

print("Fetching live NAV data...")

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    output_path = "data/raw/live_nav.csv"

    nav_df.to_csv(output_path, index=False)

    print("\nLive NAV downloaded successfully!")
    print(f"Saved to: {output_path}")
    print(nav_df.head())

else:
    print("Error:", response.status_code)