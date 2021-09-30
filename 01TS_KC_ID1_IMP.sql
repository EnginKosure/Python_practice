SELECT
    DISTINCT *,
    MIN(KC_STATUS) OVER (PARTITION BY CLAIMID_1 ) AS KEEP_CLAIM, 
FROM
    (
  SELECT DISTINCT *,
        LAG(SUM_ENDRES, 1, 0) OVER (PARTITION BY CLAIMID_1 ORDER BY CLAIMID_1, RE_BALANCEYEARPTF) AS SUM_PREV_ENDRES,
        COUNT(CLAIMID_1) OVER (PARTITION BY CLAIMID_1) AS COUNT_CLAIMID,
        ROW_NUMBER() OVER (PARTITION BY CLAIMID_1 ORDER BY CLAIMID_1, RE_BALANCEYEARPTF) AS ROW_NR,
        MAX(SUM_ENDRES) OVER (PARTITION BY CLAIMID_1) AS MAX_SUM_ENDRES,
        CASE 
  --To catch the claims that has always NULL reserves ==> K.O
  WHEN MAX(SUM_ENDRES) OVER (PARTITION BY CLAIMID_1) IS NULL
    THEN 'K.O'
  --To catch the first BY's claim ==> KEEP CLAIM (Because there is no previous year, thus no SUM_ENDRES of previous year to compare)
  WHEN /*COUNT(CLAIMID_1) OVER (PARTITION BY CLAIMID_1) =1 OR*/ ROW_NUMBER() OVER (PARTITION BY CLAIMID_1 ORDER BY CLAIMID_1, RE_BALANCEYEARPTF)=1
    THEN 'KEEP CLAIM'
  --If there are more than one BY, check if SUM_PREV_ENDRES is equal to SUM_BEGRES ==> KEEP CLAIM
  WHEN COALESCE(SUM_BEGRES,0)=LAG(SUM_ENDRES, 1, 0) OVER (PARTITION BY CLAIMID_1 ORDER BY CLAIMID_1, RE_BALANCEYEARPTF)
    THEN 'KEEP CLAIM'
  ELSE 'K.O'
END AS KC_STATUS

    --  IF (COALESCE(SUM_BEGRES,0)=LAG(SUM_ENDRES, 1, 0) OVER (PARTITION BY CLAIMID_1 ORDER BY CLAIMID_1, RE_BALANCEYEARPTF) , 'KEEP CLAIM', 'K.O') AS KC_STATUS,
    FROM
        (
  SELECT DISTINCT
            CLAIMID_1,
            LOCALINSURER,
            RE_BALANCEYEARPTF,
            -- COALESCE(SUM(BEGRES) OVER (PARTITION BY CLAIMID_1, RE_BALANCEYEARPTF ORDER BY CLAIMID_1, RE_BALANCEYEARPTF ),0) AS SUM_BEGRES,--not MAX, CONFIRMED
            -- COALESCE(SUM(ENDRES) OVER (PARTITION BY CLAIMID_1, RE_BALANCEYEARPTF ORDER BY CLAIMID_1, RE_BALANCEYEARPTF ),0) AS SUM_ENDRES,--not MIN, CONFIRMED
            SUM(BEGRES) OVER (PARTITION BY CLAIMID_1, RE_BALANCEYEARPTF ORDER BY CLAIMID_1, RE_BALANCEYEARPTF ) AS SUM_BEGRES,--not MAX, CONFIRMED --without COALESCE TBC
            SUM(ENDRES) OVER (PARTITION BY CLAIMID_1, RE_BALANCEYEARPTF ORDER BY CLAIMID_1, RE_BALANCEYEARPTF ) AS SUM_ENDRES, --not MIN, CONFIRMED --without COALESCE TBC

        FROM
            `geb-dwh-test
.uat_geb_dwh_eu_act.fact_actuary_staging`
    -- ORDER BY CLAIMID_1, RE_BALANCEYEARPTF
  ) s
)
  --Below line is for testing purposes, must be closed during production run.
  WHERE /*(MAX_SUM_ENDRES IS NULL OR MAX_SUM_ENDRES=0) AND */COUNT_CLAIMID>1
  ORDER BY CLAIMID_1, RE_BALANCEYEARPTF
  --The ORDER BY statement above is only for testing purposes. Please feel free to open when needed.