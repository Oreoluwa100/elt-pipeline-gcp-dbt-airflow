{{
  config(materialized='table', schema='reporting_dataset')
}}

WITH customer_grouping AS (
  SELECT
    customer_id,
    count(*) AS order_count,
    round(sum(order_value),2) AS lifetime_value,
    date_diff(max(order_date), min(order_date), day) AS customer_duration
  FROM {{ref('stg_orders') }}
  GROUP BY 1
)

SELECT
  customer_id,
  order_count,
  lifetime_value,
  CASE
    WHEN order_count = 1 THEN 'One-time'
    WHEN order_count BETWEEN 2 AND 5 THEN 'Repeat'
    ELSE 'Loyal'
  END AS customer_segment
FROM customer_grouping


