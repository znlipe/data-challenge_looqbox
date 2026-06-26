import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

from database import get_connection

def explore_table(table):
    connection = get_connection()

    try:
        print("\n" + "=" * 60)
        print(f"TABLE: {table}")
        print("=" * 60)

        describe = pd.read_sql(
            f"DESCRIBE {table}",
            connection
        )
        print(describe)

        print("\n" + "=" * 60)
        print("SAMPLE:")

        sample = pd.read_sql(
            f"SELECT * FROM {table} LIMIT 5",
            connection
        )
        print(sample)

    finally:
        connection.close()


def explore_tables(tables):
    for table in tables:
        explore_table(table)


if __name__ == "__main__":
    tables = [
        "IMDB_movies",
        "data_product",
        "data_product_sales",
        "data_store_cad",
        "data_store_sales"
    ]

    explore_tables(tables)
