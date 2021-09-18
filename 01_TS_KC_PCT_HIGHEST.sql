SELECT
    LOCALINSURER,
    CALC_METHOD,
    MAX(PCT_SUM_KC_ENDRES) OVER (PARTITION BY LOCALINSURER, CALC_METHOD ORDER BY PCT_SUM_KC_ENDRES DESC ) AS MaxPct,
    ROW_NUMBER() OVER (PARTITION BY LOCALINSURER ORDER BY PCT_SUM_KC_ENDRES DESC, CALC_METHOD DESC ) Row_NR
FROM
    `geb
-dwh-test.uat_geb_dwh_eu_act.source_claimid_kpi_all`
GROUP BY
  LOCALINSURER,
  CALC_METHOD,
  PCT_SUM_KC_ENDRES