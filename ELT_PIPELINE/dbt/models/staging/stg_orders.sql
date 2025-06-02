WITH orders AS (
    SELECT 
       order_id,
       customer_id,
       product_id,
       quantity,
       price,
       quantity * price AS order_value,
       order_date,
       current_timestamp() as load_time
    FROM
       {{source("staging", "raw_orders")}}
)
SELECT * from orders