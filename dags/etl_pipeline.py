from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
import sys

sys.path.append("/opt/airflow/src")

from extract import extract_data
from transform import transform_data
from load import load_data
from validate import validate_data

def extract():

    df = extract_data(
        "/opt/airflow/data/Sample - Superstore.csv"
    )

    print(df.head())

def transform():

    df = extract_data(
        "/opt/airflow/data/Sample - Superstore.csv"
    )

    df = transform_data(df)

    print(df.head())

def load():

    df = extract_data(
        "/opt/airflow/data/Sample - Superstore.csv"
    )

    df = transform_data(df)

    load_data(df)

def validate():

    df = extract_data(
        "/opt/airflow/data/Sample - Superstore.csv"
    )

    df = transform_data(df)

    report = validate_data(df)

    print(report)

with DAG(
    dag_id="sales_etl_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["etl", "sales"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load
    )

    validate_task = PythonOperator(
        task_id="validate",
        python_callable=validate
    )

    extract_task >> transform_task >> load_task >> validate_task