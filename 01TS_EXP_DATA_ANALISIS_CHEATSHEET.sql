--BLOCK-1---
-- df.shape
-- SELECT  
--     count(distinct column_name) 
-- ,  (select  count(*) from  `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`)
-- FROM `geb-dwh-test.uat_geb_dwh_eu_act.INFORMATION_SCHEMA.COLUMNS`
-- WHERE table_name = 'fact_actuary'
--BLOCK-1 End--

--BLOCK-2 Start--
--Columns and variable types for df.dtypes and df.columns
-- SELECT * EXCEPT(is_generated, generation_expression, is_stored, is_updatable)
-- FROM `geb-dwh-test.uat_geb_dwh_eu_act.INFORMATION_SCHEMA.COLUMNS`
-- WHERE table_name = 'fact_actuary'
--BLOCK-2 End--

-- BLOCK-3 Start--
--Count unique and null values per column for df.nunique(axis=0) and df.isnull().sum()
-- DECLARE columns ARRAY<STRING>;
-- DECLARE query0, query1, query2 STRING;
-- SET columns = (
--   WITH all_columns AS (
--     SELECT column_name
--     FROM `geb-dwh-test.uat_geb_dwh_eu_act.INFORMATION_SCHEMA.COLUMNS`
--     WHERE table_name = 'fact_actuary'
--   )
--   SELECT ARRAY_AGG((column_name) ) AS columns
--   FROM all_columns
-- );
-- SET query0 = (select STRING_AGG('(select count( '||x||')  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`) '||x ) AS string_agg from unnest(columns) x );
-- SET query1 = (select STRING_AGG('(select count(distinct '||x||')  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`) '||x ) AS string_agg from unnest(columns) x );
-- SET query2 = (select STRING_AGG('(select countif( '||x||' is null)  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`) '||x ) AS string_agg from unnest(columns) x );

-- EXECUTE IMMEDIATE 
-- "SELECT 'count' ,"|| query0 || " UNION ALL " ||
-- "SELECT 'unique_count' ,"|| query1 || " UNION ALL " ||
-- "SELECT 'nulls' ,"|| query2
-- ;
--BLOCK-3 End--

-- BLOCK-3-1 Start--
--min / max analysis for numeric and date time values
-- DECLARE columns ARRAY<STRING>;
-- DECLARE query3,query4 STRING;
-- SET columns = (
--   WITH all_columns AS (
--     SELECT column_name
--     FROM `geb-dwh-test.uat_geb_dwh_eu_act.INFORMATION_SCHEMA.COLUMNS`
--     WHERE table_name = 'fact_actuary'
--     and  data_type IN ('INT64','FLOAT64', 'NUMERIC', 'DATETIME')
--   )
--   SELECT ARRAY_AGG((column_name) ) AS columns
--   FROM all_columns
-- );

-- SET query3 = (select STRING_AGG('(select max( '||x||')  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`) '||x ) AS string_agg from unnest(columns) x );
-- SET query4 = (select STRING_AGG('(select min( '||x||')  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`) '||x ) AS string_agg from unnest(columns) x );

-- EXECUTE IMMEDIATE 
-- "SELECT 'max' ,"|| query3 || " UNION ALL " ||
-- "SELECT 'min' ,"|| query4
-- ;
--BLOCK-3-1 End--

--BLOCK-4-1Start--only finding numeric columns 
--How to describe a dataframe or a table (this describe function works for numerical features only)
--df.describe().apply(lambda s: s.apply(lambda x: format(x, 'f')))
-- DECLARE columns ARRAY<STRING>;
-- SET columns = (
-- WITH all_columns AS (
-- SELECT column_name
-- FROM `geb-dwh-test.uat_geb_dwh_eu_act.INFORMATION_SCHEMA.COLUMNS`
-- WHERE table_name = 'fact_actuary'
-- and  data_type IN ('INT64','FLOAT64', 'NUMERIC')
-- )
-- SELECT ARRAY_AGG((column_name) ) AS columns_numeric FROM all_columns
-- );
--BLOCK-4-1 End--

--BLOCK-4-2 All Start--
--How to describe a dataframe or a table (this describe function works for numerical features only)
--df.describe().apply(lambda s: s.apply(lambda x: format(x, 'f')))
-- DECLARE columns ARRAY<STRING>;
-- DECLARE query1, query2, query3, query4, query5, query6, query7 STRING;
-- SET columns = (
--   WITH all_columns AS (
--     SELECT column_name
--     FROM `geb-dwh-test.uat_geb_dwh_eu_act.INFORMATION_SCHEMA.COLUMNS`
--     WHERE table_name = 'fact_actuary' 
--         and  data_type IN ('INT64','FLOAT64', 'NUMERIC')
--   )
--   SELECT ARRAY_AGG((column_name) ) AS columns
--   FROM all_columns
-- );

-- SET query1 = (select STRING_AGG('(select stddev( '||x||')  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`) '||x ) AS string_agg from unnest(columns) x );
-- SET query2 = (select STRING_AGG('(select avg( '||x||')  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`) '||x ) AS string_agg from unnest(columns) x );
-- SET query3 = (select STRING_AGG('(select PERCENTILE_CONT( '||x||', 0.5) over()  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary` limit 1) '||x ) AS string_agg from unnest(columns) x );
-- SET query4 = (select STRING_AGG('(select PERCENTILE_CONT( '||x||', 0.25) over()  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary` limit 1) '||x ) AS string_agg from unnest(columns) x );
-- SET query5 = (select STRING_AGG('(select PERCENTILE_CONT( '||x||', 0.75) over()  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary` limit 1) '||x ) AS string_agg from unnest(columns) x );
-- SET query6 = (select STRING_AGG('(select max( '||x||')  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`) '||x ) AS string_agg from unnest(columns) x );
-- SET query7 = (select STRING_AGG('(select min( '||x||')  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`) '||x ) AS string_agg from unnest(columns) x );

-- EXECUTE IMMEDIATE (
-- "SELECT 'stddev' ,"|| query1 || " UNION ALL " ||
-- "SELECT 'mean'   ,"|| query2 || " UNION ALL " ||
-- "SELECT 'median' ,"|| query3 || " UNION ALL " ||
-- "SELECT '0.25' ,"|| query4 || " UNION ALL " ||
-- "SELECT '0.75' ,"|| query5 || " UNION ALL " ||
-- "SELECT 'max' ,"|| query6 || " UNION ALL " ||
-- "SELECT 'min' ,"|| query7
-- )
-- ;
--BLOCK-4-2 All End--

--BLOCK-5-Missing Values --Start--
--Let’s check if we have any missing values.==> df.isnull().sum()
-- DECLARE columns ARRAY<STRING>;
-- DECLARE query1, query2, query3, query4, query5, query6, query7, query8 STRING;
-- SET columns = (
--   WITH all_columns AS (
--     SELECT column_name
--     FROM `geb-dwh-test.uat_geb_dwh_eu_act.INFORMATION_SCHEMA.COLUMNS`
--     WHERE table_name = 'fact_actuary' 
--         and  data_type IN ('INT64','FLOAT64', 'NUMERIC')
--   )
--   SELECT ARRAY_AGG((column_name) ) AS columns
--   FROM all_columns
-- );

-- SET query1 = (select STRING_AGG('(select stddev( '||x||')  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`) '||x ) AS string_agg from unnest(columns) x );
-- SET query2 = (select STRING_AGG('(select avg( '||x||')  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`) '||x ) AS string_agg from unnest(columns) x );
-- SET query3 = (select STRING_AGG('(select PERCENTILE_CONT( '||x||', 0.5) over()  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary` limit 1) '||x ) AS string_agg from unnest(columns) x );
-- SET query4 = (select STRING_AGG('(select PERCENTILE_CONT( '||x||', 0.25) over()  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary` limit 1) '||x ) AS string_agg from unnest(columns) x );
-- SET query5 = (select STRING_AGG('(select PERCENTILE_CONT( '||x||', 0.75) over()  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary` limit 1) '||x ) AS string_agg from unnest(columns) x );
-- SET query6 = (select STRING_AGG('(select max( '||x||')  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`) '||x ) AS string_agg from unnest(columns) x );
-- SET query7 = (select STRING_AGG('(select min( '||x||')  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`) '||x ) AS string_agg from unnest(columns) x );
-- --This below added
-- SET query8 = (select STRING_AGG('(select countif( '||x||' is null)  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`) '||x ) AS string_agg from unnest(columns) x );

-- EXECUTE IMMEDIATE (
-- "SELECT 'stddev' ,"|| query1 || " UNION ALL " ||
-- "SELECT 'mean'   ,"|| query2 || " UNION ALL " ||
-- "SELECT 'median' ,"|| query3 || " UNION ALL " ||
-- "SELECT '0.25' ,"|| query4 || " UNION ALL " ||
-- "SELECT '0.75' ,"|| query5 || " UNION ALL " ||
-- "SELECT 'max' ,"|| query6 || " UNION ALL " ||
-- "SELECT 'min' ,"|| query7 || " UNION ALL " ||
-- --This below added
-- "SELECT 'nulls' ,"|| query8
-- )
-- ;
--BLOCK-5 End--

--BLOCK-6 Start--
--Cleaning Outliers ==> df_cleaned = df_cleaned[df_cleaned['PAID']<272738.696]
-- DECLARE lower, upper, mean FLOAT64;
-- SET mean = (select avg( PAID)  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`);
-- SET lower = mean - 3 * (select stddev( PAID)  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`);
-- SET upper = mean + 3 * (select stddev( PAID)  from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`);
-- EXECUTE IMMEDIATE (
-- "SELECT * from `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary` WHERE PAID >"|| upper ||" OR PAID < " || lower
-- )
--BLOCK-6 End--


--BLOCK-7 Start--
--Removing Rows with Null Values==> df = df.dropna(axis=0)
--CAUTION: HEAVY QUERY, checks every column and deletes if only a value is missing. appx. 100 GB processes within 4 min. Run only when it is really necessary. 
-- DECLARE columns ARRAY<STRING>;
-- DECLARE query STRING DEFAULT '';
-- DECLARE i INT64 DEFAULT 0;

-- SET columns = (
--   WITH all_columns AS (
--     SELECT column_name
--     FROM `geb-dwh-test.uat_geb_dwh_eu_act.INFORMATION_SCHEMA.COLUMNS`
--     WHERE table_name = 'Test-33_copy' 
--         -- and  data_type IN ('INT64','FLOAT64')
--   )
--   SELECT ARRAY_AGG((column_name) ) AS columns
--   FROM all_columns
-- );

-- LOOP
--     SET i = i + 1;

--     IF i > ARRAY_LENGTH(columns) THEN 
--         LEAVE;
--     END IF;

--     SET query = ' DELETE FROM  `geb-dwh-test.uat_geb_dwh_eu_act.Test-33_copy` WHERE ' || columns[ORDINAL(i)] || ' is null '  ;
--     EXECUTE IMMEDIATE (
--         query
--     );

-- END LOOP;
--BLOCK-7 End--


-- --BLOCK-8 Start--
-- --Analyse Data with group filtering
SELECT DISTINCT countif(KEEP_CLAIM = 'KEEP CLAIM') OVER(PARTITION BY LOCALINSURER)        as keep_claim_cnt
, countif(KEEP_CLAIM = 'K.O')  OVER(PARTITION BY LOCALINSURER)                             as k_o_cnt
, count(*) OVER(PARTITION BY LOCALINSURER)                                                 as total,
    countif(KEEP_CLAIM = 'KEEP CLAIM') OVER(PARTITION BY LOCALINSURER)     /count(*)           as keep_claim_prc
, countif(KEEP_CLAIM = 'K.O') OVER(PARTITION BY LOCALINSURER)     /count(*)                as k_o_pct,
    LOCALINSURER
FROM `geb
-dwh-test.uat_geb_dwh_eu_act.fact_actuary`
GROUP BY KEEP_CLAIM,LOCALINSURER
;


-- --BLOCK-8 End--