
SELECT DISTINCT LOCALINSURER,
    RE_BALANCEYEARPTF,
    --YEARLY TOTAL COUNT
    COUNT(KEEP_CLAIM) OVER (PARTITION BY LOCALINSURER, RE_BALANCEYEARPTF) AS CNT_YR,
    --YEARLY KEEP CLAIM COUNT
    COUNTIF(KEEP_CLAIM = 'KEEP CLAIM') OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF) AS CNT_KC_YR,
    --YEARLY KO COUNT
    COUNTIF(KEEP_CLAIM = 'K.O') OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF) AS CNT_KO_YR,
    --YEARLY KEEP CLAIM PERCENTAGE
    COUNTIF(KEEP_CLAIM = 'KEEP CLAIM') OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF)/COUNT(KEEP_CLAIM) OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF) AS PCT_CNT_KC_YR,
    --YEARLY KO PERCENTAGE
    COUNTIF(KEEP_CLAIM = 'K.O') OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF) / COUNT(KEEP_CLAIM) OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF) AS PCT_CNT_KO_YR,

    --YEARLY SUM BEGRES AND PERCENTAGE CALC
    --SUM TOTAL BEGRES
    SUM(SUM_BEGRES) OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF) AS SUM_BEGRES_YR,
    --SUM KEEP CLAIM BEGRES
    SUM(CASE WHEN KEEP_CLAIM = 'KEEP CLAIM' THEN SUM_BEGRES ELSE 0 END) OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF) AS SUM_KC_BEGRES,
    --SUM KO BEGRES
    SUM(CASE WHEN KEEP_CLAIM = 'K.O' THEN SUM_BEGRES ELSE 0 END) OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF) AS SUM_KO_BEGRES,
    --SUM KEEP CLAIM BEGRES PERCENTAGE
    COALESCE(SAFE_DIVIDE(SUM(CASE WHEN KEEP_CLAIM = 'KEEP CLAIM' THEN SUM_BEGRES ELSE 0 END) OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF), SUM(SUM_BEGRES) OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF)),0) AS PCT_SUM_KC_BEGRES,
    --SUM KO BEGRES PERCENTAGE
    COALESCE(SAFE_DIVIDE(SUM(CASE WHEN KEEP_CLAIM = 'K.O' THEN SUM_BEGRES ELSE 0 END) OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF), SUM(SUM_BEGRES) OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF)),0) AS PCT_SUM_KO_BEGRES,

    --YEARLY SUM ENDRES AND PERCENTAGE CALC
    SUM(SUM_ENDRES) OVER (PARTITION BY LOCALINSURER) AS SUM_ENDRES_YR,
    SUM(CASE WHEN KEEP_CLAIM = 'KEEP CLAIM' THEN SUM_ENDRES ELSE 0 END) OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF) AS SUM_KC_ENDRES,
    SUM(CASE WHEN KEEP_CLAIM = 'K.O' THEN SUM_ENDRES ELSE 0 END) OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF) AS SUM_KO_ENDRES,

    COALESCE(SAFE_DIVIDE(SUM(CASE WHEN KEEP_CLAIM = 'KEEP CLAIM' THEN SUM_ENDRES ELSE 0 END) OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF), SUM(SUM_ENDRES) OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF)),0) AS PCT_SUM_KC_ENDRES,
    COALESCE(SAFE_DIVIDE(SUM(CASE WHEN KEEP_CLAIM = 'K.O' THEN SUM_ENDRES ELSE 0 END) OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF), SUM(SUM_ENDRES) OVER (PARTITION BY LOCALINSURER,RE_BALANCEYEARPTF)),0) AS PCT_SUM_KO_ENDRES, 
-- "GR3-CLAIMID1-Policy Nr.+Cover Code+Claim Date" as CALC_METHOD

FROM (SELECT
        DISTINCT *,
        MIN(KC_STATUS) OVER (PARTITION BY CLAIMID_1 ) AS KEEP_CLAIM, 
    FROM
        (
  SELECT *,
            LAG(SUM_ENDRES, 1, 0) OVER (PARTITION BY CLAIMID_1 ORDER BY CLAIMID_1, RE_BALANCEYEARPTF) AS SUM_PREV_ENDRES,
            IF (COALESCE(SUM_BEGRES, 0)=LAG
(SUM_ENDRES, 1, 0) OVER
(PARTITION BY CLAIMID_1 ORDER BY CLAIMID_1, RE_BALANCEYEARPTF) , 'KEEP CLAIM', 'K.O') AS KC_STATUS,
  FROM
(
  SELECT DISTINCT
    CLAIMID_1,
    LOCALINSURER,
    RE_BALANCEYEARPTF,
    COALESCE(SUM(BEGRES) OVER (PARTITION BY CLAIMID_1, RE_BALANCEYEARPTF ORDER BY CLAIMID_1, RE_BALANCEYEARPTF ),0) AS SUM_BEGRES,--not MAX, CONFIRMED
    COALESCE(SUM(ENDRES) OVER (PARTITION BY CLAIMID_1, RE_BALANCEYEARPTF ORDER BY CLAIMID_1, RE_BALANCEYEARPTF ),0) AS SUM_ENDRES, --not MIN, CONFIRMED

FROM
    `geb
-dwh-test.uat_geb_dwh_eu_act.fact_actuary_v5`

    -- ORDER BY CLAIMID_1, RE_BALANCEYEARPTF
    ) s
)

 
)
GROUP BY RE_BALANCEYEARPTF, CLAIMID_1,LOCALINSURER, SUM_BEGRES,SUM_ENDRES ,SUM_PREV_ENDRES, KC_STATUS, KEEP_CLAIM
 ORDER BY LOCALINSURER, RE_BALANCEYEARPTF

