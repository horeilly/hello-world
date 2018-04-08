from flask import Flask, request
from flask_restful import Resource, Api
import lib.load_data as ld

app = Flask(__name__)
api = Api(app)


bonds = {}


class Bond(Resource):

    @staticmethod
    def get(bond_name):
        return ld.retrieve_bond(bond_name)

    @staticmethod
    def post(bond_name):
        data = request.json
        data["company"] = bond_name.upper()
        ld.load_bond(data)
        return data


api.add_resource(Bond, "/new/bond/<string:bond_name>")


if __name__ == "__main__":
    app.run(debug=True)

