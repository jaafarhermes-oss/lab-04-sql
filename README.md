# Lab 04: Working with SQL


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

