-- 1
SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2
SELECT
AVG(nav)
FROM fact_nav;

-- 3
SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

-- 4
SELECT *
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5
SELECT
MAX(return_5yr_pct)
FROM fact_performance;

-- 6
SELECT
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 7
SELECT
AVG(amount_inr) AS avg_transaction_amount
FROM fact_transactions;

-- 8
SELECT
state,
SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC
LIMIT 5;

-- 9
SELECT
SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC;

-- 10
SELECT
COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY transaction_type
ORDER BY transaction_count DESC;