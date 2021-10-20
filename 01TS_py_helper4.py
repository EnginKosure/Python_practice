from google.cloud import bigquery
import datetime as dt
import pandas as pd
from time import sleep
from google.api_core import retry
from google.api_core import exceptions

# GLOBAL variables
# Define retry parameter
# client = bigquery.Client()
# @retry.Retry(if_exception_type(exceptions.NotFound))
# def check_if_exists():
#     return isinstance(exceptions.NotFound)

# is_available = check_if_exists()


my_retry = retry.Retry(predicate=isinstance("404 Not found", exceptions.NotFound),
                       initial=1.0, maximum=60.0, multiplier=2.0, deadline=120.0)
# Example usage is below
# result = client_ex.some_method(retry=my_retry)


# QUERY
# creates querries for prophet input file creation using helper table for filtering
def create_prophet_input_files(li, rby, q, cc, tn):
    project = "geb-dwh-test"
    dataset_id = "uat_geb_dwh_eu_act"
    source_table = "prophet_input"
    return f"""
            CREATE OR REPLACE TABLE `{tn}` AS
            SELECT * FROM `{project}.{dataset_id}.{source_table}`
            WHERE LOCALINSURER =@li AND BALANCE_YEAR=@rby AND QUARTER=@q AND COVER_CODE=@cc;
         """

# QUERY EXECUTER
# executes create_prophet_input_files function using bigquery client


def create_tables(helper_tn):
    client_tn = bigquery.Client()
    project = "geb-dwh-test"
    dataset_id = "uat_geb_dwh_eu_act"
    table_names = []

    dataset_ref = bigquery.DatasetReference(project, dataset_id)
    table_ref = dataset_ref.table(helper_tn)
    table = client_tn.get_table(table_ref, retry=my_retry)
    df = client_tn.list_rows(table).to_dataframe()
    # print(df.iloc[0][1])
    if len(df) == 0:
        print("no records available for this quarter")
        exit()
    # create table names
    for j in range(0, len(df)):
        ds_body = 'geb-dwh-test.uat_geb_dwh_eu_act'
        full_table_name = f'{ds_body}.{df.iloc[j][1][:3]}by{int(df.iloc[j][2])}q{df.iloc[j][3]}{df.iloc[j][4].lower()}'

        # ds_body+df.iloc[j][1]+df.iloc[j][2]+df.iloc[j][3]+df.iloc[j][4]
        table_names.append(full_table_name)
    print("total records for this export: ", len(table_names))
    # print(table_names[0])

    for j in range(0, len(df)):
        # for j in range(0,1):
        li = df.iloc[j][0]
        rby = int(df.iloc[j][2])
        q = df.iloc[j][3]
        cc = df.iloc[j][4]
        tn = table_names[j]
        print(j+1, "table name ", tn)
        client_ex = bigquery.Client()
        query_ex = create_prophet_input_files(li, rby, q, cc, tn)
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("li", "STRING", f'{li}'),
                bigquery.ScalarQueryParameter("rby", "NUMERIC", f'{rby}'),
                bigquery.ScalarQueryParameter("q", "STRING", f'{q}'),
                bigquery.ScalarQueryParameter("cc", "STRING", f'{cc}'),
                bigquery.ScalarQueryParameter("tn", "STRING", f'{tn}'),
            ]
        )
        client_ex.query(query_ex, job_config=job_config)

        # EXPORT
        bucket_name = 'geb-dwh-tst-bck-novus-europe-west1'
        table_id = tn[32:]  # .lower()

        destination_uri = f"gs://{bucket_name}/{table_id}.csv"
        table_ref = dataset_ref.table(table_id)

        # DatasetReference('geb-dwh-test', 'uat_geb_dwh_eu_act')
        print('dataset_ref', dataset_ref)
        # geb-dwh-test.uat_geb_dwh_eu_act.GH7by2020q4wp
        print('TABRERF', table_ref)
        # gs://geb-dwh-tst-bck-novus-europe-west1/GH7by2020q4wp.csv
        print('destination_uri', destination_uri)

        # wait 2 sec. for table creation, then trigger extract
        sleep(2)
        extract_job = client_ex.extract_table(
            table_ref,
            destination_uri,
            # Location must match that of the source table.
            location="EU",
            retry=my_retry,
            # timeout=2.0
        )  # API request

        extract_job.result()  # Waits for job to complete.

        print("Exported {}:{}.{} to {}".format(
            project, dataset_id, table_id, destination_uri))

        # DELETE AFTER EXPORT
        # wait 1 sec. for table export, then trigger extract
        # sleep(2)
        print('Executed till delete phase ', table_ref, ' will be deleted')
        client_ex.delete_table(table_ref, retry=my_retry)  # API request
        print('Table {}:{} deleted.'.format(dataset_id, table_id))

# QUERY CREATOR
# creates the querry for helper table for latest quarter export


def create_prophet_input_export_helper_latest_quarter(rby, q, tn):
    project = "geb-dwh-test"
    dataset_id = "uat_geb_dwh_eu_act"
    source_table = "prophet_input"
    return f"""
            CREATE OR REPLACE TABLE `{tn}` AS
            SELECT DISTINCT LOCALINSURER,COMPANY_CODE,BALANCE_YEAR,QUARTER,COVER_CODE FROM
            `{project}.{dataset_id}.{source_table}`
            WHERE BALANCE_YEAR=@rby AND QUARTER=@q
            ORDER BY LOCALINSURER,BALANCE_YEAR,QUARTER,COVER_CODE;
         """


# QUERY CREATOR
# creates the query for helper table for full export
def create_prophet_input_full_export_helper(tn):
    return f"""
            CREATE OR REPLACE TABLE `{tn}` AS
            SELECT DISTINCT * FROM `geb-dwh-test.uat_geb_dwh_eu_act.source_sorted_prophet_rows_export_helper`
            ORDER BY LOCALINSURER,BALANCE_YEAR,QUARTER,COVER_CODE;
         """

# takes the user input for options: full export or latest quarter


def user_input():
    export_type = input(
        "\nOPTION-1:For full export (including all quarters), press F; \nOPTION-2:For only latest quarter, press L;\nOPTION-3:For manual selection, press M;\n")
    return export_type

# calculates and returns previous quarter and its year


def previous_quarter(ref):
    quarter = (ref.month - 1) // 3
    prev_quarter = (quarter - 1) % 4
    pq = pd.Timestamp(dt.datetime(ref.year if quarter >
                                  0 else ref.year-1, prev_quarter*3+1, 1)).quarter

    yy = pd.Timestamp(dt.datetime(ref.year if quarter >
                                  0 else ref.year-1, prev_quarter*3+1, 1)).year
    return yy, pq

# MAIN EXECUTER
# main function that executes all in a flow


def export_prophet():
    export_type = user_input()
    # The line below will be opened for production, currently open one is for testing.
    x = previous_quarter(dt.date.today())
    # x=previous_quarter(dt.date(2021,1,31)) # This line is for testing
    if export_type.lower() == 'f':
        # create the export helper table for full export
        tn = "geb-dwh-test.uat_geb_dwh_eu_act.sorted_prophet_rows_full_export_helper"
        tns = "sorted_prophet_rows_full_export_helper"
        client_f = bigquery.Client()
        query_f = create_prophet_input_full_export_helper(tn)
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("tn", "STRING", f'{tn}'),
            ]
        )
        client_f.query(query_f, job_config=job_config)

        # wait 2 sec. for table creation, then trigger table name creation function
        sleep(2)
        create_tables(tns)

    if export_type.lower() == 'l':
        current_yy, current_q = x
        print(current_yy, current_q)

        # Export helper table creation for latest quarters
        rby = int(current_yy)
        q = str(current_q)
        tn = "geb-dwh-test.uat_geb_dwh_eu_act.sorted_prophet_rows_latest_quarters"
        tns = "sorted_prophet_rows_latest_quarters"
        client_l = bigquery.Client()
        query_l = create_prophet_input_export_helper_latest_quarter(rby, q, tn)
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("rby", "NUMERIC", f'{rby}'),
                bigquery.ScalarQueryParameter("q", "STRING", f'{q}'),
                bigquery.ScalarQueryParameter("tn", "STRING", f'{tn}'),
            ]
        )
        client_l.query(query_l, job_config=job_config)

        # wait 2 sec. for table creation, then trigger table name creation function
        sleep(2)
        create_tables(tns)

    if export_type.lower() == 'm':
        current_yy = input("Provide the year for the reporting:\n")
        current_q = input("Provide the quarter:\n")
        print(current_yy, current_q)

        # Export helper table creation for latest quarters
        rby = int(current_yy)
        q = str(current_q)
        tn = "geb-dwh-test.uat_geb_dwh_eu_act.sorted_prophet_rows_manually_selected_quarter"
        tns = "sorted_prophet_rows_manually_selected_quarter"
        client_l = bigquery.Client()
        query_l = create_prophet_input_export_helper_latest_quarter(rby, q, tn)
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("rby", "NUMERIC", f'{rby}'),
                bigquery.ScalarQueryParameter("q", "STRING", f'{q}'),
                bigquery.ScalarQueryParameter("tn", "STRING", f'{tn}'),
            ]
        )
        client_l.query(query_l, job_config=job_config)

        # wait 2 sec. for table creation, then trigger table name creation function
        sleep(2)
        create_tables(tns)


export_prophet()
