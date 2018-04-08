import lib.utils


def get_all_bonds():
    query = "SELECT * FROM bonds;"
    rows = lib.utils.postgres_query(query)
    return [(row[0].strftime("%Y-%m-%d"),) + row[1:] for row in rows]


def retrieve_bond(bond_name):
    query = "SELECT * FROM bonds WHERE LOWER(company) = '{}'".format(bond_name)
    rows = lib.utils.postgres_query(query)
    rows = [(row[0].strftime("%Y-%m-%d"),) + row[1:] for row in rows]
    return rows


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
    lib.utils.postgres_query(query, False)
    return data
