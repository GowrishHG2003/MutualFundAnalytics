# Advanced Analytics + Risk Metrics

This deliverable completes the Bluestock Mutual Fund Analytics capstone task.

## Required deliverables
- `Advanced_Analytics.ipynb` — complete implementation of all requested analytics.
- `outputs/var_cvar_report.csv` — historical 95% VaR and CVaR for all 40 schemes.
- `recommender.py` — simple risk-based top-3 Sharpe recommender for Low/Moderate/High.
- `outputs/rolling_sharpe_chart.png` — 90-day rolling annualized Sharpe chart for the 5 largest funds by AUM.

## Additional outputs
- `outputs/investor_cohort_analysis.csv`
- `outputs/sip_continuity_analysis.csv`
- `outputs/sector_hhi_analysis.csv`
- `outputs/advanced_insights.md`

## How to run
1. Keep the `data/` folder in the same project root as the notebook and `recommender.py`.
2. Open `Advanced_Analytics.ipynb` in Jupyter/VS Code/Colab.
3. Run all cells.
4. To test the recommender:

```python
from recommender import recommend
recommend('Low')
recommend('Moderate')
recommend('High')
```

## Definitions used
- Historical VaR: 5th percentile of daily NAV returns.
- Historical CVaR: mean daily return at or below the 5th-percentile VaR threshold.
- Rolling Sharpe: 90 observations, annualized with `sqrt(252)`.
- SIP at-risk: investor has at least one consecutive SIP gap greater than 35 days; only investors with 6+ SIP transactions are evaluated.
- Sector HHI: `sum(weight_fraction^2)` after aggregating holdings by sector. HHI < 0.15 = unconcentrated, 0.15–0.25 = moderately concentrated, > 0.25 = highly concentrated.
