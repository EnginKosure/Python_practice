from google.cloud import bigquery
import datetime as dt
import pandas as pd
from time import sleep
from google.api_core import retry
from google.api_core import exceptions

# GLOBAL VARIABLES
# To keep the created table names which must be deleted later during clean-up
tables_cleanup = []

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

# HELPER FUNCTION TO REIDENTIFY THE ENCRYPTED (DEIDENTIFIED) GENDER FIELD


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
    print(
        f"\tThe response from DLP API call for {input_str} is", response.item.value)

    return response.item.value


# HELPER TO CHECK IF TABLE EXISTS
def bq_if_table_exists(client, table_ref):
    from google.cloud.exceptions import NotFound
    try:
        client.get_table(table_ref)
        return True
    except NotFound:
        return False


# PROPHET INPUT GENDER ENCRYPTED TABLE CREATION QUERY
def create_gender_deidentified_table():

    sql_deidentified = """ 
            CREATE OR REPLACE TABLE `geb-dwh-test.uat_geb_dwh_eu_act.prophet_input_gender_encrypted` AS 
            SELECT * FROM `geb-dwh-test.uat_geb_dwh_eu_act.source_prophet_input`
    """

    client_l = bigquery.Client()
    table = client_l.query(sql_deidentified)
    table = table.result()

    # wait 3 sec. for table creation
    sleep(3)


def get_distinct_gender_encrypted_values():

    sql = """
    SELECT DISTINCT SEX FROM `geb-dwh-test.uat_geb_dwh_eu_act.prophet_input_gender_encrypted` ORDER BY SEX DESC;
    """
    client_en = bigquery.Client()
    table_ref = "geb-dwh-test.uat_geb_dwh_eu_act.prophet_input_gender_encrypted"

    while True:
        if bq_if_table_exists(client_en, table_ref):
            print("AVAILIBILITY CHECK RETURNS TRUE",
                  table_ref, "HAS BEEN CREATED AND READY")
            table = client_en.query(sql)
            table = table.result()
            df = table.to_dataframe()
            # ['CE_(24):AfkwbapkQwFqtk8Gx42biBhS', 'CE_(24):AbmgbLq4OGncwRPFrV3ZodFN', '', None]
            distinct_values = list(df['SEX'].unique())
            print(distinct_values)
            break

        else:
            print(
                f'TABLE {table_ref} IS NOT READY, WILL WAIT 5 SECONDS AND RETRY')
            sleep(5)

    return distinct_values


def get_original(dist_val):
    enc_dec_dict = {}
    for i in dist_val:
        if i not in (None, ""):
            # CAUTION!
            # CHECK IF THE KEY_NAME AND WRAPPED_KEY ARGUMENTS ARE UP-TO-DATE! THEY MUST MATCH WITH THE ONES USED FOR ENCRYPTION IN DATAFUSION PIPELINE.
            # They would change every three months and the new wrapped_key / key_name info would be sent by IT to BI and to DWH teams.
            val = reidentify_with_deterministic('geb-dwh-test', i, surrogate_type="CE_", key_name="projects/geb-dwh-test/locations/global/keyRings/geb-dwh-tst-01/cryptoKeys/geb-dwh-tst-key01",
                                                wrapped_key="CiQAOZCFLMFIuLVQ74rUefYpxvWBwUYHWuugoSHT5lRYV+Gce+ASSQD6qDFuREha0mJXXE1RKbiAng1ACkS+8MzuaEE5GVHAomCIQHHa2pPEx8ZCuuKCuAg5HX8JwoMuIaLO2R0sMTztZoRZlUKngM4=")

            enc_dec_dict[i] = val

    # print(enc_dec_dict)
    return enc_dec_dict


# PROPHET INPUT GENDER REIDENTIFICATION QUERY
def create_gender_reidentified_table(orig_dict):

    key0 = list(orig_dict.keys())[0]
    key1 = list(orig_dict.keys())[1]
    val0 = 1 if list(orig_dict.values())[0] == 'F' else 0
    val1 = 0 if list(orig_dict.values())[1] == 'M' else 1
    # print(key0, key1)

    sql_reidentified = """ 
            CREATE OR REPLACE TABLE `geb-dwh-test.uat_geb_dwh_eu_act.prophet_input_gender_reidentified` AS 
            SELECT SPCODE, MEMBER_ID, AGE_NOW,
            CASE SEX WHEN @key0 THEN @val0
                     WHEN @key1 THEN @val1
            END AS SEX,
            ANN_ANNUITY_PAID, ANN_ANNUITY_REPORTED, ENTRY_MONTH, ENTRY_YEAR,INIT_POLS_IF,MTHS_TO_SALE,
            IFRS_RESERVES,COVER_CODE, LOCALINSURER,COMPANY_CODE, BALANCE_YEAR, QUARTER, AGE_GRT_25
            FROM `geb-dwh-test.uat_geb_dwh_eu_act.source_prophet_input`
    """

    client_l = bigquery.Client()
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("key0", "STRING", f'{key0}'),
            bigquery.ScalarQueryParameter("key1", "STRING", f'{key1}'),
            bigquery.ScalarQueryParameter("val0", "INT64", f'{val0}'),
            bigquery.ScalarQueryParameter("val1", "INT64", f'{val1}'),
        ]
    )
    table = client_l.query(sql_reidentified, job_config=job_config)
    table = table.result()

    # wait 3 sec. for table creation
    sleep(3)


# ERROR HANDLING
def control_gender_reidentification(orig_dict):

    key0 = list(orig_dict.keys())[0]
    key1 = list(orig_dict.keys())[1]
    val0 = 1 if list(orig_dict.values())[0] == 'F' else 0
    val1 = 0 if list(orig_dict.values())[1] == 'M' else 1
    # print(key0, key1)

    control_sql = """
            SELECT
            CASE WHEN CNT =(SELECT CNT FROM (SELECT SEX, COUNT(SEX) AS CNT,
                            FROM `geb-dwh-test.uat_geb_dwh_eu_act.prophet_input_gender_reidentified` 
                            GROUP BY SEX ORDER BY CNT DESC LIMIT 1)) THEN "True"
                ELSE "False"
            END AS CONTROL
            FROM (SELECT SEX, COUNT(SEX) AS CNT,
            FROM `geb-dwh-test.uat_geb_dwh_eu_act.prophet_input_gender_encrypted` 
            GROUP BY SEX
            ORDER BY CNT DESC
            LIMIT 1)
            """

    compare_sql_ = """
        SELECT * FROM (SELECT SEX, COUNT(SEX) AS CNT,
        FROM `geb-dwh-test.uat_geb_dwh_eu_act.prophet_input_gender_reidentified` 
        GROUP BY SEX
        ORDER BY CNT DESC
        LIMIT 2
        ) JOIN (SELECT SEX AS GENDER, COUNT(SEX) AS CNT,
        FROM `geb-dwh-test.uat_geb_dwh_eu_act.prophet_input_gender_encrypted` 
        GROUP BY SEX
        ORDER BY CNT DESC)  USING (CNT)
    """

    client_l = bigquery.Client()
    table = client_l.query(control_sql)
    table = table.result()
    compare = client_l.query(compare_sql_).result().to_dataframe()

    if table.to_dataframe().iloc[0][0] == 'True' and (compare.iloc[0][1] == val0 if compare.iloc[0][2] == key0 else compare.iloc[0][1] == val1) \
            and (compare.iloc[1][1] == val1 if compare.iloc[1][2] == key1 else compare.iloc[1][1] == val0):
        print("FIRST CHECK RETURNS",
              compare.iloc[0][1] == val0 if compare.iloc[0][2] == key0 else compare.iloc[0][1] == val1)
        print("SECOND CHECK RETURNS",
              compare.iloc[1][1] == val1 if compare.iloc[1][2] == key1 else compare.iloc[1][1] == val0)
        print(compare)
        print("THE GENDER REIDENTIFICATION OPERATION WAS SUCCESSFUL!")
        return True

    else:
        print("OPERATION UNSUCCESSFUL, PLEASE CHECK THE WRAPPED_KEY AND KEY_NAME PARAMETERS TO DLP REIDENTIFICATION CALL AND TRY AGAIN AFTER UPDATING")
        return False


# CREATE TABLE NAMES
def create_table_names(project, dataset_id, helper_tn):
    client_tn = bigquery.Client()
    table_names = []
    dataset_ref = bigquery.DatasetReference(project, dataset_id)
    table_ref = dataset_ref.table(helper_tn)
    table = client_tn.get_table(table_ref, retry=retry_config)
    df = client_tn.list_rows(table).to_dataframe()

    # create table names
    for j in range(0, len(df)):
        ds_body = 'geb-dwh-test.uat_geb_dwh_eu_act'
        full_table_name = f'{ds_body}.{df.iloc[j][1].replace("/","_").replace(".","_")}by{int(df.iloc[j][2])}q{df.iloc[j][3]}{df.iloc[j][4].lower()}'
        table_names.append(full_table_name)
    print("total records for this export: ", len(table_names))
    return table_names, df, dataset_ref


# TABLE GENERATOR
def generate_tables(df, table_names):
    for j in range(0, len(df)):
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


# TABLE EXPORTER
def export_tables(df, table_names, dataset_ref, project, dataset_id):
    for j in range(0, len(df)):
        bucket_name = 'geb-dwh-tst-bck-novus-europe-west1'
        date_now = dt.date.today().strftime('%Y%m%d')
        folder_name = 'prophet_exports'
        table_id = table_names[j][32:]  # .lower()

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
def delete_tables(df, table_names, dataset_ref, dataset_id, tables_cleanup):
    print('\nCLEAN-UP: The export phase has been finished. \nNow the exported tables will be deleted from BigQuery dataset')
    for j in range(len(df)):
        # DELETE AFTER EXPORT
        table_id = table_names[j][32:]
        table_ref = dataset_ref.table(table_id)
        client_ex = bigquery.Client()
        client_ex.delete_table(table_ref, retry=retry_config)  # API request
        print('Table {} {}:{} deleted.'.format(j+1, dataset_id, table_id))

    for j in range(len(tables_cleanup)):
        # DELETE AFTER EXPORT
        table_id = tables_cleanup[j]
        table_ref = dataset_ref.table(table_id)
        client_ex = bigquery.Client()
        client_ex.delete_table(table_ref, retry=retry_config)  # API request
        print('Helper Table {} {}:{} deleted.'.format(j+1, dataset_id, table_id))


# QUERY CREATOR
# creates queries for prophet input file creation using helper table for filtering
def create_prophet_input_files(li, rby, q, cc, tn):
    project = "geb-dwh-test"
    dataset_id = "uat_geb_dwh_eu_act"
    # CAUTION!
    # Check the source view name!
    source_view = "prophet_input_gender_reidentified"
    return f"""
            CREATE OR REPLACE TABLE `{tn}` AS
            SELECT * FROM `{project}.{dataset_id}.{source_view}`
            WHERE LOCALINSURER =@li AND BALANCE_YEAR=@rby AND QUARTER=@q AND COVER_CODE=@cc
            ORDER BY SPCODE, MEMBER_ID;
         """


# HELPER TABLE QUERY CREATOR-1
# creates the query for helper table generation for latest available quarter export
def create_prophet_input_export_helper_latest_quarter(rby, q, tn):
    project = "geb-dwh-test"
    dataset_id = "uat_geb_dwh_eu_act"
    # CAUTION!
    # Check the source view name!
    source_view = "prophet_input_gender_reidentified"
    return f"""
            CREATE OR REPLACE TABLE `{tn}` AS
            SELECT DISTINCT LOCALINSURER,COMPANY_CODE,BALANCE_YEAR,QUARTER,COVER_CODE FROM
            `{project}.{dataset_id}.{source_view}`
            WHERE BALANCE_YEAR=@rby AND QUARTER=@q
            ORDER BY LOCALINSURER,BALANCE_YEAR,QUARTER,COVER_CODE;
         """


# Calculates and returns previous quarter and its year
def previous_quarter(ref):
    quarter = (ref.month - 1) // 3
    prev_quarter = (quarter - 1) % 4
    pq = pd.Timestamp(dt.datetime(ref.year if quarter >
                                  0 else ref.year-1, prev_quarter*3+1, 1)).quarter
    yy = pd.Timestamp(dt.datetime(ref.year if quarter >
                                  0 else ref.year-1, prev_quarter*3+1, 1)).year
    return yy, pq


# HELPER INDEX TABLE CREATOR (LATEST AVAILABLE EXPORT)
def generate_helper_index_table(project, dataset_id, helper_tn, current_yy, current_q):
    print(
        f"generate_helper_index_table function is called with parameters: {project}, {dataset_id}, {helper_tn}, {current_yy}, {current_q} ")
    tn = f'{project}.{dataset_id}.{helper_tn}'
    rby = int(current_yy)
    q = str(current_q)
    # print("rby", rby, "q", q)
    client_l = bigquery.Client()
    query_l = create_prophet_input_export_helper_latest_quarter(rby, q, tn)
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("rby", "NUMERIC", f'{rby}'),
            bigquery.ScalarQueryParameter("q", "STRING", f'{q}'),
            bigquery.ScalarQueryParameter("tn", "STRING", f'{tn}'),
        ]
    )

    dataset_ref = bigquery.DatasetReference(project, dataset_id)
    table_ref = dataset_ref.table(helper_tn)
    client_l.query(query_l, job_config=job_config)

    while True:
        if bq_if_table_exists(client_l, table_ref):
            print("AVAILIBILITY CHECK RETURNS TRUE",
                  table_ref, "HAS BEEN CREATED AND READY")
            table = client_l.get_table(table_ref)
            df = client_l.list_rows(table).to_dataframe()
            break

        else:
            print(
                f'TABLE {table_ref} IS NOT READY, WILL WAIT 5 SECONDS AND RETRY')
            sleep(5)

    print("DATAFRAME", df)
    control_bool = len(df) == 0

    # print(len(df))
    # print("control bool",control_bool)

    if control_bool:
        client_l.delete_table(table_ref)
        print(
            f" NO RECORDS AVAILABLE FOR YEAR {current_yy} QUARTER {current_q} ")
        current_qn = current_q-1 if current_q != 1 else 4
        current_yyn = current_yy-1 if current_q == 1 else current_yy
        print(f" CHECKING FOR YEAR {current_yyn} QUARTER {current_qn} ")
        generate_helper_index_table(
            project, dataset_id, helper_tn, current_yyn, current_qn)


# MAIN EXECUTER
# main function that executes all in a flow
def export_prophet():
    project = "geb-dwh-test"
    dataset_id = "uat_geb_dwh_eu_act"
    bucket_uri = "https://console.cloud.google.com/storage/browser/geb-dwh-tst-bck-novus-europe-west1"

    # Create gender deidentified table
    create_gender_deidentified_table()

    # Get the distinct encrypted values for gender field
    distc_val_list = get_distinct_gender_encrypted_values()
    tables_cleanup.append("prophet_input_gender_encrypted")
    print("distc_val_list", distc_val_list)
    # Get the reidentified (original) values for each gender
    orig_dict = get_original(distc_val_list)

    # Below function is for creating a brand-new table, with gender field reidentified and numeric 1, 0
    create_gender_reidentified_table(orig_dict)
    tables_cleanup.append("prophet_input_gender_reidentified")

    # Control if gender reidentification process succeeded, then proceed
    if control_gender_reidentification(orig_dict):

        current_yy, current_q = previous_quarter(dt.date.today())
        # current_yy,current_q=previous_quarter(dt.date(2021,1,31)) # This line is for testing

        # print(current_yy,current_q)
        helper_tn = "sorted_prophet_rows_latest_quarters"
        tables_cleanup.append(helper_tn)

        # Helper table creation for latest available quarters
        generate_helper_index_table(
            project, dataset_id, helper_tn, current_yy, current_q)

    else:
        print("PLEASE RETRY WITH THE CORRECT DLP PARAMETERS.")
        exit()

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
    delete_tables(df, table_names, dataset_ref, dataset_id, tables_cleanup)

    print(f'\nExecuted till the end.\n\ncreate >> export >> delete phases consequently and successfully executed.\
        \nYou can check the bucket following this link--> {bucket_uri} \
        \n\nPlease do not forget to delete these exported files from the bucket after feeding your Prophet data import pipeline.\n')


if __name__ == '__main__':
    export_prophet()
