import duckdb

conn = duckdb.connect("./data/dbt_db.duckdb")

# init sql commands
conn.execute("CREATE TABLE transactions AS SELECT * FROM 'data/transactions.parquet'")
conn.execute(
    "CREATE TABLE warmups AS SELECT transaction_id, customer_id, product_category, amount FROM transactions"
)

# CRUD SQL commands in datagrip
commands = """
INSERT INTO warmups VALUES (50001, 4000, 'Clothing', 50)
INSERT INTO warmups VALUES (50002, 4001, 'Electronics', 30)
INSERT INTO warmups VALUES (50003, 4002, 'Books', 20);

SELECT * FROM warmups WHERE transaction_id IN (50001, 50002, 50003);

UPDATE warmups SET amount = 60 WHERE transaction_id = 50001

DELETE FROM warmups WHERE transaction_id = 50002;
"""
