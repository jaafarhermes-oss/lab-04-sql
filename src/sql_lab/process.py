

import logging
import os

import mysql.connector
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

DBHOST = os.getenv("DBHOST")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
DBNAME = os.getenv("DBNAME")


def read_data(filename):
    logging.info("Reading data from %s", filename)
    data = pd.read_csv(filename)
    logging.info("Read %d rows.", len(data))
    return data


def clean_data(data):
    logging.info("Cleaning data.")
    cleaned = data.dropna().copy()
    logging.info("Rows after cleaning: %d", len(cleaned))
    return cleaned


def get_sql_type(dtype):
    dtype_name = str(dtype)

    type_mapping = {
        "int64": "BIGINT",
        "int32": "INT",
        "float64": "DOUBLE",
        "bool": "TINYINT(1)",
        "datetime64[ns]": "DATETIME",
        "object": "VARCHAR(255)",
        "string": "VARCHAR(255)",
    }

    return type_mapping.get(dtype_name, "VARCHAR(255)")


def load_data(data, table):
    logging.info("Connecting to MySQL database %s.", DBNAME)

    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME,
        )
        cursor = connection.cursor()


        columns = []
        for column in data.columns:
            sql_type = get_sql_type(data[column].dtype)
            escaped_column = f"`{column.replace('`', '``')}`"
            columns.append(f"{escaped_column} {sql_type}")

        create_sql = f"""
            CREATE TABLE IF NOT EXISTS `{table}` (
                {", ".join(columns)}
            )
        """
        cursor.execute(create_sql)


        column_names = ", ".join(
            f"`{column.replace('`', '``')}`" for column in data.columns
        )
        placeholders = ", ".join(["%s"] * len(data.columns))
        insert_sql = (
            f"INSERT INTO `{table}` ({column_names}) "
            f"VALUES ({placeholders})"
        )

        for row in data.itertuples(index=False, name=None):
            values = tuple(None if pd.isna(value) else value for value in row)
            cursor.execute(insert_sql, values)

        connection.commit()
        logging.info("Uploaded %d rows to %s.", len(data), table)

    except mysql.connector.Error as error:
        if connection is not None:
            connection.rollback()
        logging.error("Database error: %s", error)
        raise

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
            logging.info("Database connection closed.")


def main():
    data = read_data("MOCK_DATA.csv")
    cleaned = clean_data(data)
    load_data(cleaned, "mock")


if __name__ == "__main__":
    main()
