from airflow_etl.extract import sqllite_operator
from unittest.mock import MagicMock

def test_sqqlite_operator():
    sqllite_operator.execute()