"""
example usage:
python3 DIM_EXEC.py --pipeline Dim_Contract
optionally defining a different environmet/dataset: 
python3  DIM_EXEC.py  --pipeline  Dim_Country --dataset_meta  geb_met_mgr_eu
"""

from google.cloud import bigquery
from geb_utils import create_start_sql, create_end_sql
from geb_utils import bq_if_table_exists
from geb_utils import create_dp_log_id_sql
from geb_utils import get_dummy_value, get_param_from_meta_dp
from geb_utils import find_if_any_predecessor_failed, check_active_flag, find_nr_predecessors
import argparse
import logging
import sys

logging.basicConfig(level=logging.INFO)  # filename='example.log',

parser = argparse.ArgumentParser()
parser.add_argument('--pipeline', nargs='*')
parser.add_argument('--dataset_meta', nargs='?')
# not used yet / using default project/ to add later
parser.add_argument('--project', nargs='?')
name_pipeline = parser.parse_args().pipeline[0]
dataset_meta = parser.parse_args().dataset_meta
project = parser.parse_args().project
if project is None:
    project = 'geb-dwh-test'

client = bigquery.Client(project)  # important

# the parameters
if dataset_meta is not None:
    parameters = get_param_from_meta_dp(
        name_pipeline, client, dataset_meta=dataset_meta, project=project)
else:
    parameters = get_param_from_meta_dp(
        name_pipeline, client)  # getting dict with all param

if parameters is not None:
    project = parameters['project']
    dp_id = parameters['dp_id']
    dataset_stage = parameters['source_dataset']
    dataset_dwh = parameters['target_dataset']
    dataset_meta = parameters['meta_dataset']
    bq_view = parameters['source_table']
    bq_table_dim = parameters['target_table']
    merge_condition = parameters['merge_condition']
    dwhid = parameters['dwhid']
else:
    print('No parameters for the pipeline {}. Exiting the script.'.format(name_pipeline))
    sys.exit('No parameters for the pipeline, exiting.')
    # quit()


# derived parameters
logging_dataset = project + '.' + dataset_meta
target = project + '.' + dataset_dwh + '.' + bq_table_dim
source = project + '.' + dataset_stage + '.' + bq_view


def my_func1(field):
    return field + ' = Source.' + field


def my_func2(field):
    return 'Source.' + field


def create_merge_dim_scd1_sql(source, target, dwhid, view_bq, client, merge_condition):
    column_names = ["{0}".format(
        schema.name) for schema in view_bq.schema if schema.name != 'CREATED_ON']
    whenmatched = [my_func1(column_name) for column_name in column_names]
    whennotmatched = [my_func2(column_name) for column_name in column_names]
    column_names = ', '.join(column_names)
    whenmatched = ', '.join(whenmatched)
    whennotmatched = ', '.join(whennotmatched)
    dp_log_id = str(create_dp_log_id_sql(
        logging_dataset, name_pipeline, client))

    return f"""
     MERGE `{target}` Target
     USING `{source}` Source
       ON {merge_condition}
     WHEN MATCHED THEN
      UPDATE SET
            {whenmatched},
            META_DP_LOG_ID = '{dp_log_id}',
            CREATED_ON = current_timestamp()
     WHEN NOT MATCHED THEN
           INSERT ({dwhid}, {column_names}, CREATED_ON, META_DP_LOG_ID)
           VALUES (generate_uuid(), {whennotmatched}, current_timestamp(), '{dp_log_id}');
          """


logging.info("Starting pipeline")
query_job_start = client.query(
    create_start_sql(logging_dataset, name_pipeline))
query_job_start.result()
logging.info("Total rows affected: %s", query_job_start.num_dml_affected_rows)

if (query_job_start.num_dml_affected_rows == 0):
    print('The dimension job(or DWH) has not been started. Aborting the pipeline. Please start dimentsion JOB.')
    sys.exit('The dimension job(or DWH) has not been started, exiting.')
    # quit()

# if (find_if_any_predecessor_failed(dp_id, client)):
#    print('Some of the dependent pipelines failed during the daily load. Thherefore this dp also is failing. Dp failed.')
#    sys.exit('Some of the dependent pipelines failed during the daily load, exiting')
#    #quit()

view_ref = client.dataset(dataset_stage).table(bq_view)
view_current_bq = client.get_table(view_ref)

print("Start merging for table {}".format(bq_table_dim))
query_job_merge = client.query(create_merge_dim_scd1_sql(
    source, target, dwhid, view_current_bq, client, merge_condition))
query_job_merge.result()
nr = query_job_merge.num_dml_affected_rows
print("Total rows affected: ", nr)

print("Ending pipeline")
query_job_end = client.query(create_end_sql(
    logging_dataset, name_pipeline, nr_rec_affected=nr))
query_job_end.result()
print("Total rows affected: ", query_job_end.num_dml_affected_rows)

print('Dimension pipeline \'{}\' ended.'.format(name_pipeline))
