-- =============================================SOURCE_FACT_ACTUARY_PRESTAGING=============================================
-- Author      : in@geb.com, kosure@geb.com
-- Create date : 01-08-2021
-- Description : Provides the prestaging table for staging_fact_actuary, without SELECTED_CLAIM_ID, KEEP_CLAIM, ANNUALIZED_PAID
-- Input       : `geb-dwh-test.uat_geb_dwh_eu_awr.dim_portfolio`,&__fact_claimdetails,&__dim_coverage, &__dim_contract, &__dim_framework, &__dim_client_lc, &__dim_company_li,
--                &__dim_includingtype, &__dim_covertype, &__dim_covergroup, &__dim_lineofrisk, &__dim_currency, &__dim_country, &__dim_client_hist, &__dim_client_role

-- Output      : fact_actuary_prestaging 
-- Related DAG : actuary_uat_v2.py
-- TODOs       : - COMPANY_CODE will be taken from dim_company_li once RIPARTYCODE is implemented there
-- ========================================================================================================================

(
-- DATE_VALUE_ADJUSTED is not present in the new view to check all commented lines
            SELECT DISTINCT
    STRING_AGG(a.CLAIMDWHID, ' | ') OVER (PARTITION BY  country.CNTRNAME,companyli.SHORTNAME,clientlc.LC_CIELEGALNAME,LOCALCD,PORTTYPECD,INCLUDINGTYPECD,
                     COVERTYPELABEL,cov.COVERLOCCD,lineofrisk.LINEOFRISKLABEL,CARRIERREFERENCE,GENDER,a.CLAIMDATE, a.LASTPAYMENTDATE,
                     a.INSUREDBIRTHDATE,a.BENEFITSTARTDATE, a.BENEFITENDDATE,CURRENCYLABEL,PORTNAME,AYEAR,AQUARTER,portfolio.EXPYEAR,a.ANNUITY,a.LUMPSUM,
                     a.BEGINRESERVEAMNT,a.ENDRESERVEAMNT,a.ANNUALBENEFITAMNT, a.ESCALATIONPERCENTAGE) as CLAIMDWHID, --TBC
    -- portfolio.PORTDWHID,--TBC --6744 unique values
    country.CNTRNAME AS LICOUNTRY,
    companyli.SHORTNAME AS LOCALINSURER,
    TRIM(rivparty.COMPANY_CODE) AS COMPANY_CODE, --To get the 3-letter(alphanumeric) company_codes for prophet_input
    clientlc.LC_CIELEGALNAME AS LOCALCLIENT,
    LOCALCD AS POLICY_NR, --new field
    INCLUDINGTYPECD AS PO_COVER_INCLUDING_TYPE, --new field
    CASE
               WHEN cov.MHLINEOFPRODUCT='POOL' AND inctype.INCLUDINGTYPECD='YES' THEN "Pool"
               WHEN cov.MHLINEOFPRODUCT='CAPTIVE' AND inctype.INCLUDINGTYPECD='YES' THEN "Captive"
               ELSE "Reinsurance Only"
            END AS LINEOFPRODUCT,--new field 
    COVERTYPELABEL AS COVERDESCRIPTION_NEW, --new field
    COVERLOCCD AS COVERCODE_NEW, --new field
    LINEOFRISKLABEL AS PO_LINEOFRISK, --new field
    --INSUREDPERSON, --in v2, canceled.
    CARRIERREFERENCE,
    a.GENDER,--not available for historical
    -- a.CLAIMID PO_CLAIM,--cancelled in v3
    CONCAT(COALESCE(framework.LOCALCD,'#'),'_',COALESCE(cov.COVERLOCCD,'#'),'_',COALESCE(FORMAT_DATE("%d/%m/%Y",CLAIMDATE),'#')) CLAIMID_1, --new field
    CONCAT(COALESCE(framework.LOCALCD,'#'),'_',COALESCE(cov.COVERLOCCD,'#'),'_',COALESCE(INSUREDBIRTHDATE,'#')) CLAIMID_2, --new field, encrypted birthdate--use encrypted
    CONCAT(COALESCE(framework.LOCALCD,'#'),'_',COALESCE(cov.COVERLOCCD,'#'),'_',COALESCE(CARRIERREFERENCE,'#'),'_',COALESCE(FORMAT_DATE("%d/%m/%Y",CLAIMDATE),'#')) CLAIMID_3, --new field
    CONCAT(COALESCE(framework.LOCALCD,'#'),'_',COALESCE(cov.COVERLOCCD,'#'),'_',COALESCE(CARRIERREFERENCE,'#')) CLAIMID_4, --new field
    --SELECTED_CLAIM_ID will be added in source_fact_actuary_staging
    FORMAT_DATE("%d/%m/%Y",a.CLAIMDATE) AS CLAIMDATE,
    FORMAT_DATE("%Y",CLAIMDATE) AS AY_ACCIDENT_YEAR, 
--new field
IF(LASTPAYMENTDATE<DATE'1901-01-01',NULL,LASTPAYMENTDATE)  AS LASTPAYMENTDATE,
-- LASTPAYMENTDATE AS LASTPAYMENTDATE_TEST,--will be removed, just for check if dummy dates are removed
IF(INSUREDBIRTHDATETRUNC<DATE'1901-01-01',NULL,INSUREDBIRTHDATETRUNC)  AS INSUREDBIRTHDATE,
-- INSUREDBIRTHDATETRUNC AS INSUREDBIRTHDATE_TEST,--will be removed, just for check if dummy dates are removed
IF(BENEFITSTARTDATE<DATE'1901-01-01',NULL,BENEFITSTARTDATE)  AS CLAIM_BENEFITBEGDATE,
IF(BENEFITENDDATE<DATE'1901-01-01',NULL,BENEFITENDDATE) AS CLAIM_BENEFITENDDATE,
            CURRENCYLABEL AS LOCALCURRENCY,
            PORTNAME AS RE_PORTFOLIO,
            AYEAR AS RE_BALANCEYEARPTF,
            AQUARTER AS RE_QUARTERPTF,
            CONCAT
(portfolio.AYEAR,0,portfolio.AQUARTER) AS CURRENTQUARTER, --new field
            FORMAT_DATE
("%d/%m/%Y", DATE_SUB
(LAST_DAY
(CAST
(CONCAT
(AYEAR,'-',CAST
(
IF(portfolio.AQUARTER IN ('0', '0 or 4 ??'),'1',portfolio.AQUARTER) AS INT64 )*3,'-15') AS DATE), quarter), INTERVAL 45 DAY)) AS CURRENTDAY,
            ROUND
(DATE_DIFF
(LAST_DAY
(CAST
(CONCAT
(AYEAR,'-',CAST
(
IF(portfolio.AQUARTER IN ('0', '0 or 4 ??'),'1',portfolio.AQUARTER) AS INT64 )*3,'-15') AS DATE), QUARTER), INSUREDBIRTHDATETRUNC,DAY)/365.24,2) AS AGEOFINSURED,--new field,
            -- CASE 
            --    WHEN REGEXP_CONTAINS(INSUREDBIRTHDATE, r'^([0]?[1-9]|[1|2][0-9]|[3][0|1])/([0]?[1-9]|[1][0-2])/([0-9]{4}|[0-9]{2})$') --To catch 15/01/1950 or 1/1/1950 format
            --    -- WHEN REGEXP_CONTAINS(INSUREDBIRTHDATE, r'^[0-9]{2}[/\-][0-9]{2}[/\-][0-9]{4}$') --According the final incoming format of INSUREDBIRTHDATE, code will be adjusted
            --    -- WHEN SAFE.PARSE_DATE("%d/%m/%Y", INSUREDBIRTHDATE) IS NOT NULL OR SAFE_CAST(INSUREDBIRTHDATE AS DATE) IS NOT NULL
            --       THEN DATE_DIFF(LAST_DAY(CAST(CONCAT(AYEAR,'-',CAST(IF(portfolio.AQUARTER IN ('0', '0 or 4 ??'),'1',portfolio.AQUARTER) AS INT64 )*3,'-15') AS DATE), QUARTER), PARSE_DATE("%d/%m/%Y", INSUREDBIRTHDATE),DAY)/365.24 
            --    ELSE DATE_DIFF(LAST_DAY(CAST(CONCAT(AYEAR,'-',CAST(IF(portfolio.AQUARTER IN ('0', '0 or 4 ??'),'1',portfolio.AQUARTER) AS INT64 )*3,'-15') AS DATE), QUARTER), PARSE_DATE("%d/%m/%Y", "1/1/1900"),DAY)/365.24 
            -- END AS AGEOFINSURED,
            
            CASE
               WHEN SAFE_CAST
(SAFE.FORMAT_DATE
("%Y",CLAIMDATE) AS INT64 )>=AYEAR THEN "CY" --GREATER SIGN ADDITION IS FROM FRITZ, 29-10-2021
               WHEN SAFE_CAST
(SAFE.FORMAT_DATE
("%Y",CLAIMDATE) AS INT64)<0 THEN "CY"--2nd
               WHEN SAFE_CAST
(SAFE.FORMAT_DATE
("%Y",CLAIMDATE) AS INT64)<AYEAR THEN "PY"--3rd
               WHEN SAFE_CAST
(SAFE.FORMAT_DATE
("%Y",CLAIMDATE) AS INT64) IS NULL THEN "n.a."
END AS CY_PY,--new field
            portfolio.EXPYEAR AS RE_EXPERIENCEYEARPTF,
            a.ANNUITY,
            a.LUMPSUM,
            COALESCE
(a.ANNUITY,0)+COALESCE
(a.LUMPSUM,0) AS PAID, --new field--coalesce
            a.BEGINRESERVEAMNT AS BEGRES,
            a.ENDRESERVEAMNT AS ENDRES,
            a.ANNUALBENEFITAMNT AS PO_ANNUALBENEFITAMOUNT,
IF(COALESCE(a.ESCALATIONPERCENTAGE, 0)=-1,0,COALESCE
(a.ESCALATIONPERCENTAGE, 0)) AS ESCALATION_PCT,--new field-- The -1 values transformed into 0 (Fritz's input 30/09/2021 - TS_v6)
            CONCAT
(AYEAR, AQUARTER) AS APPEARANCE,
--new field  
-- AYEAR - CAST(FORMAT_DATE("%Y",CLAIMDATE) AS INT64) AS DEVELOPMENT_PERIOD_ON_AY,--ADDED after the request of Fritz on 07 OCTOBER 2021 --TBC, removed on TS_v6, so removed from here also
-- DATE_DIFF(DATE_SUB(LAST_DAY(CAST(CONCAT(AYEAR,'-',CAST(IF(portfolio.AQUARTER IN ('0', '0 or 4 ??'),'1',portfolio.AQUARTER) AS INT64 )*3,'-15') AS DATE), quarter), INTERVAL 45 DAY), a.CLAIMDATE, QUARTER) AS DEVELOPMENT_PERIOD_IN_QUARTERS, --(Fritz's input 07/10/2021 - TS_v6)--Removed with v8

(select VALIDFROM
from uat_geb_dwh_eu_awr.dim_dummy)
VALIDFROM,
--added this as it is standard in all tables
(select VALIDTILL
from uat_geb_dwh_eu_awr.dim_dummy)
VALIDTILL,  --added this as it is standard in all tables
            max
( a.CREATED_ON) CREATED_ON -- the selection of the new records is done based on this created_on
                               -- whether it should be max() -> to be confirmed/checked later 


            -- FROM  `geb-dwh-test.uat_geb_dwh_eu_awr.dim_portfolio` portfolio --old version, 38.708 nulls (mainly from VIRA/VIRI)
            --Item_034: Ensure all the data from the CM is removed==> with WHERE PORTTYPECD ='REINS'statement, we excluded all CM data
            FROM
( SELECT *
FROM `geb-dwh-test.uat_geb_dwh_eu_awr.dim_portfolio`
WHERE PORTTYPECD ='REINS' and AQUARTER != '0')
portfolio --Tihomir's suggestion, 3232 nulls ==>2633 nulls after AQUARTER condition
            --Below, AND MOL_CLAIMID IS NOT NULL part is TBC, with that addition, there is no more null values. Without that, 169 null values (CARRIERREFERENCE gives also the same result)
            --Wait till Tihomir's confirmation to open MOL_CLAIMID IS NOT NULL part 25-10-2021 (--Confirmed by Fritz)
            JOIN `geb-dwh-test.uat_geb_dwh_eu_awr.fact_claimdetails` as a ON a.PORTDWHID=portfolio.PORTDWHID /*AND MOL_CLAIMID IS NOT NULL /*and portfolio.PORTTYPECD ='REINS'  and portfolio.AQUARTER != '0'*/ --and portfolio.AQUARTER!='0 or 4 ??' --to ensure all the data from the CM is removed, INNER JOIN
            LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_awr.dim_coverage`  cov ON a.COVERDWHID=cov.COVERDWHID AND COVERLOCCD NOT IN('SRT','SLRT')--excluded after TS update 07/10/2021
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
            
            -- cleintrole is being removed from client_hist, new place to get  MHLINEOFPRODUCT is dim_coverage. See line 29.
            -- LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_awr.dim_client_hist` AS clienthist ON clientlc.MH_CIEDWHID=clienthist.MH_CIEDWHID AND portfolio.EXPYEAR=clienthist.EXPYEAR-- Confirmed
            -- LEFT JOIN `geb-dwh-test.uat_geb_dwh_eu_awr.dim_client_role` AS clientrole ON clienthist.CLIENTROLEDWHID=clientrole.CLIENTROLEDWHID
            
            -- TODO--will be taken from dim_company_li, after RIPARTYCODE is implemented there
            LEFT JOIN `geb-dwh-test.uat_geb_inb_eu_novus.RIVPARTY` AS rivparty ON companyli.RIPARTYID=rivparty.PARTY_ID --To get the 3-letter company_codes for prophet_input 

            WHERE AYEAR >= 2012 --TBC

            --Below 6 lines may be uncommented if in the future this source view decided to be run using DIM_EXEC2.py script.
            -- WHERE a.CREATED_ON >
            -- case when (select max(dp_start) from `geb-dwh-test.uat_geb_met_eu.meta_dp_log`
            -- where dp_end is not null and dp_name = 'Fact_Actuary') is null
            -- then TIMESTAMP('1999-01-01 00:00:01.000000 UTC')
            -- else (select max(dp_start) from `geb-dwh-test.uat_geb_met_eu.meta_dp_log`
            -- where dp_end is not null and dp_name = 'Fact_Actuary')  end


            GROUP BY country.CNTRNAME,companyli.SHORTNAME,clientlc.LC_CIELEGALNAME,LOCALCD,PORTTYPECD,INCLUDINGTYPECD,COVERTYPELABEL,cov.COVERLOCCD,lineofrisk.LINEOFRISKLABEL,CARRIERREFERENCE,GENDER,
                     a.CLAIMDATE, a.LASTPAYMENTDATE, a.INSUREDBIRTHDATE,a.BENEFITSTARTDATE, a.BENEFITENDDATE,currencylabel,portname,ayear,aquarter,portfolio.expyear,a.ANNUITY,a.LUMPSUM,
                     a.BEGINRESERVEAMNT,a.ENDRESERVEAMNT,a.ANNUALBENEFITAMNT, a.ESCALATIONPERCENTAGE, a.CLAIMDWHID, INSUREDBIRTHDATETRUNC, portfolio.PORTDWHID,rivparty.COMPANY_CODE,MHLINEOFPRODUCT
) 
