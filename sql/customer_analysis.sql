-- Query to analyze customer purchase behavior
SELECT
    customer_id,
    COUNT(*) AS total_purchases,
    SUM(total_sales) AS total_spent
FROM
    transactions
GROUP BY
    customer_id
ORDER BY
    total_spent DESC;