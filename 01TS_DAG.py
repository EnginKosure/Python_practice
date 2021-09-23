from datetime import timedelta
from datetime import date

import datetime
import json

from airflow import models

from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from airflow.contrib.operators import bigquery_operator
from airflow.operators import python_operator


from google.cloud import bigquery


default_args = {
    # The start_date describes when a DAG is valid / can be run. Set this to a
    # fixed point in time rather than dynamically, since it is evaluated every
    # time a DAG is parsed. See:
    # https://airflow.apache.org/faq.html#what-s-the-deal-with-start-date
    # 'start_date': YESTERDAY,
    # , tzinfo=local_tz),  #-> adding timezone
    'start_date': datetime.datetime(2020, 11, 10),
    'owner': 'GEB'
}


dataset_meta = 'uat_geb_met_eu'
dataset_sta = 'uat_geb_dwh_eu_act'
dataset_dwh = 'uat_geb_dwh_eu_act'

source_fa_staging = 'geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary_staging'
source_fa_final = 'geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary_final'
source_keep_claim_pct = 'geb-dwh-test.uat_geb_dwh_eu_act.source_keep_claim_pct_all'
claim_ids = ['CLAIMID_1', 'CLAIMID_2', 'CLAIMID_3', 'CLAIMID_4']

with models.DAG(
    'Actuary_test_DAG',
    default_args=default_args,
    description='for_testing',
    schedule_interval=None,
) as Areaman_as_dag:

    #
    t00 = BashOperator(task_id='Start_DWH_Actuary_loads',
                       bash_command=f"python3 /home/airflow/gcs/dags/pipelines_control/DWH_Start.py --pipeline DWH_Actuary_Loads --dataset_meta {dataset_meta} ",
                       dag=Areaman_as_dag)

    t0 = BashOperator(task_id='Start_Actuary_Job',
                      bash_command=f"python3 /home/airflow/gcs/dags/pipelines_control/Job_Start.py --pipeline Job_Actuary_Start --dataset_meta {dataset_meta} ",
                      dag=Areaman_as_dag)

    t9 = BashOperator(task_id='End_Actuary_Job',
                      bash_command=f"python3 /home/airflow/gcs/dags/pipelines_control/Job_End.py --pipeline Job_Actuary_Start --dataset_meta {dataset_meta} ",
                      dag=Areaman_as_dag)

    t99 = BashOperator(task_id='End_DWH_Actuary_loads',
                       bash_command=f"python3 /home/airflow/gcs/dags/pipelines_control/DWH_End.py --pipeline DWH_Actuary_Loads --dataset_meta {dataset_meta} ",
                       dag=Areaman_as_dag)

    #   Below, to add KEEP_CLAIM over fact_actuary_staging table--> The final name will be fact_actuary_final
    t01 = BashOperator(task_id='Run_Fact_Actuary_Prestaging',
                       bash_command=f"python3 /home/airflow/gcs/dags/dp_exec/DIM_EXEC2.py --pipeline  Fact_Actuary_Prestaging --dataset_meta {dataset_meta}",
                       dag=Areaman_as_dag)

    #   Below, to add KEEP_CLAIM over fact_actuary_staging table--> The final name will be fact_actuary_final
    t02 = BashOperator(task_id='Run_Fact_Actuary_Staging',
                       bash_command=f"python3 /home/airflow/gcs/dags/dp_exec/DIM_EXEC2.py --pipeline  Fact_Actuary_Staging --dataset_meta {dataset_meta}",
                       dag=Areaman_as_dag)

    t1 = BashOperator(task_id='Run_Fact_Actuary',
                      bash_command=f"python3 /home/airflow/gcs/dags/dp_exec/DIM_EXEC2.py --pipeline  Fact_Actuary --dataset_meta {dataset_meta}",
                      dag=Areaman_as_dag)

    #   To produce DB_Run_Off_Fields table
    t3 = BashOperator(task_id='Run_DB_Run_Off',
                      bash_command=f"python3 /home/airflow/gcs/dags/dp_exec/DIM_EXEC2.py --pipeline  DB_Run_Off --dataset_meta {dataset_meta}",
                      dag=Areaman_as_dag)

    t100 = bigquery_operator.BigQueryOperator(
        task_id='Fact_Actuary_Prestaging',
        sql=f"""
        CREATE TABLE `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary_w_o_null` AS SELECT * FROM `geb-dwh-test.uat_geb_dwh_eu_act.source_fact_actuary_staging`
            WHERE LOCALINSURER IS NOT NULL
            ORDER BY LOCALINSURER,CARRIERREFERENCE, RE_BALANCEYEARPTF, RE_QUARTERPTF
        """,
        use_legacy_sql=False,
        dag=Areaman_as_dag
    )

    t00 >> t0 >> t1 >> t100 >> t9 >> t99
    # t00 >> t0 >> t01 >> t02 >> t1 >>
