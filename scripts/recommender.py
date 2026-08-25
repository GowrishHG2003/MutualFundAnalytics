"""Simple risk-based mutual fund recommender for the Bluestock capstone."""
from pathlib import Path
import pandas as pd

RISK_MAP = {
    "low": ["Low"],
    "moderate": ["Moderate"],
    "high": ["High"],
}

def recommend(risk_appetite, data_path=None, top_n=3):
    """Return top funds by Sharpe ratio within the requested risk grade.

    Parameters
    ----------
    risk_appetite : str
        One of Low, Moderate, or High.
    data_path : str or Path, optional
        Path to 07_scheme_performance_clean.csv. Defaults to the repository
        data/processed location relative to this file.
    top_n : int
        Number of recommendations.
    """
    key = str(risk_appetite).strip().lower()
    if key not in RISK_MAP:
        raise ValueError("risk_appetite must be Low, Moderate, or High")

    if data_path is None:
        candidates = [
            Path(__file__).resolve().parent / "data" / "processed" / "07_scheme_performance_clean.csv",
            Path(__file__).resolve().parent / ".." / "data" / "processed" / "07_scheme_performance_clean.csv",
        ]
        data_path = next((p for p in candidates if p.exists()), candidates[0])

    df = pd.read_csv(data_path)
    result = (df[df["risk_grade"].isin(RISK_MAP[key])]
              .sort_values(["sharpe_ratio", "return_3yr_pct"], ascending=False)
              .head(top_n)
              [["amfi_code", "scheme_name", "risk_grade", "sharpe_ratio", "return_3yr_pct", "expense_ratio_pct"]]
              .reset_index(drop=True))
    return result

if __name__ == "__main__":
    for appetite in ["Low", "Moderate", "High"]:
        print(f"\n{appetite} risk appetite")
        print(recommend(appetite).to_string(index=False))
