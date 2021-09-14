(
-- DATE_VALUE_ADJUSTED is not present in the new view to check all commented lines
            WITH staging_fa AS (SELECT DISTINCT

            fa.SELECTED_CLAIM_ID,
            fa.INSUREDBIRTHDATE,
            --fa.AGEOFINSURED, --will be calculated at export phase of fact_actuary,
            fa.ESCALATION_PCT,
            fa.COVERDESCRIPTION_NEW,
            fa.COVERCODE_NEW,
            fa.PO_LINEOFRISK,
            fa.RE_BALANCEYEARPTF AS BALANCE_YEAR,
            fa.POLICY_NR,
            fa.LINEOFPRODUCT,
            fa.CLAIMDATE,
            fa.AY_ACCIDENT_YEAR,
            fa.BEGRES,
            fa.PAID,
            fa.ENDRES,
            fa.PO_ANNUALBENEFITAMOUNT AS THEORETICAL_ANNUAL_BENEFIT,--58
            fa.ANNUALIZED_PAID,--59
            fa.CY_PY,--37
            FORMAT_DATE("%d/%m/%Y",MIN(PARSE_DATE("%d/%m/%Y",fa.CURRENTDAY)) OVER (PARTITION BY fa.SELECTED_CLAIM_ID)) AS FIRST_APPEARANCE_DATE,
            EXTRACT(YEAR FROM MIN(PARSE_DATE("%d/%m/%Y",fa.CURRENTDAY)) OVER (PARTITION BY fa.SELECTED_CLAIM_ID)) AS FIRST_APPEARANCE_YEAR,
            IF(EXTRACT(YEAR FROM MIN(PARSE_DATE("%d/%m/%Y",fa.CURRENTDAY)) OVER (PARTITION BY fa.SELECTED_CLAIM_ID))=fa.RE_BALANCEYEARPTF, 1, 0) AS FIRST_OPENING_CLAIM,
            IF(COALESCE(fa.ENDRES,0) !=0, 1, 0) AS OPEN_CLAIM, 
            IF(COALESCE(fa.ENDRES,0) =0 AND MAX(fa.PAID) OVER (PARTITION BY fa.SELECTED_CLAIM_ID)>0, 1, 0) AS CLOSED_CLAIM,
            IF(COALESCE(fa.ENDRES,0) =0 AND MAX(COALESCE(fa.PAID,0)) OVER (PARTITION BY fa.SELECTED_CLAIM_ID)=0, 1, 0) CLOSED_CLAIM_W_O_PAYMENT,
            IF(COALESCE(fa.BEGRES,0) =0 AND fa.RE_BALANCEYEARPTF>CAST(fa.AY_ACCIDENT_YEAR AS INT64), 1, 0) AS IBNR_REOPENED_CLAIM,
            IF(COALESCE(fa.BEGRES,0) =0 AND fa.RE_BALANCEYEARPTF>CAST(fa.AY_ACCIDENT_YEAR AS INT64) AND EXTRACT(YEAR FROM MIN(PARSE_DATE("%d/%m/%Y",fa.CURRENTDAY)) OVER (PARTITION BY fa.SELECTED_CLAIM_ID))=fa.RE_BALANCEYEARPTF, 1, 0) AS IBNR,
            

         (select VALIDFROM from uat_geb_dwh_eu_awr.dim_dummy) VALIDFROM, --added this as it is standard in all tables
         (select VALIDTILL from uat_geb_dwh_eu_awr.dim_dummy) VALIDTILL,  --added this as it is standard in all tables
         max( fa.CREATED_ON) CREATED_ON -- the selection of the new records is done based on this created_on
         -- whether it should be max() -> to be confirmed/checked later 

            FROM  `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary_v5` fa

            -- WHERE fa.CREATED_ON >
            -- case when (select max(dp_start) from `geb-dwh-test.uat_geb_met_eu.meta_dp_log`
            -- where dp_end is not null and dp_name = 'Fact_Actuary') is null
            -- then TIMESTAMP('1999-01-01 00:00:01.000000 UTC')
            -- else (select max(dp_start) from `geb-dwh-test.uat_geb_met_eu.meta_dp_log`
            -- where dp_end is not null and dp_name = 'Fact_Actuary')  end
      --if line 35 max(fa.CREATED_ON) can be calculated in a different way, we don't need the GROUP BY below
         GROUP BY SELECTED_CLAIM_ID,INSUREDBIRTHDATE,ESCALATION_PCT,COVERDESCRIPTION_NEW,COVERCODE_NEW,PO_LINEOFRISK,RE_BALANCEYEARPTF,
         POLICY_NR,LINEOFPRODUCT,CLAIMDATE,AY_ACCIDENT_YEAR,BEGRES,PAID,ENDRES,PO_ANNUALBENEFITAMOUNT,ANNUALIZED_PAID,CY_PY,CURRENTDAY
         )

         SELECT * EXCEPT (THEORETICAL_ANNUAL_BENEFIT,
            ANNUALIZED_PAID,CY_PY),
               MAX(staging_fa.IBNR) OVER (PARTITION BY staging_fa.SELECTED_CLAIM_ID) AS IBNR_ACROSS_TIME,
               IF(MAX(staging_fa.IBNR) OVER (PARTITION BY staging_fa.SELECTED_CLAIM_ID)=1, staging_fa.BALANCE_YEAR-staging_fa.FIRST_APPEARANCE_YEAR,0) AS IBNR_DEV_FIRST_APP,
               IF(MAX(staging_fa.IBNR) OVER (PARTITION BY staging_fa.SELECTED_CLAIM_ID)=1, staging_fa.BALANCE_YEAR-CAST(staging_fa.AY_ACCIDENT_YEAR AS INT64 ),0) AS IBNR_DEV_ON_AY,
               IF(staging_fa.IBNR_REOPENED_CLAIM=1 AND MAX(staging_fa.IBNR) OVER (PARTITION BY staging_fa.SELECTED_CLAIM_ID)=1,0,1) AS RE_OPENED_CLAIM,
               staging_fa.BALANCE_YEAR - CAST(staging_fa.AY_ACCIDENT_YEAR AS INT64) AS DEVELOPMENT_PERIOD_ON_AY,
               IF(staging_fa.BEGRES>0 OR staging_fa.PAID>0 OR staging_fa.ENDRES>0, 1, 0) AS FLAG_AMOUNT_GRT_0,
               staging_fa.CY_PY,
               CASE 
                  WHEN staging_fa.CY_PY='CY' THEN 'CY' 
                  WHEN staging_fa.CY_PY='PY' THEN (
                                                CASE 
                                                   WHEN staging_fa.BALANCE_YEAR-CAST(staging_fa.AY_ACCIDENT_YEAR AS INT64)>8 THEN CONCAT('PY',' 8+')
                                                   ELSE CONCAT('PY ', staging_fa.BALANCE_YEAR-CAST(staging_fa.AY_ACCIDENT_YEAR AS INT64 ))
                                                END)
                  ELSE 'n.a.'
               END AS CY_PY_DETAILED,--TBC 'n.a.'
               IF(COALESCE(BEGRES,0)>0,1,0) AS FLAG_OP_RES_GRT_0,-- Confirmed
               IF(BEGRES>0 AND CLOSED_CLAIM=1,1,0) AS FLAG_CLOSED_CLAIM_W_OP_RES_GRT_0,
               IF(IF(BEGRES>0 AND CLOSED_CLAIM>0,1,0)=1,BEGRES, 0) AS OP_RES_TO_CLOSE_CLAIM,
               IF(IF(BEGRES>0 AND CLOSED_CLAIM>0,1,0)=1,PAID, 0) AS PAY_TO_CLOSE_CLAIM,
               IF(IF(BEGRES>0 AND CLOSED_CLAIM>0,1,0)=1,BEGRES-PAID, 0) AS DEF_SURPL_TO_CLOSE_CLAIM,
               IF(BEGRES>0 AND OPEN_CLAIM=1,1,0) AS FLAG_OPEN_CLAIM_W_OP_RES_GRT_0,--44
               IF(IF(BEGRES>0 AND OPEN_CLAIM=1,1,0)>0,BEGRES,0) AS OP_RES_TO_OPEN,--45
               IF(IF(BEGRES>0 AND OPEN_CLAIM=1,1,0)>0,PAID,0) AS PAY_TO_OPEN, --46
               IF(IF(BEGRES>0 AND OPEN_CLAIM=1,1,0)>0,ENDRES,0) AS CLOSE_RES_TO_OPEN,
               IF(IF(BEGRES>0 AND OPEN_CLAIM=1,1,0)>0,(BEGRES-PAID-ENDRES),0) AS DEF_SURPL_TO_OPEN,--48 BEGRES-PAID-ENDRES
               IF(BEGRES >0 AND CLOSED_CLAIM_W_O_PAYMENT=1,1,0) AS FLAG_CLOSED_CLAIM_WO_PAY_W_OP_RES_GRT_0,
               IF(IF(BEGRES>0 AND CLOSED_CLAIM=1,1,0)=1, BEGRES, 0) AS OP_RES_TO_CLOSE_WO_PAY, --50
               IF(IF(BEGRES>0 AND staging_fa.CLOSED_CLAIM=1,1,0)=1, BEGRES, 0) AS DEF_SURPL_TO_CLOSE_WO_PAY, --51 The same with 50
               IF(IF(IBNR_REOPENED_CLAIM=1 AND MAX(IBNR) OVER (PARTITION BY SELECTED_CLAIM_ID)=1,0,1)=1, (PAID+ENDRES), 0) AS REOPEN_INCURRED,--52
               IF(IF(IBNR_REOPENED_CLAIM=1 AND MAX(IBNR) OVER (PARTITION BY SELECTED_CLAIM_ID)=1,0,1)=1, PAID,0) AS REOPEN_PAY,--53
               IF(IF(IBNR_REOPENED_CLAIM=1 AND MAX(IBNR) OVER (PARTITION BY SELECTED_CLAIM_ID)=1,0,1)=1, ENDRES,0) AS REOPEN_END_RES,
               IF(IF(IBNR_REOPENED_CLAIM=1 AND MAX(IBNR) OVER (PARTITION BY SELECTED_CLAIM_ID)=1,0,1)=1,-(PAID+ENDRES), 0) AS DEF_SURPL_REOPEN,
               DATE_DIFF(PARSE_DATE('%d/%m/%Y',CONCAT('31/12/',BALANCE_YEAR)), PARSE_DATE('%d/%m/%Y',CLAIMDATE), YEAR) AS DURATION_SINCE_CLAIM_DATE,
               DATE_DIFF(PARSE_DATE('%d/%m/%Y',CONCAT('31/12/',BALANCE_YEAR)), PARSE_DATE('%d/%m/%Y',FIRST_APPEARANCE_DATE), YEAR) AS DURATION_SINCE_FIRST_PAYMENT_DATE,
               THEORETICAL_ANNUAL_BENEFIT,
               ANNUALIZED_PAID,            
               IF(OPEN_CLAIM=1, COALESCE(SAFE_DIVIDE(ENDRES,THEORETICAL_ANNUAL_BENEFIT),0),NULL) AS ESTIMATED_DURATION_THEORETICAL_ANNUAL_BENEFIT,
               IF(OPEN_CLAIM=1, COALESCE(SAFE_DIVIDE(ENDRES,ANNUALIZED_PAID),0),NULL) AS ESTIMATED_DURATION_ANNUALIZED_PAID,

             FROM staging_fa 
             
             ORDER BY SELECTED_CLAIM_ID, BALANCE_YEAR
             
             )