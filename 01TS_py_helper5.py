from google.cloud import bigquery
import datetime as dt
import pandas as pd
from time import sleep
from google.api_core import retry
from google.api_core import exceptions


# QUERY EXECUTER
# executes create_prophet_input_files function using bigquery client

def create_tables(helper_tn):
    client_tn = bigquery.Client()
    project = "geb-dwh-test"
    dataset_id = "uat_geb_dwh_eu_act"
    table_names = []

    dataset_ref = bigquery.DatasetReference(project, dataset_id)
    table_ref = dataset_ref.table(helper_tn)
    table = client_tn.get_table(table_ref)
    df = client_tn.list_rows(table).to_dataframe()
    # print(df.iloc[0][2])
    if len(df) == 0:
        print("no records available")
        exit()
    # create table names
    for j in range(0, len(df)):
        ds_body = 'geb-dwh-test.uat_geb_dwh_eu_act'
        # full_table_name=f'{ds_body}.{df.iloc[j][1][:3]}by{int(df.iloc[j][2])}q{df.iloc[j][3]}{df.iloc[j][4].lower()}'
        full_table_name = f'{ds_body}.{df.iloc[j][2]}'

        table_names.append(full_table_name)
    # print("total records for this export: ",len(table_names))
    # print(table_names)

    if confirm(table_names):
        for j in range(0, len(df)):
            # for j in range(0,1):
            li = df.iloc[j][2][7:]
            tn = table_names[j]
            print(j+1, "table name ", tn)
            client_ex = bigquery.Client()
            query_ex = create_ReSQ_export(li, tn)
            job_config = bigquery.QueryJobConfig(
                query_parameters=[
                    bigquery.ScalarQueryParameter("li", "STRING", f'{li}'),
                    bigquery.ScalarQueryParameter("tn", "STRING", f'{tn}'),
                ]
            )
            client_ex.query(query_ex, job_config=job_config)

        # EXPORT
        print('wait 5 sec. for table creation, then trigger extract')
        sleep(5)
        for j in range(0, len(df)):
            bucket_name = 'geb-dwh-tst-bck-novus-europe-west1'
            table_id = table_names[j][39:]  # .lower()
            print('table_id', table_id)

            destination_uri = f"gs://{bucket_name}/{table_id}.csv"
            table_ref = dataset_ref.table(table_id)

            # DatasetReference('geb-dwh-test', 'uat_geb_dwh_eu_act')
            print('dataset_ref', dataset_ref)
            # geb-dwh-test.uat_geb_dwh_eu_act.ReSQ_input_1_non_cumulative_paid_triangels
            print('TABRERF', table_ref)
            # gs://geb-dwh-tst-bck-novus-europe-west1/ReSQ_input_1_non_cumulative_paid_triangels.csv
            print('destination_uri', destination_uri)

            extract_job = client_ex.extract_table(
                table_ref,
                destination_uri,
                # Location must match that of the source table.
                location="EU",
                timeout=5.0
            )  # API request

            extract_job.result()  # Waits for job to complete.

        print("Exported {}:{}.{} to {}".format(
            project, dataset_id, table_id, destination_uri))

        for j in range(len(df)):
            # DELETE AFTER EXPORT
            # wait 1 sec. for table export, then trigger extract
            # sleep(2)
            table_id = table_names[j][39:]  # .lower()
            table_ref = dataset_ref.table(table_id)
            print('Executed till delete phase ', table_ref, ' will be deleted')
            client_ex.delete_table(table_ref)  # API request
            print('Table {}:{} deleted.'.format(dataset_id, table_id))

# QUERY CREATOR
# creates the export table for ReSQ
# CREATE TABLE `geb-dwh-test.uat_geb_dwh_eu_act.ReSQ_input_1_non_cumulative_paid_triangels`
# AS SELECT * FROM `geb-dwh-test.uat_geb_dwh_eu_act.source_ReSQ_input_1_non_cumulative_paid_triangels`


def create_ReSQ_export(li, tn):
    project = "geb-dwh-test"
    dataset_id = "uat_geb_dwh_eu_act"
    # source_table=tn
    # ctn=tn[39:]
    return f"""
            CREATE OR REPLACE TABLE `{project}.{dataset_id}.{li}` AS
            SELECT * FROM
            `{tn}`;
         """


# QUERY CREATOR
# creates the helper source view index for ReSQ table creation phase
def create_ReSQ_helper_view_index(tn):
    project = "geb-dwh-test"
    dataset_id = "uat_geb_dwh_eu_act"
    source_table = "INFORMATION_SCHEMA.VIEWS"
    return f"""
           CREATE OR REPLACE TABLE `{tn}` AS
           SELECT * EXCEPT(check_option)
            FROM `{project}.{dataset_id}.{source_table}`
            WHERE table_name LIKE '%ReSQ%'
         """


# HELPER to confirm
def confirm(table_names):
    answer = ""
    print(
        f'There will be {len(table_names)} tables exported.\nThe source views to be used are: {table_names} Do you confirm?')
    while answer not in ["y", "n"]:
        answer = input("Please confirm to continue [Y/N]? ").lower()
    return answer == "y"


# MAIN EXECUTER
# main function that executes all in a flow
def export_resq():
    # create the export helper
    tn = "geb-dwh-test.uat_geb_dwh_eu_act.resq_source_view_index_as_export_helper"
    tns = "resq_source_view_index_as_export_helper"
    client_f = bigquery.Client()
    query_f = create_ReSQ_helper_view_index(tn)

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("tn", "STRING", f'{tn}'),
        ]
    )
# Creation of helper_index_file
    client_f.query(query_f, job_config=job_config)

    # wait 2 sec. for table creation, then trigger table name creation function
    sleep(3)
    create_tables(tns)


export_resq()
