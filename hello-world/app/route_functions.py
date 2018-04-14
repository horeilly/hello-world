from app.models import Bond
from sqlalchemy import func
import app.utils


def get_all_bonds():
    data = Bond.query.all()
    return app.utils.convert_model_to_json(data)


def retrieve_bond(bond_name):
    data = Bond.query.filter(
        func.lower(Bond.company) == bond_name.lower()).all()
    return app.utils.convert_model_to_json(data)


def load_bond(data):
    query = (
        "INSERT INTO"
        "  bonds "
        "VALUES ("
        "  '{date}',"
        "  '{company}',"
        "  {overnight},"
        "  {_7_day},"
        "  {_15_day},"
        "  {_30_day},"
        "  {_60_day},"
        "  {_90_day}"
        ")".format(**data)
    )
    app.utils.postgres_query(query)
    return data
