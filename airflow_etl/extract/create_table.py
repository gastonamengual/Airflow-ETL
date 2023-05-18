import sqlite3

# create a database connection and cursor
conn = sqlite3.connect("sales.db")
c = conn.cursor()

# create a table to store our data
c.execute(
    """
          CREATE TABLE sales (
              id INTEGER PRIMARY KEY,
              date DATE,
              product TEXT,
              price FLOAT
          )
          """
)

c.execute(
    """
          INSERT INTO sales (date, product, price)
          VALUES
              ('2023-01-01', 'Product A', 100.0),
              ('2023-01-02', 'Product B', 150.0),
              ('2023-01-03', 'Product A', 200.0),
              ('2023-01-04', 'Product C', 75.0),
              ('2023-01-05', 'Product B', 120.0),
              ('2023-01-06', 'Product C', 90.0),
              ('2023-01-07', 'Product A', 180.0),
              ('2023-01-08', 'Product B', 130.0),
              ('2023-01-09', 'Product C', 80.0),
              ('2023-01-10', 'Product A', 190.0)
          """
)

conn.commit()
conn.close()
