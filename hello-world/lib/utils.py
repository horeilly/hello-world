import os
import psycopg2


def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        raise KeyError("Expected variable {} to be in the environment."
                       "".format(name))


def connect_to_postgres(db):
    dsn_params = {
      "dbname": db,
      "user": get_env_variable("POSTGRES_USER"),
      "host": get_env_variable("POSTGRES_HOST"),
      "password": get_env_variable("POSTGRES_PW")
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
