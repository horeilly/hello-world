import os
import psycopg2


def get_conn_string_parameters():
    return {
      "dbname": "api",
      "user": os.environ["USER"],
      "host": "127.0.0.1",
      "password": ""
    }


def postgres_query(query, data=True):
    dsn_params = get_conn_string_parameters()
    dsn = "dbname='{dbname}' user='{user}' host='{host}' password='{password}'"
    conn = psycopg2.connect(dsn.format(**dsn_params))
    cur = conn.cursor()
    cur.execute(query)
    if data:
        rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    if data:
        return rows
    else:
        return None
