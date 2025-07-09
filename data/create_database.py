import duckdb


def create_database():
    db_path = "data/local_db.duckdb"
    conn = duckdb.connect(db_path)

    transactions = conn.execute("select * from 'data/transactions.csv'").fetchall()

    print(transactions)


# create_database()
