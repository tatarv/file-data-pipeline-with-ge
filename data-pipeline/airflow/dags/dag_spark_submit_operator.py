from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'spark',
    'retries': 0,
}

with DAG(
    dag_id="spark_submit_operator_example",
    description='A simple DAG to demonstrate SparkSubmitOperator',
    default_args=default_args,
    start_date=datetime.now(),
    catchup=False, 
    schedule_interval=None,       
) as dag:

    start = DummyOperator(task_id="start", dag=dag)

    spark_task = SparkSubmitOperator(
        task_id='spark_task',
        application='/opt/airflow/dags/spark_job/spark_submit_operator.py',  # Caminho para o arquivo do job Spark
        conn_id='spark_default',  # ID da conexão do Spark definida no Airflow
        name='spark_example_job',  # Nome do job Spark
        dag=dag,
    )

    end = DummyOperator(task_id="end", dag=dag)

start >> spark_task >> end