-- SELECT id, account_id, total_amt_usd
-- FROM orders
-- ORDER BY total_amt_usd DESC
-- LIMIT 5;

--SELECT num FROM UNNEST(GENERATE_ARRAY(2012,EXTRACT(YEAR FROM CURRENT_DATE())  )) AS num;
SELECT *
FROM accounts
WHERE name NOT LIKE 'C%' AND name NOT LIKE '%s'
;

SELECT a.primary_poc, w.channel, w.occurred_at
FROM web_events w
    JOIN accounts a
    ON w.account_id=a.id;

SELECT
    r.name AS reg_name, s.name as rep_name, a.name as ac_name
FROM sales_reps s
    JOIN region r
    ON s.region_id=r.id AND r.name='Midwest'
    JOIN accounts a
    ON s.id=a.sales_rep_id;


SELECT
    r.name as reg_name, s.name as rep_name, a.name as account_name
FROM region r
    JOIN sales_reps s
    ON r.id=s.region_id
    JOIN accounts a
    ON s.id=a.sales_rep_id AND s.name LIKE 'S%' AND r.name='Midwest'
ORDER BY a.name;

SELECT
    r.name region, a.name account, o.total_amt_usd/o.total unit_price
FROM sales_reps s
    JOIN region r
    ON s.region_id=r.id
    JOIN accounts a
    ON s.id=a.sales_rep_id
    JOIN orders o
    ON a.id=o.account_id
WHERE o.standard_qty>100
