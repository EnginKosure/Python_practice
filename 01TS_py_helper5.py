from google.cloud import bigquery
import datetime as dt
import pandas as pd
from time import sleep
from google.api_core import retry
from google.api_core import exceptions


# CREATE TABLE NAMES
def create_table_names(project, dataset_id, helper_tn):
    client_tn = bigquery.Client()
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
        full_table_name = f'{ds_body}.{df.iloc[j][2]}'

        table_names.append(full_table_name)
    return table_names, df, dataset_ref

# QUERY CREATOR-1
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


# QUERY CREATOR-2
# creates the helper source view index for ReSQ table creation phase
def reSQ_helper_view_index_query(tn, search_term, project, dataset_id):
    source_table = "INFORMATION_SCHEMA.VIEWS"
    return f"""
           CREATE OR REPLACE TABLE `{tn}` AS
           SELECT * EXCEPT(check_option)
            FROM `{project}.{dataset_id}.{source_table}`
            WHERE table_name LIKE @search_term ORDER BY table_name;
         """


# HELPER INDEX TABLE CREATOR (Executes QUERY-2: create_ReSQ_helper_view_index)
def generate_helper_index_table(search_term, project, dataset_id, helper_tn):
    # create the export helper index table using info schema of bigquery
    tn = f'{project}.{dataset_id}.{helper_tn}'
    client_f = bigquery.Client()
    query_f = reSQ_helper_view_index_query(
        tn, search_term, project, dataset_id)

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter(
                "search_term", "STRING", f'{search_term}'),
        ]
    )
    client_f.query(query_f, job_config=job_config)
    # wait 3 sec. for helper index table creation so as to table creation function may have it when triggered
    sleep(3)


# HELPER function to check the table names and get confirmation
def confirm(table_names):
    answer = ""
    print(
        f'\nThere will be {len(table_names)} tables exported.\n\nThe source views that will be used are: \n{table_names} \n\nDo you confirm?')
    while answer not in ["y", "n"]:
        answer = input("Please confirm to continue [Y/N]? ").lower()
    return answer == "y"


# TABLE GENERATOR
def generate_tables(df, table_names):
    for j in range(0, len(df)):
        # for j in range(0,1):
        li = df.iloc[j][2][7:]
        tn = table_names[j]
        print("source view name ", j+1, tn)
        client_ex = bigquery.Client()
        query_ex = create_ReSQ_export(li, tn)
        client_ex.query(query_ex)


# TABLE EXPORTER
def export_tables(df, table_names, dataset_ref, project, dataset_id):
    for j in range(0, len(df)):
        bucket_name = 'geb-dwh-tst-bck-novus-europe-west1'
        table_id = table_names[j][39:]  # .lower()
        # print('table_id', table_id)

        destination_uri = f"gs://{bucket_name}/{table_id}.csv"
        table_ref = dataset_ref.table(table_id)

        # print('dataset_ref',dataset_ref) # DatasetReference('geb-dwh-test', 'uat_geb_dwh_eu_act')
        # geb-dwh-test.uat_geb_dwh_eu_act.ReSQ_input_1_non_cumulative_paid_triangels
        print('\nTable reference: ', table_ref)
        # gs://geb-dwh-tst-bck-novus-europe-west1/ReSQ_input_1_non_cumulative_paid_triangels.csv
        print('destination_uri', destination_uri)

        client_ex = bigquery.Client()
        extract_job = client_ex.extract_table(
            table_ref,
            destination_uri,
            # Location must match that of the source table.
            location="EU",
            timeout=5.0
        )  # API request

        extract_job.result()  # Waits for job to complete.

        print("\nExported {}:{}.{} to {}".format(
            project, dataset_id, table_id, destination_uri))


# TABLE DELETOR
def delete_tables(df, table_names, dataset_ref, dataset_id):
    print('\nCLEAN-UP: The export phase has been finished. \nNow the exported tables will be deleted from BigQuery dataset')
    for j in range(len(df)):
        # DELETE AFTER EXPORT
        # wait 1 sec. for table export, then trigger extract
        # sleep(2)
        table_id = table_names[j][39:]  # .lower()
        table_ref = dataset_ref.table(table_id)
        # print('Executed till delete phase ', table_ref, ' will be deleted')
        client_ex = bigquery.Client()
        client_ex.delete_table(table_ref)  # API request
        print('Table {}:{} deleted.'.format(dataset_id, table_id))

# MAIN EXECUTER (main function that executes all in a flow)
# executes table generator, exporter, deletor functions after preparing table names as parameters
# using helper index file created by info schema of bigquery


def export_resq():
    project = "geb-dwh-test"
    dataset_id = "uat_geb_dwh_eu_act"
    bucket_uri = "https://console.cloud.google.com/storage/browser/geb-dwh-tst-bck-novus-europe-west1"
    search_term = '%ReSQ%'
    helper_tn = "resq_source_view_index_as_export_helper"

    # Trigger helper index table generation
    generate_helper_index_table(search_term, project, dataset_id, helper_tn)

    # CREATE TABLE NAMES
    table_names, df, dataset_ref = create_table_names(
        project, dataset_id, helper_tn)

    # show the source views that will be used for table creation and ask for confirmation
    # if confirmed, continue to execution
    if confirm(table_names):
        # GENERATE TABLES
        generate_tables(df, table_names)

        # EXPORT TABLES
        print('\nwait 5 sec. for table creation, then trigger extract\n')
        sleep(5)
        export_tables(df, table_names, dataset_ref, project, dataset_id)

        # DELETE TABLES
        delete_tables(df, table_names, dataset_ref, dataset_id)

        print(f'\nExecuted till the end.\n\ncreate >> export >> delete phases consequently and successfully executed.\
        \nYou can check the bucket following this link--> {bucket_uri} \
        \n\nPlease do not forget to delete these exported files from the bucket after feeding your ReSQ data import pipeline.\n')


export_resq()
