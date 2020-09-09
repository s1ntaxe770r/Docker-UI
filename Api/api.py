# Routes return pure json

from flask import Blueprint
from flask.json import jsonify

api_route = Blueprint("api_route", __name__)


@api_route.route("/containers", methods=["GET"])
def index():
    test = {"fake": "json"}
    return jsonify(test)
