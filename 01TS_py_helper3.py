from google.cloud import bigquery
import datetime as dt
import pandas as pd
from time import sleep

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


# executes create_prophet_input_files function using bigquery client
def create_tables(helper_tn):
    client = bigquery.Client()
    project = "geb-dwh-test"
    dataset_id = "uat_geb_dwh_eu_act"
    table_names = []

    dataset_ref = bigquery.DatasetReference(project, dataset_id)
    table_ref = dataset_ref.table(helper_tn)
    table = client.get_table(table_ref)
    df = client.list_rows(table).to_dataframe()
    # print(df.iloc[0][1])
    for j in range(0, len(df)):
        ds_body = 'geb-dwh-test.uat_geb_dwh_eu_act'
        full_table_name = f'{ds_body}.{df.iloc[j][1][:3]}by{int(df.iloc[j][2])}q{df.iloc[j][3]}{df.iloc[j][4].lower()}'

        # ds_body+df.iloc[j][1]+df.iloc[j][2]+df.iloc[j][3]+df.iloc[j][4]
        table_names.append(full_table_name)
    print(table_names)
    # print(table_names[0])

    # for j in range(0,len(df)):
    for j in range(0, 2):
        li = df.iloc[j][0]
        rby = int(df.iloc[j][2])
        q = df.iloc[j][3]
        cc = df.iloc[j][4]
        tn = table_names[j]
        print(tn, "xxxx")
        client = bigquery.Client()
        query = create_prophet_input_files(li, rby, q, cc, tn)
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("li", "STRING", f'{li}'),
                bigquery.ScalarQueryParameter("rby", "NUMERIC", f'{rby}'),
                bigquery.ScalarQueryParameter("q", "STRING", f'{q}'),
                bigquery.ScalarQueryParameter("cc", "STRING", f'{cc}'),
                bigquery.ScalarQueryParameter("tn", "STRING", f'{tn}'),
            ]
        )
        client.query(query, job_config=job_config)

        # bucket_name = 'geb-dwh-tst-bck-novus-europe-west1'
        # table_id = tn#.lower()

        # destination_uri = f"gs://{bucket_name}/{table_id}.csv"
        # table_ref = dataset_ref.table(table_id)

        # extract_job = client.extract_table(
        #         table_ref,
        #         destination_uri,
        #         # Location must match that of the source table.
        #         location="europe-west1",
        #     )  # API request
        # extract_job.result()  # Waits for job to complete.

        # print( "Exported {}:{}.{} to {}".format(project, dataset_id, table_id, destination_uri))


# creates the querry for helper table for latest quarter export
def create_prophet_input_export_helper_latest_quarter(rby, q, tn):
    project = "geb-dwh-test"
    dataset_id = "uat_geb_dwh_eu_act"
    source_table = "prophet_input"
    return f"""
            CREATE OR REPLACE TABLE `{tn}` AS
            SELECT LOCALINSURER,COMPANY_CODE,BALANCE_YEAR,QUARTER,COVER_CODE FROM
            `{project}.{dataset_id}.{source_table}`
            WHERE BALANCE_YEAR=@rby AND QUARTER=@q
            ORDER BY LOCALINSURER,BALANCE_YEAR,QUARTER,COVER_CODE;
         """

# creates the query for helper table for full export


def create_prophet_input_full_export_helper(tn):
    return f"""
            CREATE OR REPLACE TABLE `{tn}` AS
            SELECT * FROM `geb-dwh-test.uat_geb_dwh_eu_act.source_sorted_prophet_rows_export_helper`;
         """

# takes the user input for options: full export or latest quarter


def user_input():
    export_type = input(
        "For full export (including all quarters), press F; \nFor only latest quarter, press L\n")
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


# main function that executes all in a flow
def export_prophet():
    export_type = user_input()
    # x=previous_quarter(dt.date.today())
    x = previous_quarter(dt.date(2015, 1, 31))
    if export_type == 'F' or 'f':
        # create the export helper table for full export
        tn = "geb-dwh-test.uat_geb_dwh_eu_act.sorted_prophet_rows_full_export_helper"
        tns = "sorted_prophet_rows_full_export_helper"
        client = bigquery.Client()
        query = create_prophet_input_full_export_helper(tn)
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("tn", "STRING", f'{tn}'),
            ]
        )
        client.query(query, job_config=job_config)

        # wait 2 sec. for table creation, then trigger table name creation function
        sleep(2)
        create_tables(tns)

    if export_type == 'L' or 'l':
        current_yy, current_q = x
        print(current_yy, current_q)

        # Export helper table creation for latest quarters
        rby = int(current_yy)
        q = str(current_q)
        tn = "geb-dwh-test.uat_geb_dwh_eu_act.sorted_prophet_rows_latest_quarters"
        tns = "sorted_prophet_rows_latest_quarters"
        client = bigquery.Client()
        query = create_prophet_input_export_helper_latest_quarter(rby, q, tn)
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("rby", "NUMERIC", f'{rby}'),
                bigquery.ScalarQueryParameter("q", "STRING", f'{q}'),
                bigquery.ScalarQueryParameter("tn", "STRING", f'{tn}'),
            ]
        )
        client.query(query, job_config=job_config)

        # wait 2 sec. for table creation, then trigger table name creation function
        sleep(2)
        create_tables(tns)


export_prophet()
