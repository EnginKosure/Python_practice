-- =============================================SOURCE_TRIANGLE_INPUT_3_CUMULATIVE_PAID_TRIANGLES========================================================
-- Author      : in@geb.com, kosure@geb.com
-- Create date : 29-09-2021 (updated on 20-10-2021 according to the ResQ_Input v_3 requirements)
-- Description : Provides the Cumulative Paid Triangles input table for ReSQ for the purpose of reserve evaluation with non life techniques.
--               The data of this table are based on the Non-Cumulative Paid Triangles.
-- Input       : `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`
-- Output      : triangle_input_3_cumulative_paid_triangles table
-- Related DAG : actuary_uat_v2.py
-- TODOs       : --SEE LINE 24
-- ======================================================================================================================================================

WITH
  non_cum
  as
  
  (
    SELECT
      DISTINCT PO_LINEOFRISK,
      COVERCODE_NEW,
      UNIQUE_ACCIDENT_YEAR, --ResQ_Input v_3
      UNIQUE_DEVELOPMENT_PERIOD_IN_QUARTERS, --ResQ_Input v_3
      SUM(PAID) OVER (PARTITION BY UNIQUE_ACCIDENT_YEAR,UNIQUE_DEVELOPMENT_PERIOD_IN_QUARTERS, PO_LINEOFRISK, COVERCODE_NEW) SUM_PAID
    FROM
      `geb
  -dwh-test.uat_geb_dwh_eu_act.fact_actuary` a
WHERE
  COVERCODE_NEW IN
('LTD','PD','LTD-SS') AND 
  CAST
(a.UNIQUE_ACCIDENT_YEAR AS INT64 )>=2012 --TBC
)
--Below, SUM_PAID is only for testing, will be removed before production run
SELECT DISTINCT * /*EXCEPT(SUM_PAID)*/ ,
  SUM(SUM_PAID) OVER (PARTITION BY UNIQUE_ACCIDENT_YEAR,COVERCODE_NEW , PO_LINEOFRISK ORDER BY UNIQUE_ACCIDENT_YEAR,UNIQUE_DEVELOPMENT_PERIOD_IN_QUARTERS ROWS BETWEEN UNBOUNDED PRECEDING  AND CURRENT ROW) AS CUM_PAID
FROM non_cum
ORDER BY
  COVERCODE_NEW,  UNIQUE_ACCIDENT_YEAR,  UNIQUE_DEVELOPMENT_PERIOD_IN_QUARTERS