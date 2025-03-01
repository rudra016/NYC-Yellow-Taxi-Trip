from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import pandas as pd
import psycopg2
from include.scripts.extract import download_data
from include.scripts.transform import clean_data
from include.scripts.load import load_data_to_postgres

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Initialize DAG
dag = DAG(
    'nyc_taxi_etl',
    default_args=default_args,
    description='ETL Pipeline for NYC Yellow Taxi Data',
    schedule_interval='@daily',
    catchup=False
)

# Define file paths
RAW_DATA_PATH = "/usr/local/airflow/data/raw"
CLEANED_DATA_PATH = "/usr/local/airflow/data/clean"


# Extract Task
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=download_data,
    op_kwargs={'save_path': RAW_DATA_PATH},
    execution_timeout=timedelta(hours=1),
    dag=dag
)

# Transform Task
transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=clean_data,
    op_kwargs={'input_path': RAW_DATA_PATH, 'output_path': CLEANED_DATA_PATH},
    dag=dag
)

# Load Task
load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data_to_postgres,
    op_kwargs={'input_path': CLEANED_DATA_PATH},
    dag=dag
)

# Define Task Dependencies
extract_task >> transform_task >> load_task
