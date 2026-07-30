Data Dictionary

 fact_nav

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Mutual fund AMFI code |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

 fact_transactions

| Column | Type | Description |
|--------|------|-------------|
| investor_id | TEXT | Investor ID |
| transaction_date | DATE | Date of transaction |
| amfi_code | INTEGER | Mutual fund code |
| transaction_type | TEXT | SIP / Redemption / Lumpsum |
| amount_inr | REAL | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | Tier of city |
| age_group | TEXT | Investor age group |
| gender | TEXT | Gender |
| annual_income_lakh | REAL | Annual income |
| payment_mode | TEXT | Payment method |
| kyc_status | TEXT | KYC verification status |

---

fact_performance

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Mutual fund code |
| scheme_name | TEXT | Scheme name |
| fund_house | TEXT | Asset Management Company |
| category | TEXT | Fund category |
| plan | TEXT | Growth/Regular/Direct |
| return_1yr_pct | REAL | 1-year return |
| return_3yr_pct | REAL | 3-year return |
| return_5yr_pct | REAL | 5-year return |
| benchmark_3yr_pct | REAL | Benchmark return |
| alpha | REAL | Alpha value |
| beta | REAL | Beta value |
| sharpe_ratio | REAL | Sharpe Ratio |
| sortino_ratio | REAL | Sortino Ratio |
| std_dev_ann_pct | REAL | Annual standard deviation |
| max_drawdown_pct | REAL | Maximum drawdown |
| aum_crore | REAL | Assets Under Management |
| expense_ratio_pct | REAL | Expense ratio |
| morningstar_rating | INTEGER | Morningstar rating |
| risk_grade | TEXT | Risk category |