-- Sample SQL query for RFM segmentation
WITH customer_orders AS (
  SELECT customer_id, 
         MAX(order_date) AS last_order,
         COUNT(order_id) AS frequency,
         SUM(order_amount) AS monetary
  FROM orders
  GROUP BY customer_id
)
SELECT customer_id,
       DATEDIFF(CURDATE(), last_order) AS recency,
       frequency,
       monetary
FROM customer_orders;
