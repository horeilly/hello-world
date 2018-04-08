from flask import Flask, request, jsonify
import lib.route_functions as rf
import lib.utils

app = Flask(__name__)
#
# db_params = {
#   "url": lib.utils.get_env_variable("POSTGRES_URL"),
#   "user": lib.utils.get_env_variable("POSTGRES_USER"),
#   "pw": lib.utils.get_env_variable("POSTGRES_PW"),
#   "db": lib.utils.get_env_variable("POSTGRES_DB")
# }
# db_url = "postgresql+psycopg2://{user}:{pw}@{url}/{db}".format(**db_params)


@app.route("/bonds")
def get_all_bonds():
    return jsonify(rf.get_all_bonds())


@app.route("/bonds/<string:bond_name>", methods=["GET", "POST"])
def bond(bond_name):
    if request.method == "GET":
        return jsonify(rf.retrieve_bond(bond_name))
    elif request.method == "POST":
        data = request.json
        data["company"] = bond_name.upper()
        rf.load_bond(data)
        return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)

