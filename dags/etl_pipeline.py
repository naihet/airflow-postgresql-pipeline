from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys

sys.path.append("/opt/airflow")

from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
from src.validate import validate_data
from src.quality import quality_check
from src.logger import logger
from src.callbacks import (
    task_failure_alert,
    dag_success_alert,
)
from airflow.models import Variable
from src.storage import upload_file, download_file

CSV_PATH = Variable.get("CSV_PATH")

def upload():

    upload_file(
        "/opt/airflow/data/Sample - Superstore.csv",
        "sales-data",
        "Sample - Superstore.csv"
    )

    print("Upload completed")

def download():

    download_file(
        "sales-data",
        "Sample - Superstore.csv",
        "/opt/airflow/temp/Sample - Superstore.csv"
    )

    print("Download completed")

def extract(ti):

    logger.info("Extract task started")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    raw_path = f"/opt/airflow/temp/raw_{timestamp}.parquet"

    extract_data(
        CSV_PATH,
        raw_path
    )

    ti.xcom_push(
        key="raw_path",
        value=raw_path
    )

    logger.info("Extract task finished")

def transform(ti):

    logger.info("Transform task started")

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

    logger.info("Transform task finished")

def quality(ti):

    logger.info("Quality task started")

    clean_path = ti.xcom_pull(
        task_ids="transform",
        key="clean_path"
    )

    report = quality_check(clean_path)

    logger.info("=" * 40)

    logger.info("DATA QUALITY REPORT")

    for key, value in report.items():

        logger.info(f"{key}: {value}")

    logger.info("=" * 40)

    logger.info("Quality task finished")

def load(ti):

    logger.info("Load task started")

    clean_path = ti.xcom_pull(
        task_ids="transform",
        key="clean_path"
    )

    load_data(
        clean_path
    )

    logger.info("Load task finished")

def validate(ti):

    logger.info("Validate task started")

    clean_path = ti.xcom_pull(
        task_ids="transform",
        key="clean_path"
    )

    report = validate_data(
        clean_path
    )

    logger.info(report)

    logger.info("Validate task finished")

with DAG(
    dag_id="sales_etl_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["etl", "sales"],
    on_success_callback=dag_success_alert,
) as dag:

    upload_task = PythonOperator(
        task_id="upload",
        python_callable=upload
    )

    download_task = PythonOperator(
        task_id="download",
        python_callable=download
    )

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
        on_failure_callback=task_failure_alert
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform,
        on_failure_callback=task_failure_alert
    )

    quality_task = PythonOperator(
        task_id="quality",
        python_callable=quality,
        on_failure_callback=task_failure_alert
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load,
        on_failure_callback=task_failure_alert
    )

    validate_task = PythonOperator(
        task_id="validate",
        python_callable=validate,
        on_failure_callback=task_failure_alert
    )

    upload_task >> download_task >> extract_task >> transform_task >> quality_task >> load_task >> validate_task