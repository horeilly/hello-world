import json
import os


class Config(object):

    creds_path_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)))
    db_path = os.path.abspath(
        os.path.dirname(__file__)
    )
    creds_path = os.path.join(creds_path_dir, "credentials.json")
    with open(creds_path, "r") as f:
        creds = json.load(f)

    POSTGRES_USER = creds["POSTGRES_USER"]
    POSTGRES_PW = creds["POSTGRES_PW"]
    POSTGRES_HOST = creds["POSTGRES_HOST"]
    POSTGRES_DB = "api"

    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(db_path, "app.db")
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{}:{}@{}/{}".format(
        POSTGRES_USER, POSTGRES_PW, POSTGRES_HOST, POSTGRES_DB)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ""
