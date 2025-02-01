-- Query to analyze total sales by product
SELECT
    product_id,
    SUM(total_sales) AS total_sales
FROM
    sales_summary
GROUP BY
    product_id
ORDER BY
    total_sales DESC;