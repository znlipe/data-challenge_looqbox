import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
import database as db


def df_cad():
    connection = db.get_connection()

    try:
        # Query 1 provided by the client.
        df = pd.read_sql(
            f"""
            SELECT
                STORE_CODE,
                STORE_NAME,
                START_DATE,
                END_DATE,
                BUSINESS_NAME,
                BUSINESS_CODE
            FROM data_store_cad""",
            connection
        )
        return df
    finally:
        connection.close()


def df_sales():
    connection = db.get_connection()

    # Period requested by the client.
    # the filter is applied in Pandas later on.
    client_period = pd.to_datetime(['2019-10-01', '2019-12-31'])

    try:
        # Query 2 provided by the client.
        query = """
                SELECT STORE_CODE,
                       DATE,
                       SALES_VALUE,
                       SALES_QTY
                FROM data_store_sales
                WHERE DATE BETWEEN '2019-01-01' AND '2019-12-31'
                """

        df = pd.read_sql(query, connection)

        # Ensures date comparisons are made between datetime values.
        df['DATE'] = pd.to_datetime(df['DATE'])

        filtered_df = df[
            (df["DATE"] >= client_period[0]) &
            (df["DATE"] <= client_period[1])
            ]
        return filtered_df

    finally:
        connection.close()


# Final Table
def build_client_visualization():
    # Combines sales data with store metadata using STORE_CODE.
    merged = pd.merge(
        left=df_sales(),
        right=df_cad(),
        on=['STORE_CODE'],
        how='inner'
    )

    # Calculate the ticket average (TM) for each sales record.
    merged['TM'] = merged['SALES_VALUE'] / merged['SALES_QTY']

    # Aggregates TM by store and business category to match the requested output.
    visualizer_df = (
        merged.groupby(['STORE_NAME', 'BUSINESS_NAME'], as_index=False)
        ["TM"].mean()
    )
    visualizer_df['TM'] = visualizer_df["TM"].round(2)

    visualizer_df = visualizer_df.rename(
        columns={
            "STORE_NAME": "Loja",
            "BUSINESS_NAME": "Categoria"
        }
    )
    return visualizer_df


if __name__ == "__main__":
    my_data = build_client_visualization()
    print(my_data)
