from google.cloud import bigquery

client = bigquery.Client()
project = "geb-dwh-test"
dataset_id = "uat_geb_dwh_eu_act"

dataset_ref = bigquery.DatasetReference(project, dataset_id)
table_ref = dataset_ref.table("sorted_prophet_rows_3")
table = client.get_table(table_ref)

df = client.list_rows(table).to_dataframe()
# print(df.iloc[0][1])
table_names = []
for j in range(0, len(df)):
    ds_body = 'geb-dwh-test.uat_geb_dwh_eu_act'
    full_table_name = f'{ds_body}.{df.iloc[j][0].replace(" ","")[:5]}by{int(df.iloc[j][1])}q{df.iloc[j][2]}{df.iloc[j][3]}'

    # ds_body+df.iloc[j][0]+df.iloc[j][1]+df.iloc[j][2]+df.iloc[j][3]
# '{} {}'.format('one', 'two')
    table_names.append(full_table_name)
# print(table_names)
print(table_names[0])


def create_prophet_input_files(li, rby, q, cc, tn):
    project = "geb-dwh-test"
    dataset_id = "uat_geb_dwh_eu_act"
    source_table = "prophet_input"
    return f"""
            CREATE OR REPLACE TABLE `{tn}` AS
            --CREATE OR REPLACE TABLE  `geb-dwh-test.uat_geb_dwh_eu_act.Testprophet_input_2` AS
            SELECT * FROM `{project}.{dataset_id}.{source_table}`
            WHERE LOCALINSURER =@li AND BALANCE_YEAR=@rby AND QUARTER=@q AND COVER_CODE=@cc;
         """


# for j in range(0,len(df)):
for j in range(0, 2):
    li = df.iloc[j][0]
    rby = int(df.iloc[j][1])
    q = df.iloc[j][2]
    cc = df.iloc[j][3]
    tn = table_names[j]
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

    bucket_name = 'geb-dwh-tst-bck-novus-europe-west1'
    table_id = tn  # .lower()

    destination_uri = f"gs://{bucket_name}/{table_id}.csv"
    table_ref = dataset_ref.table(table_id)

    extract_job = client.extract_table(
        table_ref,
        destination_uri,
        # Location must match that of the source table.
        location="europe-west1",
    )  # API request
    extract_job.result()  # Waits for job to complete.

    print("Exported {}:{}.{} to {}".format(
        project, dataset_id, table_id, destination_uri))
