-- SELECT id, account_id, total_amt_usd
-- FROM orders
-- ORDER BY total_amt_usd DESC
-- LIMIT 5;

--SELECT num FROM UNNEST(GENERATE_ARRAY(2012,EXTRACT(YEAR FROM CURRENT_DATE())  )) AS num;
SELECT *
FROM accounts
WHERE name NOT LIKE 'C%' AND name NOT LIKE '%s' ;