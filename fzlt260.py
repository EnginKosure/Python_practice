import pandas as pd
from google.cloud import bigquery
Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
for i, m in enumerate(Months):
    print(i, m)


for i in '123':
    print("python", i,)


Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
Dict.update({"Sarah": 9})
print(Dict)


tr = 'acfab113-8a97-4871-adec-8e423de3d2b8 | 5bf807b8-b573-43b4-94da-f1c335db74ce | 23112cf0-50c8-4911-b609-d125179d0983 | 58c61236-8e70-4401-ba6f-96feecf14f95 | 9ec39e71-9287-4965-8885-da3b7086b3d8 | a8963f84-9cae-40b9-b886-6cc875f3a5e3 | 94fef309-ca5b-47a4-8123-fd4daf8b6286 | 7172313e-8d5f-43ac-97c8-2c0327fd5e96 | 7e81c227-3b6b-4934-a588-22c6e3c63e36 | 21ff24c1-f313-4055-bf40-872d6a37e534 | 0837c70d-bf2e-465c-a09c-54874a734d2c | 3167cba5-e9ba-4828-a54c-30e31d0170bb | 6d01253a-f86a-40de-9b0c-a0f708a25a7b | 3fcfa34c-d518-42d4-a89a-3db36643036f | 3650dd36-6d69-42a4-9948-989926f83efb | a5235b63-f7ab-4921-a72a-b999b3635461 | 2f837b41-219a-4743-adec-1ce2f87d4dfb | 6ef6b919-0852-43dc-8a8f-915ac8bead44 | 79a8404b-5c77-4851-be68-d3d4c95eed7d | c694eda4-5a34-42b0-89aa-3fb736a3270d | 1b013a9b-248f-4d2a-b790-35eaa6619ebc | 4f320bdc-d602-43de-9bd3-6638a01ad22c | eeafc0bc-7178-49cd-8286-8fc87092c157 | 0afc7d3f-c558-43f7-b0b1-50f65b3dd714 | 8afa3056-2bf2-48a4-a7d6-ffccc8f97160 | f7fb410c-814b-434b-bf55-de161a904cf8 | dbd814b1-c8a8-4f9d-8bed-6604658424da'
tr = tr.split('|')
# print(tr)
tr = [i.strip() for i in tr]
print(tr)


def control_dupl():

    control_sql = """
                SELECT
                CLAIMDWHID,
                CASE
                    WHEN FLOOR(LENGTH(CLAIMDWHID)/36)>24 THEN FLOOR(LENGTH(CLAIMDWHID)/36)-2
                    WHEN FLOOR(LENGTH(CLAIMDWHID)/36)>12 THEN FLOOR(LENGTH(CLAIMDWHID)/36)-1
                ELSE
                FLOOR(LENGTH(CLAIMDWHID)/36)
                END
                AS CNT
                FROM
                `geb-dwh-test.uat_geb_dwh_eu_act.fact_actuary`
                WHERE
                CLAIMDWHID LIKE '%|%'
                ORDER BY
                CNT DESC
            """

    client_l = bigquery.Client()
    table = client_l.query(control_sql)
    table = table.result().to_dataframe()
    # table=table['CLAIMDWHID'].str.split('|', expand=False)
    print(table['CLAIMDWHID'].str.split(
        '|', expand=False).explode('CLAIMDWHID'))

    with open("duplicates.csv", "a") as o:
        o.write('Hello Tihomir')
        table['CLAIMDWHID'].str.split('|', expand=False).explode(
            'CLAIMDWHID').to_csv(o, header=True, index=True)


if __name__ == '__main__':
    control_dupl()
