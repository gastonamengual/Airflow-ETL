from airflow import DAG
from .etl_example.extract import sqllite_operator

with DAG(
    dag_id='etl_dag'
) as dag:
    sqllite_operator