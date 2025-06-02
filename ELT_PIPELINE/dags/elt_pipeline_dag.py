"""
This DAG orchestrates a daily ELT pipeline that:
1. Ingest data to GCS and load into BigQuery
2. Triggers DBT transformation after data load.
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import sys
from data_to_gcs_to_bq import data_gcs_bq

# Set execution date to yesterday (standard practice)
yesterday = datetime.combine(datetime.today() - timedelta(days = 1), datetime.min.time())

default_args = {
    'owner': 'airflow',
    'start_date': yesterday,
    'retries': 1,
    'retry_delay': timedelta(minutes = 3),
}

with DAG(
    dag_id = 'data_to_gcs_bq_dag',
    default_args = default_args,
    schedule_interval = '@daily', # Runs daily at midnight
    catchup = False
) as dag:
    # Task 1: Data ingestion and Loading
    ingest_and_load_data = PythonOperator(
        task_id ='ingest_and_load_data',
        python_callable = data_gcs_bq  # Calls ETL function
    )
    # DBT transformation
    run_dbt = BashOperator(
    task_id='run_dbt',
    bash_command='cd /opt/airflow/dbt && DBT_PROFILES_DIR=/opt/airflow/config/.dbt dbt run',
)
    # Task 1 >> Task 2
    ingest_and_load_data >> run_dbt
