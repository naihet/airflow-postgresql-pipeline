from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys

sys.path.append("/opt/airflow/src")

from extract import extract_data
from transform import transform_data
from load import load_data
from validate import validate_data
from quality import quality_check

def extract(ti):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    raw_path = f"/opt/airflow/temp/raw_{timestamp}.parquet"

    extract_data(
        "/opt/airflow/data/Sample - Superstore.csv",
        raw_path
    )

    ti.xcom_push(
        key="raw_path",
        value=raw_path
    )

    print("Extract completed")

def transform(ti):

    raw_path = ti.xcom_pull(
        task_ids="extract",
        key="raw_path"
    )

    clean_path = raw_path.replace(
        "raw",
        "clean"
    )

    transform_data(
        raw_path,
        clean_path
    )

    ti.xcom_push(
        key="clean_path",
        value=clean_path
    )

    print("Transform completed")

def quality(ti):

    clean_path = ti.xcom_pull(
        task_ids="transform",
        key="clean_path"
    )

    quality_check(clean_path)

    print("Quality Check completed")

def load(ti):

    clean_path = ti.xcom_pull(
        task_ids="transform",
        key="clean_path"
    )

    load_data(
        clean_path
    )

    print("Load completed")

def validate(ti):

    clean_path = ti.xcom_pull(
        task_ids="transform",
        key="clean_path"
    )

    report = validate_data(
        clean_path
    )

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

    quality_task = PythonOperator(
    task_id="quality",
    python_callable=quality
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load
    )

    validate_task = PythonOperator(
        task_id="validate",
        python_callable=validate
    )

    extract_task >> transform_task >> quality_task >> load_task >> validate_task