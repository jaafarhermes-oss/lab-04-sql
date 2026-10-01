# Lab 04: Working with SQL

This folder contains the required files for the DS2022 SQL lab.

## Required files

- `initialize.sql` creates related `users` and `posts` tables and inserts 10 rows into each.
- `media_query.sql` uses a JOIN and WHERE clause.
- `media_results.txt` shows the expected output from that query.
- `MOCK_DATA.csv` contains 200 mock records.
- `src/sql_lab/process.py` cleans and uploads the CSV to MySQL.
- `src/sql_lab/query.py` queries the uploaded `mock` table.

## Before running

Replace `COMPUTING_ID` with your UVA computing ID in the shell commands from the assignment.

```bash
cd ~/ds2022-fall-2026/lab-04-sql
uv init --name "sql_lab" --description "sql work for DS2022"
uv add mysql-connector-python pandas
```

If you already initialized the project, do not run `uv init` again.

## Case Study 1

```bash
export MYSQL_PWD='COMPUTING_ID'
mycli -h ds2022.cgls84scuy1e.us-east-1.rds.amazonaws.com -P 3306 -u COMPUTING_ID -D COMPUTING_ID_media < initialize.sql

export MYSQL_PWD='COMPUTING_ID'
mycli -h ds2022.cgls84scuy1e.us-east-1.rds.amazonaws.com -P 3306 -u COMPUTING_ID -D COMPUTING_ID_media < media_query.sql > media_results.txt
```

## Case Study 2

Set the database environment variables:

```bash
export DBHOST='ds2022.cgls84scuy1e.us-east-1.rds.amazonaws.com'
export DBUSER='COMPUTING_ID'
export DBPASS='COMPUTING_ID'
export DBNAME='COMPUTING_ID_mock'
```

Then run:

```bash
uv run python src/sql_lab/process.py
```

Check the database:

```bash
export MYSQL_PWD='COMPUTING_ID'
mycli -h ds2022.cgls84scuy1e.us-east-1.rds.amazonaws.com -P 3306 -u COMPUTING_ID -D COMPUTING_ID_mock
```

Inside MySQL:

```sql
SHOW TABLES;
DESCRIBE mock;
SELECT COUNT(*) FROM mock;
SELECT * FROM mock LIMIT 5;
```

Finally:

```bash
uv run python src/sql_lab/query.py
```

## Note

The course database is student-specific, so the SQL scripts that connect to MySQL must be run with your own UVA computing ID. The local files are ready, but I cannot truthfully claim the remote database execution succeeded until you run those commands.
