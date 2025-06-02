{{
    config(materialized='table', schema='reporting_dataset')
}}
SELECT 
    DATE_TRUNC(order_date, DAY) AS day,
    round(sum(order_value),2) AS total_amount,
    count(DISTINCT order_id) AS total_orders,
    sum(quantity) AS total_quantity_sold,
    round(sum(CASE WHEN product_id = "A101" THEN order_value END),2) AS product_A101_value,
    round(sum(CASE WHEN product_id = "B202" THEN order_value END),2) AS product_B202_value,
    round(sum(CASE WHEN product_id = "C303" THEN order_value END),2) AS product_C303_value,
    round(sum(CASE WHEN product_id = "D404" THEN order_value END),2) AS product_D404_value,
    sum(CASE WHEN product_id = "A101" THEN quantity END) AS product_A101_quantity,
    sum(CASE WHEN product_id = "B202" THEN quantity END) AS product_B202_quantity,
    sum(CASE WHEN product_id = "C303" THEN quantity END) AS product_C303_quantity,
    sum(CASE WHEN product_id = "D404" THEN quantity END) AS product_D404_quantity
FROM {{ref("stg_orders")}}
GROUP BY 1
order by 1