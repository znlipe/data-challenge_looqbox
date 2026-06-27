import pandas as pd
import database as db


def retrieve_data(product_code: int = None, store_code: int = None, date=None):
    connection = db.get_connection()

    try:
        query = """
                SELECT *
                FROM data_product_sales
                """

        conditions = []
        params = []

        if product_code is not None:
            conditions.append("PRODUCT_CODE = %s")
            params.append(product_code)

        if store_code is not None:
            conditions.append("STORE_CODE = %s")
            params.append(store_code)

        if date is not None and len(date) != 2:
            raise ValueError("Date should be a list with two elements")

        if date is not None:
            conditions.append("DATE BETWEEN %s AND %s")
            params.extend([date[0], date[1]])

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        result = pd.read_sql(query, connection, params=params)
        return result

    finally:
        connection.close()


if __name__ == "__main__":
    my_data = retrieve_data(
        product_code=172,
        store_code=2
    )
    print(my_data)