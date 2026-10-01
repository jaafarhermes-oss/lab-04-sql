

import logging
import os

import mysql.connector

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

DBHOST = os.getenv("DBHOST")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
DBNAME = os.getenv("DBNAME")


def get_connection():
    return mysql.connector.connect(
        host=DBHOST,
        user=DBUSER,
        password=DBPASS,
        database=DBNAME,
    )


def get_data_by_group(value):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM mock WHERE `group` = %s"
        cursor.execute(query, (value,))
        rows = cursor.fetchall()

        logging.info("Found %d rows for group '%s'.", len(rows), value)
        return rows

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)
        raise

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


def plot_counts(groupby):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()


        cursor.execute("SHOW COLUMNS FROM mock")
        valid_columns = {row[0] for row in cursor.fetchall()}

        if groupby not in valid_columns:
            raise ValueError(f"Invalid column name: {groupby}")
        query = f"SELECT `{groupby}`, COUNT(*) FROM mock GROUP BY `{groupby}`"
        cursor.execute(query)
        rows = cursor.fetchall()

        logging.info("Calculated counts grouped by '%s'.", groupby)
        return rows

    except (mysql.connector.Error, ValueError) as error:
        logging.error("Query error: %s", error)
        raise

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


def main():
    rows = get_data_by_group("alpha")
    print("Rows in group 'alpha':")
    for row in rows[:5]:
        print(row)

    counts = plot_counts("city")
    print("\nCounts by city:")
    for value, count in counts:
        print(f"{value}: {count}")


if __name__ == "__main__":
    main()
