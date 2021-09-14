WITH fa AS (
-- DATE_VALUE_ADJUSTED is not present in the new view to check all commented lines
            SELECT   DISTINCT
               --IFNULL(portfolio.PORTDWHID, (select dwhid from uat_geb_dwh_eu_awr.dim_dummy))PORTDWHID,
               --IFNULL(cov.COVERDWHID, (select dwhid from uat_geb_dwh_eu_awr.dim_dummy))COVERDWHID, --policy_renewalID + _ + policy_coverage_code
               --IFNULL(cur.CURRENCYDWHID, (select dwhid from uat_geb_dwh_eu_awr.dim_dummy)) CURRENCYDWHID,
               --(select dwhid from uat_geb_dwh_eu_awr.dim_dummy) CLAIMTYPEDWHID, --dummy
               --IFNULL(inc.INCLUDINGTYPEDWHID, (select dwhid from uat_geb_dwh_eu_awr.dim_dummy)) RESULTINCLUDINGTYPEDWHID, --new column suggested by Fabiano
            -- a.CLAIMDWHID,  --TBC
            country.CNTRNAME LICOUNTRY,
            companyli.SHORTNAME LOCALINSURER,
            clientlc.LC_CIELEGALNAME LOCALCLIENT,
            LOCALCD POLICY_NR, --new field
            INCLUDINGTYPECD PO_COVER_INCLUDING_TYPE, --new field
            CASE
               WHEN clientrole.CLIENTROLELABEL='POOL' AND inctype.INCLUDINGTYPECD='YES' THEN "Pool"
               WHEN clientrole.CLIENTROLELABEL='CAPTIVE' AND inctype.INCLUDINGTYPECD='YES' THEN "Captive"
               ELSE "Reinsurance Only"
            END AS LINEOFPRODUCT,--new field 
            COVERTYPELABEL COVERDESCRIPTION_NEW, --new field
            COVERLOCCD COVERCODE_NEW, --new field
            LINEOFRISKLABEL PO_LINEOFRISK, --new field
            --INSUREDPERSON, --in v2, canceled.
            CARRIERREFERENCE,
            a.GENDER,--not available for historical
            -- a.CLAIMID PO_CLAIM,--cancelled in v3
            CONCAT(COALESCE(framework.LOCALCD,'#'),'_',COALESCE(cov.COVERLOCCD,'#'),'_',COALESCE(FORMAT_DATE("%d/%m/%Y",CLAIMDATE),'#')) CLAIMID_1, --new field
            CONCAT(COALESCE(framework.LOCALCD,'#'),'_',COALESCE(cov.COVERLOCCD,'#'),'_',COALESCE(INSUREDBIRTHDATE,'#')) CLAIMID_2, --new field, encrypted birthdate--use encrypted
            CONCAT(COALESCE(framework.LOCALCD,'#'),'_',COALESCE(cov.COVERLOCCD,'#'),'_',COALESCE(CARRIERREFERENCE,'#'),'_',COALESCE(FORMAT_DATE("%d/%m/%Y",CLAIMDATE),'#')) CLAIMID_3, --new field
            CONCAT(COALESCE(framework.LOCALCD,'#'),'_',COALESCE(cov.COVERLOCCD,'#'),'_',COALESCE(CARRIERREFERENCE,'#')) CLAIMID_4, --new field
            CASE  
               WHEN 
               (SELECT s.CALC_METHOD FROM
                           (SELECT LOCALINSURER , CALC_METHOD,
                              MAX(PCT_SUM_KC_ENDRES) OVER (PARTITION BY LOCALINSURER, CALC_METHOD ORDER BY PCT_SUM_KC_ENDRES DESC )  AS MaxPct,
                              ROW_NUMBER() OVER (PARTITION BY LOCALINSURER ORDER BY PCT_SUM_KC_ENDRES DESC, CALC_METHOD DESC ) Row_NR
                              FROM `geb-dwh-test.uat_geb_dwh_eu_act.source_keep_claim_w_li_dynamic_v5_pct`
                              GROUP BY LOCALINSURER, CALC_METHOD, PCT_SUM_KC_ENDRES) s
                           WHERE s.ROW_NR=1 AND s.LOCALINSURER=companyli.SHORTNAME) 
                     LIKE '%CLAIMID1%' THEN CONCAT(COALESCE(framework.LOCALCD,'#'),'_',COALESCE(cov.COVERLOCCD,'#'),'_',COALESCE(FORMAT_DATE("%d/%m/%Y",CLAIMDATE),'#'))
               WHEN (SELECT s.CALC_METHOD FROM
                           (SELECT LOCALINSURER , CALC_METHOD,
                              MAX(PCT_SUM_KC_ENDRES) OVER (PARTITION BY LOCALINSURER, CALC_METHOD ORDER BY PCT_SUM_KC_ENDRES DESC )  AS MaxPct,
                              ROW_NUMBER() OVER (PARTITION BY LOCALINSURER ORDER BY PCT_SUM_KC_ENDRES DESC, CALC_METHOD DESC ) Row_NR
                              FROM `geb-dwh-test.uat_geb_dwh_eu_act.source_keep_claim_w_li_dynamic_v5_pct`
                              GROUP BY LOCALINSURER, CALC_METHOD, PCT_SUM_KC_ENDRES) s
                           WHERE s.ROW_NR=1 AND s.LOCALINSURER=companyli.SHORTNAME) 
                     LIKE'%CLAIMID2%' THEN  CONCAT(COALESCE(framework.LOCALCD,'#'),'_',COALESCE(cov.COVERLOCCD,'#'),'_',COALESCE(INSUREDBIRTHDATE,'#'))
               WHEN (SELECT s.CALC_METHOD FROM
                           (SELECT LOCALINSURER , CALC_METHOD,
                              MAX(PCT_SUM_KC_ENDRES) OVER (PARTITION BY LOCALINSURER, CALC_METHOD ORDER BY PCT_SUM_KC_ENDRES DESC )  AS MaxPct,
                              ROW_NUMBER() OVER (PARTITION BY LOCALINSURER ORDER BY PCT_SUM_KC_ENDRES DESC, CALC_METHOD DESC ) Row_NR
                              FROM `geb-dwh-test.uat_geb_dwh_eu_act.source_keep_claim_w_li_dynamic_v5_pct`
                              GROUP BY LOCALINSURER, CALC_METHOD, PCT_SUM_KC_ENDRES) s
                           WHERE s.ROW_NR=1 AND s.LOCALINSURER=companyli.SHORTNAME) 
                     LIKE'%CLAIMID3%' THEN CONCAT(COALESCE(framework.LOCALCD,'#'),'_',COALESCE(cov.COVERLOCCD,'#'),'_',COALESCE(CARRIERREFERENCE,'#'),'_',COALESCE(FORMAT_DATE("%d/%m/%Y",CLAIMDATE),'#'))
               WHEN (SELECT s.CALC_METHOD FROM
                           (SELECT LOCALINSURER , CALC_METHOD,
                              MAX(PCT_SUM_KC_ENDRES) OVER (PARTITION BY LOCALINSURER, CALC_METHOD ORDER BY PCT_SUM_KC_ENDRES DESC )  AS MaxPct,
                              ROW_NUMBER() OVER (PARTITION BY LOCALINSURER ORDER BY PCT_SUM_KC_ENDRES DESC, CALC_METHOD DESC ) Row_NR
                              FROM `geb-dwh-test.uat_geb_dwh_eu_act.source_keep_claim_w_li_dynamic_v5_pct`
                              GROUP BY LOCALINSURER, CALC_METHOD, PCT_SUM_KC_ENDRES) s
                           WHERE s.ROW_NR=1 AND s.LOCALINSURER=companyli.SHORTNAME) 
                     LIKE'%CLAIMID4%' THEN CONCAT(COALESCE(framework.LOCALCD,'#'),'_',COALESCE(cov.COVERLOCCD,'#'),'_',COALESCE(CARRIERREFERENCE,'#'))
               ELSE 'n/a'
               END as SELECTED_CLAIM_ID, --new field
            FORMAT_DATE("%d/%m/%Y",a.CLAIMDATE) CLAIMDATE,
            FORMAT_DATE("%Y",CLAIMDATE) AY_ACCIDENT_YEAR, --new field
            LASTPAYMENTDATE,
            INSUREDBIRTHDATE,
            BENEFITSTARTDATE CLAIM_BENEFITBEGDATE,
            BENEFITENDDATE CLAIM_BENEFITENDDATE,
            CURRENCYLABEL LOCALCURRENCY,
            PORTNAME RE_PORTFOLIO,
            AYEAR RE_BALANCEYEARPTF,
            AQUARTER RE_QUARTERPTF,
            CONCAT(portfolio.AYEAR,0,portfolio.AQUARTER) CURRENTQUARTER, --new field; there are 0 values as quarter in dim_portfolio?
            FORMAT_DATE("%d/%m/%Y", DATE_SUB(LAST_DAY(CAST(CONCAT(AYEAR,'-',CAST(IF(portfolio.AQUARTER IN ('0', '0 or 4 ??'),'1',portfolio.AQUARTER) AS INT64 )*3,'-15') AS DATE), quarter), INTERVAL 45 DAY)) CURRENTDAY,
            --DATE_DIFF(LAST_DAY(CAST(CONCAT(2021,'-',CAST(IF(portfolio.AQUARTER IN ('0', '0 or 4 ??'),'1',portfolio.AQUARTER) AS INT64 )*3,'-15') AS DATE), QUARTER), PARSE_DATE("%d/%m/%Y", INSUREDBIRTHDATE),DAY)/365.24 AGEOFINSURED,--new field, fails to parse the encrypted string for INSUREDBIRTHDATE--null, will be calculated at export phase in data fusion
            CASE
               WHEN CAST(COALESCE(FORMAT_DATE("%Y",CLAIMDATE),'2500') AS INT64 )=AYEAR THEN "CY"
               WHEN CAST(COALESCE(FORMAT_DATE("%Y",CLAIMDATE),'2500') AS INT64)<0 THEN "CY"--2nd
               WHEN CAST(COALESCE(FORMAT_DATE("%Y",CLAIMDATE),'2500') AS INT64)<AYEAR THEN "PY"--3rd
               ELSE "n.a."
            END AS CY_PY,--new field
            
            portfolio.EXPYEAR RE_EXPERIENCEYEARPTF,
            a.ANNUITY,
            a.LUMPSUM,
            COALESCE(a.ANNUITY,0)+COALESCE(a.LUMPSUM,0) AS  PAID, --new field--coalesce
            a.BEGINRESERVEAMNT BEGRES,
            a.ENDRESERVEAMNT ENDRES,
            a.ANNUALBENEFITAMNT PO_ANNUALBENEFITAMOUNT,
--Below, old version, new version needs confirmation
            -- SAFE_DIVIDE(SUM(COALESCE(a.ANNUITY,0)+COALESCE(a.LUMPSUM,0)),CAST(IF(portfolio.AQUARTER IN ('0', '0 or 4 ??'),'1',portfolio.AQUARTER) AS INT64 )*4) ANNUALIZED_PAID, --new field
            SAFE_DIVIDE(
               SUM(COALESCE(a.ANNUITY,0)+COALESCE(a.LUMPSUM,0)) OVER (PARTITION BY CARRIERREFERENCE, AYEAR) , 
            (COUNTIF((COALESCE(a.ANNUITY,0)+COALESCE(a.LUMPSUM,0))<>0) OVER (PARTITION BY CARRIERREFERENCE, AYEAR))
            )*4 ANNUALIZED_PAID, --new field
            
            -- (COUNTIF((COALESCE(a.ANNUITY,0)+COALESCE(a.LUMPSUM,0))<>0) OVER (PARTITION BY CARRIERREFERENCE, AYEAR)) TEST,
            -- (COUNTIF((COALESCE(a.ANNUITY,0)+COALESCE(a.LUMPSUM,0))<>0) OVER (PARTITION BY CARRIERREFERENCE, AYEAR, AQUARTER)) QTEST,
--ABOVE 3 ROWS will be controlled and deleted
            
            COALESCE(a.ESCALATIONPERCENTAGE, 0) ESCALATION_PCT,--new field--Coordinate with Tihomir
            
            
            CONCAT(AYEAR, AQUARTER) APPEARANCE,  --new field       

           (select VALIDFROM from uat_geb_dwh_eu_awr.dim_dummy) VALIDFROM, --added this as it is standard in all tables
            (select VALIDTILL from uat_geb_dwh_eu_awr.dim_dummy) VALIDTILL,  --added this as it is standard in all tables
            max( a.CREATED_ON) CREATED_ON -- the selection of the new records is done based on this created_on
                               -- whereter it should be max() -> to be confirmed/checked later 


            FROM  `geb-dwh-test.uat_geb_dwh_eu_awr.dim_portfolio` portfolio
            LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_awr.fact_claimdetails` as a ON a.PORTDWHID=portfolio.PORTDWHID and portfolio.PORTTYPECD ='REINS' and portfolio.AQUARTER != '0' and portfolio.AQUARTER!='0 or 4 ??' --added filter  for reinsurance
            LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_awr.dim_coverage` cov ON a.COVERDWHID=cov.COVERDWHID 
            LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_awr.dim_contract` as contract ON cov.CONTRACTDWHID =contract.CONTRACTDWHID
            LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_awr.dim_framework` as framework ON contract.FRAMEDWHID=framework.FRAMEDWHID
            LEFT JOIN  `geb-dwh-test.uat_geb_dwh_eu_awr.dim_client_lc` AS clientlc ON framework.CLIENTCIEDWHID=clientlc.LC_CIEDWHID
            LEFT JOIN  `geb-dwh-test.uat_geb_dwh_eu_awr.dim_company_li` AS companyli ON framework.PROVIDERCIEDWHID=companyli.LI_CIEDWHID 
            LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_awr.dim_includingtype`  inctype ON cov.INCLUDINGTYPEDWHID=inctype.INCLUDINGTYPEDWHID 
            LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_awr.dim_covertype` covtype ON cov.COVERTYPEDWHID=covtype.COVERTYPEDWHID
            LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_awr.dim_covergroup` covgroup ON covtype.COVERGRDWHID=covgroup.COVERGRDWHID
            LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_awr.dim_lineofrisk` lineofrisk ON covgroup.LINEOFRISKDWHID=lineofrisk.LINEOFRISKDWHID
            LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_awr.dim_currency` cur ON a.CURRENCYDWHID=cur.CURRENCYDWHID            
            LEFT JOIN  `geb-dwh-test.uat_geb_dwh_eu_awr.dim_country` AS country ON companyli.CNTRDWHID=country.CNTRDWHID
            LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_awr.dim_client_hist` AS clienthist ON clientlc.MH_CIEDWHID=clienthist.MH_CIEDWHID AND portfolio.EXPYEAR=clienthist.EXPYEAR-- Confirmed
            LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_awr.dim_client_role` AS clientrole ON clienthist.CLIENTROLEDWHID=clientrole.CLIENTROLEDWHID


            -- WHERE /*clientrole.CLIENTROLEDWHID IS NOT NULL AND*/ a.CREATED_ON >
            -- case when (select max(dp_start) from `geb-dwh-test.uat_geb_met_eu.meta_dp_log`
            -- where dp_end is not null and dp_name = 'Fact_Actuary') is null
            -- then TIMESTAMP('1999-01-01 00:00:01.000000 UTC')
            -- else (select max(dp_start) from `geb-dwh-test.uat_geb_met_eu.meta_dp_log`
            -- where dp_end is not null and dp_name = 'Fact_Actuary')  end


            GROUP BY country.CNTRNAME,companyli.SHORTNAME,clientlc.LC_CIELEGALNAME,LOCALCD,PORTTYPECD,INCLUDINGTYPECD,clientrole.CLIENTROLELABEL,COVERTYPELABEL,cov.COVERLOCCD,lineofrisk.LINEOFRISKLABEL,CARRIERREFERENCE,GENDER,
                     a.CLAIMDATE, a.LASTPAYMENTDATE, a.INSUREDBIRTHDATE,a.BENEFITSTARTDATE, a.BENEFITENDDATE,currencylabel,portname,ayear,aquarter,portfolio.expyear,a.ANNUITY,a.LUMPSUM,
                     a.BEGINRESERVEAMNT,a.ENDRESERVEAMNT,a.ANNUALBENEFITAMNT, a.ESCALATIONPERCENTAGE/*, a.CLAIMDWHID*/

-- ORDER BY LOCALINSURER --Resources exceeded during query execution: Not enough resources for query planning - too many subqueries or query is too complex.
             ) 


SELECT *,
CASE  
               WHEN cl1.CLAIMID_1 = fa.SELECTED_CLAIM_ID THEN cl1.KEEP_CLAIM
               WHEN cl2.CLAIMID_2 = fa.SELECTED_CLAIM_ID THEN cl2.KEEP_CLAIM
               WHEN cl3.CLAIMID_3 = fa.SELECTED_CLAIM_ID THEN cl3.KEEP_CLAIM
               WHEN cl4.CLAIMID_4 = fa.SELECTED_CLAIM_ID THEN cl4.KEEP_CLAIM
               ELSE 'n/a'
               END as KEEP_CLAIM,
                 --new field --each year, how to get, business logic expected.
            --'N/A' AS KEEP_CLAIM,
            

FROM fa
LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_act.keep_claim_w_li_dynamic_v1` cl1
ON fa.SELECTED_CLAIM_ID=cl1.CLAIMID_1
LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_act.keep_claim_w_li_dynamic_2` cl2
ON fa.SELECTED_CLAIM_ID=cl2.CLAIMID_2
LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_act.keep_claim_w_li_dynamic_3` cl3
ON fa.SELECTED_CLAIM_ID=cl3.CLAIMID_3
LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_act.keep_claim_w_li_dynamic_4` cl4
ON fa.SELECTED_CLAIM_ID=cl4.CLAIMID_4