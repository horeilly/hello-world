import lib.utils


def get_all_bonds():
    query = "SELECT * FROM bonds;"
    rows, columns = lib.utils.postgres_query(query)
    rows = [(row[0].strftime("%Y-%m-%d"),) + row[1:] for row in rows]
    results = [{k: v for k, v in zip(columns, row)} for row in rows]
    return results


def retrieve_bond(bond_name):
    query = "SELECT * FROM bonds WHERE LOWER(company) = '{}'".format(bond_name)
    rows, columns = lib.utils.postgres_query(query)
    rows = [(row[0].strftime("%Y-%m-%d"),) + row[1:] for row in rows]
    results = [{k: v for k, v in zip(columns, row)} for row in rows]
    return results


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
