import duckdb

conn = duckdb.connect("local_db.duckdb")
conn.execute("CREATE TABLE transactions AS SELECT * FROM 'data/transactions.parquet'")


def main():
    print("Hello World!")


if __name__ == "__main__":
    main()
