{{
    config(materialized = "table", schema = "reporting_dataset")
}}
SELECT
    product_id,
    count(order_id) AS order_count,
    round(sum(order_value),2) AS total_amount,
    round(AVG(quantity),2) AS avg_order_size,
FROM {{ref("stg_orders")}}
    GROUP BY 1