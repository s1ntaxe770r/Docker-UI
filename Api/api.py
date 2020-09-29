# Routes return pure json

from flask import Blueprint
from flask.json import jsonify
from containerman import ContainerMan as cm

api = Blueprint("api", __name__)

# @api.route("/containers", methods=["GET"])
# def index():


@api.route("/containers/running", methods=["GET"])
def running():
    containers = cm.DockerInfo()
    running_containers = containers["running_containers"]

    json = {"containers": running_containers}
    return jsonify(json)
