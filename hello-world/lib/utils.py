import json
import os
import psycopg2


def connect_to_postgres(db):
    creds_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)))
    creds_path = os.path.join(creds_dir, "credentials.json")
    with open(creds_path, "r") as f:
        creds = json.load(f)

    dsn_params = {
      "dbname": db,
      "user": creds["POSTGRES_USER"],
      "host": creds["POSTGRES_HOST"],
      "password": creds["POSTGRES_PW"]
    }
    dsn = "dbname='{dbname}' user='{user}' host='{host}' password='{password}'"
    conn = psycopg2.connect(dsn.format(**dsn_params))
    return conn


# FIXME: Handle this better
def postgres_query(query):
    conn = connect_to_postgres("api")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    cur.execute(query)
    try:
        rows = cur.fetchall()
        columns = [col[0] for col in cur.description]
    except psycopg2.ProgrammingError:
        rows, columns = None, None
    cur.close()
    conn.close()
    return rows, columns
