from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


bonds = {}


class Bond(Resource):

    @staticmethod
    def get(bond_name):
        return {bond_name: bonds[bond_name]}

    @staticmethod
    def post(bond_name):
        bonds[bond_name] = request.json
        bonds[bond_name]["coupon_payments"] = bonds[bond_name]["principal"] * bonds[bond_name]["coupon"]
        return {bond_name: bonds[bond_name]}


api.add_resource(Bond, "/new/bond/<string:bond_name>")


if __name__ == "__main__":
    app.run(debug=True)

