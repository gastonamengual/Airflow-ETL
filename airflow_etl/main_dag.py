from airflow import DAG
from airflow_etl.extract import sqllite_operator

with DAG(dag_id="etl_dag") as dag:
    sqllite_operator
