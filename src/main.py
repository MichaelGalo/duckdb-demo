import duckdb


def main():
    conn = duckdb.connect("./data/dbt_db.duckdb")


if __name__ == "__main__":
    main()
