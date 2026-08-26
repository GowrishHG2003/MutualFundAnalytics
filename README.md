# Bluestock Mutual Fund Analytics Capstone

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![SQL](https://img.shields.io/badge/SQL-SQLite-003B57?logo=sqlite)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly)
![Status](https://img.shields.io/badge/Status-Completed-success)

## Overview

This repository contains an end-to-end Mutual Fund Analytics Capstone Project completed as part of the Bluestock Fintech project.

The project builds a complete analytics pipeline for mutual-fund data, starting with raw CSV ingestion and live NAV retrieval, followed by data cleaning, SQLite database design, exploratory analysis, fund-performance measurement, dashboard development, advanced risk analytics, investor analysis, reporting, and final presentation.

The objective is to transform raw mutual-fund data into a reproducible analytics solution that can answer questions about:

- Fund and AMC-level AUM
- NAV and return trends
- SIP inflows and investor behaviour
- Fund performance and risk-adjusted returns
- Benchmark-relative performance
- Portfolio concentration and risk
- Investor cohorts and SIP continuity
- Fund recommendations based on risk appetite
- Interactive management-level dashboard insights

---

## Project Objectives

The project covers the following major objectives:

1. Build a reproducible ETL/data-ingestion pipeline.
2. Inspect and validate all supplied CSV datasets.
3. Retrieve live NAV data for selected mutual-fund schemes.
4. Validate AMFI scheme codes against NAV history.
5. Clean and standardise raw data.
6. Design a relational SQLite/star-schema database.
7. Perform exploratory data analysis across funds, investors and categories.
8. Calculate return, CAGR, Sharpe, Sortino, Alpha, Beta and drawdown metrics.
9. Compare funds against Nifty 50 and Nifty 100 benchmarks.
10. Develop an interactive Power BI/Tableau-style dashboard.
11. Perform advanced VaR, CVaR, rolling Sharpe, cohort, SIP continuity and concentration analysis.
12. Produce a final report and presentation suitable for project evaluation.

---

# 1. End-to-End Workflow

```text
Raw CSV Data
     │
     ▼
Data Ingestion & Validation
     │
     ├── NAV API / mfapi.in
     │
     ▼
Data Cleaning & Standardisation
     │
     ▼
SQLite Database
     │
     ├── SQL Queries
     ├── EDA
     ├── Performance Analytics
     └── Advanced Risk Analytics
     │
     ▼
Power BI / Tableau Dashboard
     │
     ▼
Final Report + Presentation
```

---

# 2. Project Phases

## Phase 1 — Project Setup & Data Ingestion

The initial stage established the project structure and reproducible data-ingestion workflow.

### Completed work

- Created the project directory structure.
- Initialised Git and connected the project to GitHub.
- Installed required Python dependencies.
- Created `requirements.txt`.
- Loaded all 10 provided CSV datasets using Pandas.
- Inspected:
  - shape
  - data types
  - first records
  - anomalies
- Implemented live NAV retrieval using the MFAPI endpoint.
- Fetched NAV data for five key schemes:
  - SBI Bluechip — `119551`
  - ICICI Bluechip — `120503`
  - Nippon Large Cap — `118632`
  - Axis Bluechip — `119092`
  - Kotak Bluechip — `120841`
- Saved API responses as raw CSV data.
- Explored the fund master.
- Identified unique fund houses, categories, sub-categories and risk grades.
- Validated AMFI scheme codes by checking that codes in `fund_master` exist in `nav_history`.
- Created a short data-quality summary.

### Main deliverables

```text
scripts/etl_pipeline.py
scripts/live_nav_fetch.py
requirements.txt
```

---

# 3. Data Cleaning & SQLite Database Design

The second phase converted raw data into analysis-ready datasets and a relational SQLite database.

## Cleaning performed

### `nav_history.csv`

- Parsed date fields into datetime.
- Sorted records by `amfi_code` and date.
- Forward-filled missing NAV values for weekends/holidays where appropriate.
- Removed duplicate records.
- Validated that NAV values are greater than zero.

### `investor_transactions.csv`

- Standardised transaction types:
  - SIP
  - Lumpsum
  - Redemption
- Validated transaction amounts.
- Standardised date formats.
- Checked KYC-status enum values.

### `scheme_performance.csv`

- Validated numerical return fields.
- Flagged anomalous values.
- Checked expense-ratio values against the expected range of approximately `0.1%–2.5%`.

## SQLite star schema

The database was designed around dimensions and fact tables:

```text
dim_fund
dim_date

fact_nav
fact_transactions
fact_performance
fact_aum
```

Primary keys and foreign keys were defined to maintain relational integrity.

Cleaned datasets were loaded into SQLite using SQLAlchemy/Pandas, and row counts were checked against the source CSV files.

### SQL analysis

The project includes analytical SQL covering:

- Top 5 funds by AUM
- Average NAV by month
- SIP year-over-year growth
- Transactions by state
- Funds with expense ratio below 1%
- Additional business-oriented fund and investor queries

### Data dictionary

A data dictionary was created documenting:

- Column names
- Data types
- Business definitions
- Source references

### Main deliverables

```text
data/processed/
data/db/bluestock_mf.db
sql/schema.sql
sql/queries.sql
data_dictionary.md
```

---

# 4. Exploratory Data Analysis

EDA was performed across NAV, AUM, SIP, investor, geographic, folio and portfolio data.

## Analysis and visualisations

### NAV Trend Analysis

- Daily NAV trends for all 40 schemes.
- Historical analysis covering 2022–2026.
- Identification of the 2023 bull run.
- Identification of the 2024 market correction.
- Interactive Plotly visualisation.

### AUM Growth

- Year-wise grouped AUM comparison by fund house.
- AMC-level comparison.
- SBI dominance was highlighted according to the project specification.

### SIP Inflow Analysis

- Monthly SIP inflow time series from January 2022 to December 2025.
- Annotation of the December 2025 all-time high of approximately ₹31,002 Cr.

### Category Inflow Heatmap

- Month on the X-axis.
- Fund category on the Y-axis.
- Net inflow represented through colour intensity.

### Investor Demographics

- Age-group distribution.
- SIP amount by age group.
- Investor demographic comparisons.

### Geographic Distribution

- SIP amount by state.
- Tier-2 vs Tier-3 city distribution.
- Geographic investor behaviour analysis.

### Folio Growth

- Folio count growth from approximately 13.26 Cr in January 2022 to 26.12 Cr in December 2025.
- Key milestones were highlighted.

### NAV Return Correlation

- Pairwise correlation of daily returns for 10 selected funds.
- Correlation heatmap.

### Sector Allocation

- Sector weights aggregated from portfolio holdings.
- Sector concentration analysis across equity funds.

### EDA findings

Ten key findings were documented in the EDA notebook using Markdown cells, with each insight supported by a corresponding visualisation.

### Main deliverables

```text
notebooks/03_eda_analysis.ipynb
```

The EDA stage contains 15+ analytical charts and exported PNG visualisations for reporting.

---

# 5. Fund Performance Analytics

The performance-analysis stage evaluates the return and risk characteristics of all 40 schemes.

## Daily returns

Daily return is calculated as:

```text
daily_return = NAV_t / NAV_(t-1) - 1
```

The return distributions were checked for reasonable behaviour and anomalies.

## CAGR

Compound annual growth rates were calculated for:

- 3-year performance
- 5-year performance

Formula:

```text
CAGR = (Ending NAV / Beginning NAV)^(1 / n) - 1
```

The calculation uses the appropriate annualisation period for the analysis.

## Sharpe Ratio

The Sharpe Ratio was calculated as:

```text
Sharpe = (Rp - Rf) / Std(Rp) × √252
```

where:

- `Rp` = fund return
- `Rf` = annualised risk-free rate proxy
- `Std(Rp)` = standard deviation of returns
- `252` = trading days per year

The project uses 6.5% as the RBI repo-rate proxy specified in the task.

All 40 funds were ranked using risk-adjusted performance.

## Sortino Ratio

The Sortino Ratio follows the same basic structure as Sharpe, but the denominator uses only downside volatility from negative-return days.

## Alpha and Beta

Fund returns were regressed against Nifty 100 returns using `scipy.stats.linregress`.

```text
Alpha = regression intercept × 252
Beta  = regression slope
```

## Maximum Drawdown

Maximum drawdown was calculated as:

```text
Maximum Drawdown =
min(NAV / running_max(NAV) - 1)
```

This measures the largest peak-to-trough decline experienced by each fund.

## Fund Scorecard

A composite score from 0–100 was constructed using:

- 30% — 3-year return rank
- 25% — Sharpe rank
- 20% — Alpha rank
- 15% — Expense-ratio rank, inverse
- 10% — Maximum-drawdown rank, inverse

This produces a comparable fund scorecard combining return, risk and cost considerations.

## Benchmark comparison

The project compares the top-performing funds with:

- Nifty 50
- Nifty 100

Tracking error is calculated as:

```text
Tracking Error =
Std(Fund Return - Benchmark Return) × √252
```

### Main deliverables

```text
notebooks/04_performance_analytics.ipynb
fund_scorecard.csv
alpha_beta.csv
benchmark comparison chart PNG
```

---

# 6. Dashboard Development

An interactive dashboard was designed using Power BI/Tableau-style business intelligence requirements.

## Dashboard structure

### Page 1 — Industry Overview

KPI cards include:

- Total AUM
- SIP inflows
- Folios
- Number of schemes

Visualisations include:

- Industry AUM trend from 2022–2025
- AUM by AMC

### Page 2 — Fund Performance

Includes:

- Return vs risk/standard-deviation scatter plot.
- Bubble size based on AUM.
- Sortable fund scorecard.
- NAV versus benchmark comparison.

Slicers include:

- Fund house
- Category
- Plan

### Page 3 — Investor Analytics

Includes:

- Transaction amount by state.
- SIP/Lumpsum/Redemption split.
- Age-group vs average SIP amount.
- Monthly transaction volume.

Slicers include:

- State
- Age group
- City tier

### Page 4 — SIP & Market Trends

Includes:

- SIP inflow trend.
- Nifty 50 comparison.
- Category inflow heatmap.
- Top 5 categories by net inflow for FY25.

### Dashboard interactivity

- Drill-through from fund-level views to NAV details.
- Interactive slicers.
- Tooltips.
- Cross-filtering.
- Business-oriented KPI presentation.

### Dashboard exports

```text
dashboard/bluestock_mf.pbix
reports/Dashboard.pdf
4 page PNG screenshots
```

---

# 7. Advanced Analytics & Risk Metrics

The advanced-analysis phase extends the project beyond descriptive analytics into risk measurement and investor intelligence.

## Historical VaR

Historical Value at Risk at the 95% confidence level was calculated using the 5th percentile of the daily return distribution.

```text
VaR 95% = 5th percentile of daily returns
```

## CVaR

Conditional Value at Risk was calculated as the mean return of observations below the VaR threshold.

```text
CVaR = Mean(Returns | Return < VaR)
```

VaR and CVaR were calculated across all 40 schemes.

## Rolling 90-Day Sharpe

Rolling Sharpe was calculated using:

```text
Rolling Sharpe =
Rolling Mean Return / Rolling Std Return × √252
```

A rolling 90-day window was used to evaluate changes in risk-adjusted performance over time.

## Investor Cohort Analysis

Investors were grouped by their first transaction year.

For each cohort, the analysis includes:

- Average SIP amount.
- Total amount invested.
- Preferred funds.

This provides insight into how investor behaviour varies across acquisition cohorts.

## SIP Continuity Analysis

Investors with at least six SIP transactions were evaluated.

The analysis calculates:

- Average gap between SIP transaction dates.
- Investors with gaps greater than 35 days.

Investors exceeding this threshold are flagged as:

```text
at-risk
```

## Fund Recommendation Engine

A simple recommendation engine accepts risk appetite:

```text
Low
Moderate
High
```

It then returns the top three funds by Sharpe Ratio within the matching `risk_grade`.

Main implementation:

```text
scripts/recommender.py
```

## Sector HHI Concentration

Portfolio concentration was evaluated using the Herfindahl-Hirschman Index:

```text
HHI = Σ(weight_i²)
```

Higher HHI indicates greater sector concentration.

The metric was compared across equity funds.

## Advanced insights

Five key advanced insights were documented, including findings around:

- Highest VaR funds
- Investor cohort investment behaviour
- SIP continuity
- Fund risk profiles
- Portfolio concentration

### Main deliverables

```text
notebooks/05_advanced_analytics.ipynb
var_cvar_report.csv
scripts/recommender.py
rolling_sharpe_chart.png
```

---

# 8. Final Report & Presentation

The final documentation stage consolidates the complete project into professional deliverables.

## Final report

The report covers:

1. Executive summary
2. Data sources
3. ETL architecture
4. Data cleaning
5. EDA findings
6. Performance analysis
7. Dashboard screenshots
8. Risk and advanced analytics
9. Key findings
10. Limitations
11. Recommendations
12. Conclusion

Target length:

```text
15–20 pages
```

## Presentation

A 12-slide presentation was created covering:

1. Title
2. Problem and objective
3. Data sources
4. Architecture
5. EDA highlights
6. EDA highlights
7. Performance metrics
8. Performance metrics
9. Dashboard
10. Dashboard
11. Key findings
12. Thank you

### Main deliverables

```text
reports/Final_Report.pdf
reports/Presentation.pptx
```

---

# 9. Repository Structure

The repository follows the project structure specified in the evaluation rubric:

```text
bluestock_mf_capstone/
│
├── data/
│   ├── raw/
│   │   └── original downloaded files
│   │
│   ├── processed/
│   │   └── cleaned and merged CSV files
│   │
│   └── db/
│       └── bluestock_mf.db
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── compute_metrics.py
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── bluestock_mf.pbix
│
├── reports/
│   ├── Final_Report.pdf
│   └── Presentation.pptx
│
├── requirements.txt
├── data_dictionary.md
└── README.md
```

---

# 10. Technology Stack

| Area | Tools / Technologies |
|---|---|
| Programming | Python |
| Data manipulation | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn, Plotly |
| Statistical analysis | SciPy |
| Database | SQLite |
| Database connectivity | SQLAlchemy |
| API / NAV retrieval | Requests, MFAPI |
| Development | Jupyter Notebook |
| Business intelligence | Power BI / Tableau |
| Version control | Git & GitHub |
| Documentation | Markdown |
| Reporting | PDF / PowerPoint |

---

# 11. Installation

Clone the repository:

```bash
git clone https://github.com/GowrishHG2003
cd bluestock_mf_capstone
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 12. Running the Project

## Option 1 — Run notebooks sequentially

Run the notebooks in this order:

```text
01_data_ingestion.ipynb
        ↓
02_data_cleaning.ipynb
        ↓
03_eda_analysis.ipynb
        ↓
04_performance_analytics.ipynb
        ↓
05_advanced_analytics.ipynb
```

## Option 2 — Run the ETL pipeline

The project also includes a master pipeline script:

```bash
python scripts/etl_pipeline.py
```

The pipeline is intended to automate the major data-processing steps and reduce manual execution.

---

# 13. Data Quality & Validation

Several validation checks were implemented throughout the project.

### Data-level checks

- CSV shape inspection.
- Data-type validation.
- Duplicate detection.
- Missing-value checks.
- Date parsing.
- Positive NAV validation.
- Positive transaction-amount validation.
- Transaction-type standardisation.
- KYC enum validation.
- Expense-ratio anomaly checks.
- AMFI code validation.

### Database-level checks

- Primary-key validation.
- Foreign-key relationships.
- Source-to-database row-count comparison.
- Schema validation.
- SQL query testing.

### Analytics-level checks

- Return distribution inspection.
- Benchmark comparison.
- Drawdown validation.
- Risk-metric calculations.
- Consistency checks across fund-level outputs.

---

# 14. Important Project Rules Followed

The project was implemented with the following evaluation requirements in mind:

- Use `pathlib.Path` or `os.path.join` instead of hard-coded file paths.
- Handle weekends and holidays when working with NAV history.
- Annualise CAGR using the appropriate trading-period methodology rather than simple calendar-day assumptions.
- Include units explicitly when presenting AUM.
- Provide at least two interactive filters/slicers per dashboard page.
- Include benchmark comparisons.
- Keep raw and processed data separated.
- Avoid committing SQLite `.db` files when the repository rubric requires the database to be reproducible.
- Share `schema.sql` and pipeline code so the database can be recreated.
- Keep notebooks and Python scripts reproducible and documented.

---

# 15. Reproducibility

The project is designed to be reproducible from raw data.

The intended workflow is:

```text
Raw files
   ↓
ETL pipeline
   ↓
Cleaned datasets
   ↓
SQLite database
   ↓
SQL analysis
   ↓
EDA
   ↓
Performance metrics
   ↓
Advanced analytics
   ↓
Dashboard
   ↓
Final report
```

This separation makes it easier to:

- Re-run the project.
- Update NAV data.
- Replace or refresh source datasets.
- Validate intermediate outputs.
- Reproduce analytical results.
- Maintain the project in GitHub.

---

# 16. Key Analytical Areas

The project combines several levels of financial analytics.

### Descriptive Analytics

- AUM trends
- SIP trends
- Folio growth
- Investor demographics
- Geographic distribution
- Category inflows

### Diagnostic Analytics

- NAV trends
- Return correlations
- Benchmark comparison
- Fund-level risk/return analysis
- Sector concentration

### Risk Analytics

- Sharpe Ratio
- Sortino Ratio
- Maximum Drawdown
- Alpha
- Beta
- Tracking Error
- Historical VaR
- CVaR
- Rolling Sharpe
- HHI

### Prescriptive / Decision Analytics

- Composite fund scorecard
- Risk-based fund recommender
- Investor SIP continuity flagging
- Cohort analysis
- Portfolio concentration assessment

---

# 17. Evaluation Coverage

The implementation addresses the core project evaluation areas:

| Evaluation Area | Coverage |
|---|---|
| ETL pipeline | Completed |
| Data validation | Completed |
| SQLite database | Completed |
| SQL schema & queries | Completed |
| EDA | Completed |
| Performance metrics | Completed |
| Risk-adjusted metrics | Completed |
| Benchmark comparison | Completed |
| Dashboard | Completed |
| Advanced analytics | Completed |
| Recommendation engine | Completed |
| Final report | Completed |
| Presentation | Completed |
| Git/GitHub version control | Completed |

---

# 18. Future Enhancements

The project specification also identified optional bonus extensions that can be developed in future iterations:

- Automated weekday NAV ingestion using a scheduled job.
- Streamlit web application as an alternative dashboard.
- Monte Carlo NAV-growth projections with uncertainty bands.
- Markowitz Efficient Frontier portfolio optimisation.
- Automated HTML/email performance reporting.

These are considered potential extensions rather than core project deliverables.

---

# 19. Conclusion

The Bluestock Mutual Fund Analytics Capstone demonstrates a complete **data-to-decision analytics workflow** for the mutual-fund domain.

The project integrates:

```text
Data Engineering
      +
SQL & Database Design
      +
Exploratory Data Analysis
      +
Financial Performance Analytics
      +
Risk Analytics
      +
Business Intelligence
      +
Investor Analytics
      +
Reporting & Presentation
```

The final solution provides a reproducible framework for analysing mutual-fund performance, understanding investor behaviour, measuring portfolio risk, comparing funds with market benchmarks, and communicating actionable insights through an interactive dashboard and professional reports.

---

## Author

GOWRISH HG

Mutual Fund Analytics Capstone  
Bluestock Fintech

---

## Disclaimer

This project is intended for educational and analytical purposes only. The fund rankings, risk metrics and recommendation outputs are based on the supplied project datasets and defined analytical methodology. They should not be interpreted as financial advice or investment recommendations.
