from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_dag',
    default_args=default_args,
    description='Description of my DAG',
    schedule_interval=timedelta(seconds=5),
)

t1 = BashOperator(
    task_id='start_python_api_container',
    bash_command='docker run -d --name my_python_api_container my_python_api',
    dag=dag,
)

t2 = BashOperator(
    task_id='start_matlab_container',
    bash_command='docker run -d --name my_matlab_container my_matlab_image',
    dag=dag,
)

t1 >> t2

