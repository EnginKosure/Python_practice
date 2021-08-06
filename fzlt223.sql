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

