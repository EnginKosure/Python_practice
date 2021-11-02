from google.cloud import bigquery
import datetime as dt
import pandas as pd
from time import sleep
from google.api_core import retry
from google.api_core import exceptions

# HELPER TO REIDENTIFIED ENCRYPTED GENDER


def reidentify_with_deterministic(
        project,
        input_str,
        surrogate_type=None,
        key_name=None,
        wrapped_key=None,
):
    """Deidentifies sensitive data in a string using deterministic encryption.
    Args:
        project: The Google Cloud project id to use as a parent resource.
        input_str: The string to deidentify (will be treated as text).
        surrogate_type: The name of the surrogate custom info type to used
            during the encryption process.
        key_name: The name of the Cloud KMS key used to encrypt ('wrap') the
            AES-256 key. Example:
            keyName = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/
            keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME'
        wrapped_key: The encrypted ('wrapped') AES-256 key to use. This key
            should be encrypted using the Cloud KMS key specified by key_name.
    Returns:
        None; the response from the API is printed to the terminal.
    """
    import base64

    # Import the client library
    import google.cloud.dlp

    # Instantiate a client
    dlp = google.cloud.dlp_v2.DlpServiceClient()

    # Convert the project id into a full resource id.
    parent = f"projects/{project}"

    # The wrapped key is base64-encoded, but the library expects a binary
    # string, so decode it here.
    wrapped_key = base64.b64decode(wrapped_key)

    # Construct reidentify Configuration
    reidentify_config = {
        "info_type_transformations": {
            "transformations": [
                {
                    "primitive_transformation": {
                        "crypto_deterministic_config": {
                            "crypto_key": {
                                "kms_wrapped": {
                                    "wrapped_key": wrapped_key,
                                    "crypto_key_name": key_name,
                                }
                            },
                            "surrogate_info_type": {"name": surrogate_type},
                        }
                    }
                }
            ]
        }
    }

    inspect_config = {
        "custom_info_types": [
            {"info_type": {"name": surrogate_type}, "surrogate_type": {}}
        ]
    }

    # Convert string to item
    item = {"value": input_str}

    # Call the API
    response = dlp.reidentify_content(
        request={
            "parent": parent,
            "reidentify_config": reidentify_config,
            "inspect_config": inspect_config,
            "item": item,
        }
    )

    # Print results
    print("Only the response from DLP API call", response.item.value)

    return response.item.value


def get_disitnct_gender_encrypted_values(project, dataset_id, helper_tn="prophet_input_gender_encrypted"):
    client_en = bigquery.Client()
    # project = "geb-dwh-test"
    # dataset_id = "uat_geb_dwh_eu_act"
    sql = """
    SELECT DISTINCT SEX FROM `geb-dwh-test.uat_geb_dwh_eu_act.prophet_input_gender_encrypted` ORDER BY SEX DESC;
    """
    # dataset_ref = bigquery.DatasetReference(project, dataset_id)
    # table_ref = dataset_ref.table(helper_tn)
    # table = client_en.get_table(table_ref, retry=retry_config)
    table = client_en.query(sql)
    table = table.result()
    print("TABLE--DISTINCT QUERY", table)
    df = table.to_dataframe()
    # ['CE_(24):AfkwbapkQwFqtk8Gx42biBhS', 'CE_(24):AbmgbLq4OGncwRPFrV3ZodFN', '', None]
    distinct_values = list(df['SEX'].unique())
    print(distinct_values)
    if len(df) == 0:
        print("no values available")
        exit()

    return distinct_values


def get_original(dist_val):
    enc_dec_dict = {}
    for i in dist_val:
        if i not in (None, ""):
            val = reidentify_with_deterministic('geb-dwh-test', i, surrogate_type="CE_", key_name="projects/geb-dwh-test/locations/global/keyRings/geb-dwh-tst-01/cryptoKeys/geb-dwh-tst-key01",
                                                wrapped_key="CiQAOZCFLMFIuLVQ74rUefYpxvWBwUYHWuugoSHT5lRYV+Gce+ASSQD6qDFuREha0mJXXE1RKbiAng1ACkS+8MzuaEE5GVHAomCIQHHa2pPEx8ZCuuKCuAg5HX8JwoMuIaLO2R0sMTztZoRZlUKngM4=")

            enc_dec_dict[i] = val

    print(enc_dec_dict)
    return enc_dec_dict


# UPDATE GENDER QUERY EXECUTER
def update_gender_using_dlp_dict(orig_dict, project, dataset_id, helper_tn):
    # tn="geb-dwh-test.uat_geb_dwh_eu_act.sorted_prophet_rows_full_export_helper"
    # dataset_ref = bigquery.DatasetReference(project, dataset_id)
    # table_ref = dataset_ref.table(helper_tn)
    tn = f'{project}.{dataset_id}.{helper_tn}'
    # tns="sorted_prophet_rows_full_export_helper"

    key0 = list(orig_dict.keys())[0]
    key1 = list(orig_dict.keys())[1]
    val0 = list(orig_dict.values())[0]
    val1 = list(orig_dict.values())[1]
    print(key0, key1)

    sql_update = """ 
    UPDATE `geb-dwh-test.uat_geb_dwh_eu_act.prophet_input_gender_encrypted`
    SET SEX = CASE SEX WHEN @key0 THEN @val0
                    WHEN @key1 THEN @val1
        END
    WHERE SEX IN (@key0,@key1);
    """

    client_l = bigquery.Client()
    # query_l=create_prophet_input_export_helper_latest_quarter(rby,q,tn)
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("tn", "STRING", f'{tn}'),
            bigquery.ScalarQueryParameter("key0", "STRING", f'{key0}'),
            bigquery.ScalarQueryParameter("key1", "STRING", f'{key1}'),
            bigquery.ScalarQueryParameter("val0", "STRING", f'{val0}'),
            bigquery.ScalarQueryParameter("val1", "STRING", f'{val1}'),
        ]
    )
    table = client_l.query(sql_update, job_config=job_config)
    table = table.result()

    # wait 3 sec. for table creation, then trigger table name creation function
    sleep(3)


# CONFIGURE RETRY STRATEGY
"""
predicate parameter defaults to if_transient_error(), which catches following errors considered transient:

    - google.api_core.exceptions.InternalServerError - HTTP 500, gRPC INTERNAL(13) and its subclasses.

    - google.api_core.exceptions.TooManyRequests - HTTP 429

    - google.api_core.exceptions.ServiceUnavailable - HTTP 503

    - requests.exceptions.ConnectionError

    - requests.exceptions.ChunkedEncodingError - The server declared chunked encoding but sent an invalid chunk.

    - google.auth.exceptions.TransportError - Used to indicate an error occurred during an HTTP request.
"""

retry_config = retry.Retry(initial=1.0, maximum=60.0,
                           multiplier=2.0, deadline=120.0)
# Example usage is below:
# result = client.some_method(retry=retry_config)

# CREATE TABLE NAMES


def create_table_names(project, dataset_id, helper_tn):
    client_tn = bigquery.Client()
    # project = "geb-dwh-test"
    # dataset_id = "uat_geb_dwh_eu_act"
    table_names = []

    dataset_ref = bigquery.DatasetReference(project, dataset_id)
    table_ref = dataset_ref.table(helper_tn)
    table = client_tn.get_table(table_ref, retry=retry_config)
    df = client_tn.list_rows(table).to_dataframe()
    # print(df.iloc[0][1])
    if len(df) == 0:
        print("no records available for this quarter")
        exit()
    # create table names
    for j in range(0, len(df)):
        ds_body = 'geb-dwh-test.uat_geb_dwh_eu_act'
        # full_table_name=f'{ds_body}.{df.iloc[j][1][:3]}by{int(df.iloc[j][2])}q{df.iloc[j][3]}{df.iloc[j][4].lower()}'
        full_table_name = f'{ds_body}.{df.iloc[j][1].replace("/","_").replace(".","_")}by{int(df.iloc[j][2])}q{df.iloc[j][3]}{df.iloc[j][4].lower()}'

        # ds_body+df.iloc[j][1]+df.iloc[j][2]+df.iloc[j][3]+df.iloc[j][4]
        table_names.append(full_table_name)
    print("total records for this export: ", len(table_names))
    # print(table_names[0])
    return table_names, df, dataset_ref


# TABLE GENERATOR
def generate_tables(df, table_names):
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

# HELPER TO CHECK IF TABLE EXISTS


def bq_if_table_exists(client, table_ref):
    from google.cloud.exceptions import NotFound
    try:
        client.get_table(table_ref)
        return True
    except NotFound:
        return False

# TABLE EXPORTER


def export_tables(df, table_names, dataset_ref, project, dataset_id):
    for j in range(0, len(df)):
        bucket_name = 'geb-dwh-tst-bck-novus-europe-west1'
        date_now = dt.date.today().strftime('%Y%m%d')
        folder_name = 'prophet_exports'
        table_id = table_names[j][32:]  # .lower()

        # ADDED date_now AS SUB-FOLDER NAME FOR TESTING PURPOSES, WILL BE REMOVED LATER --TBC
        destination_uri = f"gs://{bucket_name}/{folder_name}/{date_now}/{table_id}_{date_now}.csv"
        table_ref = dataset_ref.table(table_id)

        # geb-dwh-test.uat_geb_dwh_eu_act.GH7by2020q4wp
        print('\nTable reference:', j+1, table_ref,)
        # gs://geb-dwh-tst-bck-novus-europe-west1/GH7by2020q4wp.csv
        print('destination_uri', destination_uri)
        client_ex = bigquery.Client()

        while True:
            if bq_if_table_exists(client_ex, table_ref):
                print("AVAILIBILITY CHECK RETURNS TRUE",
                      table_ref, "HAS BEEN CREATED AND READY")
                extract_job = client_ex.extract_table(
                    table_ref,
                    destination_uri,
                    # Location must match that of the source table.
                    location="EU",
                    retry=retry_config,
                    # timeout=5.0
                )  # API request

                extract_job.result()  # Waits for job to complete.

                print("Exported {}:{}.{} to {}".format(
                    project, dataset_id, table_id, destination_uri))
                break
            else:
                print(
                    f'TABLE {table_ref} IS NOT READY, WILL WAIT 5 SECONDS AND RETRY')
                sleep(5)


# TABLE DELETOR
def delete_tables(df, table_names, dataset_ref, dataset_id):
    print('\nCLEAN-UP: The export phase has been finished. \nNow the exported tables will be deleted from BigQuery dataset')
    for j in range(len(df)):
        # DELETE AFTER EXPORT
        # wait 1 sec. for table export, then trigger extract
        # sleep(2)
        table_id = table_names[j][32:]  # .lower()
        table_ref = dataset_ref.table(table_id)
        # print('Executed till delete phase ', table_ref, ' will be deleted')
        client_ex = bigquery.Client()
        client_ex.delete_table(table_ref, retry=retry_config)  # API request
        print('Table {} {}:{} deleted.'.format(j+1, dataset_id, table_id))


# QUERY CREATOR
# creates queries for prophet input file creation using helper table for filtering
def create_prophet_input_files(li, rby, q, cc, tn):
    project = "geb-dwh-test"
    dataset_id = "uat_geb_dwh_eu_act"
    # Check the source view name!
    source_view = "source_prophet_input_v6"
    return f"""
            CREATE OR REPLACE TABLE `{tn}` AS
            SELECT * FROM `{project}.{dataset_id}.{source_view}`
            WHERE LOCALINSURER =@li AND BALANCE_YEAR=@rby AND QUARTER=@q AND COVER_CODE=@cc
            ORDER BY SPCODE, MEMBER_ID;
         """


# HELPER TABLE QUERY CREATOR-1
# creates the query for helper table generation for latest/selected quarter export
def create_prophet_input_export_helper_latest_quarter(rby, q, tn):
    project = "geb-dwh-test"
    dataset_id = "uat_geb_dwh_eu_act"
    # Check the source view name!
    source_view = "source_prophet_input_v6"
    return f"""
            CREATE OR REPLACE TABLE `{tn}` AS
            SELECT DISTINCT LOCALINSURER,COMPANY_CODE,BALANCE_YEAR,QUARTER,COVER_CODE FROM
            `{project}.{dataset_id}.{source_view}`
            WHERE BALANCE_YEAR=@rby AND QUARTER=@q
            ORDER BY LOCALINSURER,BALANCE_YEAR,QUARTER,COVER_CODE;
         """


# HELPER TABLEQUERY CREATOR-2
# creates the query for helper table generation for full export
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


# HELPER INDEX TABLE CREATOR (FULL EXPORT)
def generate_helper_index_table_full(project, dataset_id, helper_tn):
    # tn="geb-dwh-test.uat_geb_dwh_eu_act.sorted_prophet_rows_full_export_helper"
    tn = f'{project}.{dataset_id}.{helper_tn}'
    # tns="sorted_prophet_rows_full_export_helper"
    client_f = bigquery.Client()
    query_f = create_prophet_input_full_export_helper(tn)

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("tn", "STRING", f'{tn}'),
        ]
    )
    client_f.query(query_f, job_config=job_config)

    # wait 3 sec. for table creation, then trigger table name creation function
    sleep(3)


# HELPER INDEX TABLE CREATOR (LATEST OR SELECTED EXPORT)
def generate_helper_index_table_selected(project, dataset_id, helper_tn, current_yy, current_q):
    # tn="geb-dwh-test.uat_geb_dwh_eu_act.sorted_prophet_rows_full_export_helper"
    tn = f'{project}.{dataset_id}.{helper_tn}'
    # tns="sorted_prophet_rows_full_export_helper"
    rby = int(current_yy)
    q = str(current_q)
    # tns="sorted_prophet_rows_latest_quarters"
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

    # wait 3 sec. for table creation, then trigger table name creation function
    sleep(3)


# MAIN EXECUTER
# main function that executes all in a flow
def export_prophet():
    project = "geb-dwh-test"
    dataset_id = "uat_geb_dwh_eu_act"
    bucket_uri = "https://console.cloud.google.com/storage/browser/geb-dwh-tst-bck-novus-europe-west1"

    distc_val_list = get_disitnct_gender_encrypted_values(
        project, dataset_id, helper_tn="prophet_input_gender_encrypted")
    print("distc_val_list", distc_val_list)
    orig_dict = get_original(distc_val_list)
    print("original", orig_dict)
    update_gender_using_dlp_dict(
        orig_dict, project, dataset_id, helper_tn="prophet_input_gender_encrypted")

    export_type = user_input()

    if export_type.lower() == 'f':
        # create the export helper table for full export
        helper_tn = "sorted_prophet_rows_full_export_helper"
        generate_helper_index_table_full(project, dataset_id, helper_tn)

        # create_tables(tns)

    if export_type.lower() == 'l':
        current_yy, current_q = previous_quarter(dt.date.today())
        # current_yy,current_q=previous_quarter(dt.date(2021,1,31)) # This line is for testing
        print(current_yy, current_q)
        helper_tn = "sorted_prophet_rows_latest_quarters"

        # Export helper table creation for latest quarters
        generate_helper_index_table_selected(
            project, dataset_id, helper_tn, current_yy, current_q)

        # create_tables(tns)

    if export_type.lower() == 'm':
        current_yy = input("Provide the year for the reporting:\n")
        current_q = input("Provide the quarter:\n")
        print(current_yy, current_q)
        helper_tn = "sorted_prophet_rows_manually_selected_quarter"
        # Export helper table creation for selected quarters
        generate_helper_index_table_selected(
            project, dataset_id, helper_tn, current_yy, current_q)

        # create_tables(tns)

    # CREATE TABLE NAMES
    table_names, df, dataset_ref = create_table_names(
        project, dataset_id, helper_tn)

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
        \n\nPlease do not forget to delete these exported files from the bucket after feeding your Prophet data import pipeline.\n')


export_prophet()
