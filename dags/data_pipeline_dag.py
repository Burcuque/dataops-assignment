from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

with DAG(
    'dataops_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    # SSHOperator ile spark_client konteynerine bağlanıp kodu çalıştır
    run_cleaning_on_spark = SSHOperator(
        task_id='run_cleaning_script',
        ssh_conn_id='ssh_spark_client', # Bunu Airflow UI'dan tanımlamalısın
        command='python3 /scripts/clean_data.py'
    )
