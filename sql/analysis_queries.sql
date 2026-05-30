-- Analysis queries for Telco Customer Churn

-- Total customers
SELECT COUNT(*) AS total_customers FROM customers;

-- Churned customers
SELECT COUNT(*) AS churned_customers FROM customers WHERE churn = 'Yes';

-- Churn rate (percentage)
SELECT
  ROUND(100.0 * SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) / NULLIF(COUNT(*),0), 2) AS churn_rate_pct
FROM customers;

-- Revenue (total_charges) by payment method
SELECT payment_method, SUM(total_charges) AS total_revenue, COUNT(*) AS customers
FROM customers
GROUP BY payment_method
ORDER BY total_revenue DESC;

-- Contract analysis: counts and avg monthly charges
SELECT contract AS contract_type, COUNT(*) AS customer_count, ROUND(AVG(monthly_charges),2) AS avg_monthly_charges
FROM customers
GROUP BY contract
ORDER BY customer_count DESC;
