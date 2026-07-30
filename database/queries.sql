-- 1
SELECT COUNT(*) AS total_funds
FROM fact_performance;

-- 2
SELECT AVG(nav) AS average_nav
FROM fact_nav;

-- 3
SELECT transaction_type,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;

-- 4
SELECT state,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5
SELECT scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6
SELECT scheme_name,
aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 7
SELECT risk_grade,
COUNT(*) AS total
FROM fact_performance
GROUP BY risk_grade;

-- 8
SELECT gender,
AVG(amount_inr) AS avg_investment
FROM fact_transactions
GROUP BY gender;

-- 9
SELECT city_tier,
COUNT(*) AS investors
FROM fact_transactions
GROUP BY city_tier;

-- 10
SELECT strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;