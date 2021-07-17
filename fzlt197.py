# Import the timedelta object
from datetime import timedelta

# Create the dictionary entry
default_args = {
    'start_date': datetime(2020, 2, 20),
    'sla': timedelta(minutes=30)
}

# Add to the DAG
test_dag = DAG('test_workflow', default_args=default_args,
               schedule_interval='@None')


test_dag = DAG('test_workflow', start_date=datetime(
    2020, 2, 20), schedule_interval='@None')


# After completing the SLA on the entire workflow, you realize you really
# only need the SLA timing on a specific task instead of the full workflow.
# Create the task with the SLA
task1 = BashOperator(task_id='first_task',
                     sla=timedelta(hours=3),
                     bash_command='initialize_data.sh',
                     dag=test_dag)
