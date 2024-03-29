WITH
    source_keep_claim
    AS

    (
        SELECT
            *
        FROM (
    SELECT
                a.CLAIMID_1 CLAIMID_1,
                a.LOCALINSURER,
                RE_BALANCEYEARPTF,
                BEGRES,
                ENDRES, 
            FROM
                `geb-dwh
    
    -test.uat_geb_dwh_eu_act.fact_actuary_v3` a
    GROUP BY
      1, 2, 3, 4, 5 
      )AS pvt1 PIVOT
(SUM
(BEGRES) SUM_BEGRES,
      SUM
(ENDRES) SUM_ENDRES FOR RE_BALANCEYEARPTF IN
(2012,
        2013,
        2014,
        2015,
        2016,
        2017,
        2018,
        2019,
        2020)) pvt2
  ORDER BY
    1)
SELECT
    *, 
IF
  ((COALESCE(SUM_ENDRES_2012,0)=COALESCE(SUM_BEGRES_2013,0)
    AND COALESCE(SUM_ENDRES_2013,0)=COALESCE(SUM_BEGRES_2014,0)
    AND COALESCE(SUM_ENDRES_2014,0)=COALESCE(SUM_BEGRES_2015,0)
    AND COALESCE(SUM_ENDRES_2015,0)=COALESCE(SUM_BEGRES_2016,0)
    AND COALESCE(SUM_ENDRES_2016,0)=COALESCE(SUM_BEGRES_2017,0)
    AND COALESCE(SUM_ENDRES_2017,0)=COALESCE(SUM_BEGRES_2018,0)
    AND COALESCE(SUM_ENDRES_2018,0)=COALESCE(SUM_BEGRES_2019,0)
    AND COALESCE(SUM_ENDRES_2019,0)=COALESCE(SUM_BEGRES_2020,0)
    --AND COALESCE(SUM_ENDRES_2020,0)=COALESCE(SUM_BEGRES_2021,0) 
    AND NOT (SUM_BEGRES_2012 IS NULL AND SUM_ENDRES_2012 IS NULL AND SUM_BEGRES_2013 IS NULL AND SUM_ENDRES_2013 IS NULL AND SUM_BEGRES_2014 IS NULL AND SUM_ENDRES_2014 IS NULL AND
        SUM_BEGRES_2015 IS NULL AND SUM_ENDRES_2015 IS NULL AND SUM_BEGRES_2016 IS NULL AND SUM_ENDRES_2016 IS NULL AND SUM_BEGRES_2017 IS NULL AND SUM_ENDRES_2017 IS NULL AND
        SUM_BEGRES_2018 IS NULL AND SUM_ENDRES_2018 IS NULL AND SUM_BEGRES_2019 IS NULL AND SUM_ENDRES_2019 IS NULL AND SUM_BEGRES_2020 IS NULL AND SUM_ENDRES_2020 IS NULL)
    ),'KEEP CLAIM','K.O.') KEEPCLAIM
FROM
  source_keep_claim