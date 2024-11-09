import sys
from pathlib import Path

# Add the project root to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from etl.extract import extract_data


def on_failure_callback(**context):
    print(f"Task {context['task_instance_key_str']} failed.")


default_args = {
    "owner": "chiba",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "on_failure_callback": on_failure_callback,
}

with DAG(
    dag_id="f1_etl_v01",
    default_args=default_args,
    schedule_interval="0 15 * * 1",
    start_date=datetime(2024, 11, 9),
    tags=["etl"],
    catchup=False,
) as dag:
    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract_data,
        dag=dag,
    )

    extract_task
