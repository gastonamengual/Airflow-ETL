from airflow.providers.sqlite.operators.sqlite import SqliteOperator

sqllite_operator = SqliteOperator(
    task_id='read_table',
    sqlite_conn_id='sqlite_default',
    sql='SELECT * FROM sales',
)