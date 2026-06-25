import os

import mysql.connector as sql
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

# Connection
def get_connection():
    try:
        return sql.connect(
            host= os.getenv("MYSQL_HOST"),
            user = os.getenv("MYSQL_USER"),
            password = os.getenv("MYSQL_PASSWORD"),
            database = os.getenv("MYSQL_DATABASE"),
        )
    except Error as e:
        print(f"Connection error: {e}")
        raise

if __name__ == "__main__":
    conn = get_connection()
    if conn.is_connected():
        print(f"Success! Connected to {conn.server_info}")
    conn.close()
