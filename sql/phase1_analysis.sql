-- Phase 1 SQL analysis queries for Telco Customer Churn
-- Run these after importing the CSV into the `customers` table

-- 1) Total customers (expected 7043)
SELECT COUNT(*) AS total_customers FROM customers;

-- 2) Churn count
SELECT churn, COUNT(*) AS count
FROM customers
GROUP BY churn;

-- 3) Churn rate (percentage)
SELECT
  ROUND(
    100.0 * SUM(CASE WHEN churn='Yes' THEN 1 ELSE 0 END) / NULLIF(COUNT(*),0),
    2
  ) AS churn_rate_pct
FROM customers;

-- 4) Contract x Churn
SELECT contract, churn, COUNT(*) AS count
FROM customers
GROUP BY contract, churn
ORDER BY contract;

-- 5) Payment method x Churn
SELECT paymentmethod AS payment_method, churn, COUNT(*) AS count
FROM customers
GROUP BY paymentmethod, churn
ORDER BY payment_method;

-- 6) Quick revenue by payment method
SELECT paymentmethod AS payment_method, SUM(total_charges) AS total_revenue, COUNT(*) AS customers
FROM customers
GROUP BY paymentmethod
ORDER BY total_revenue DESC;

-- Note: adjust column names if your DB has different casing (e.g., "PaymentMethod").
