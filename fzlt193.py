from airflow.models import DAG
default_args = {
    'owner': 'jdoe',
    'start_date': '2019-01-01'
}
dag = DAG(dag_id="etl_update", default_args=default_args)

# on command line:
# airflow list_dags # to show all recognized DAGs.
# airflow -h # for descriptions
# airflow webserver -p 9090 #To start airflow webserver on port 9090
