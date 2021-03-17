# Routes return pure json

from flask import Blueprint,request
from flask.json import jsonify
from containerman import ContainerMan as cm

api = Blueprint("api", __name__)

# @api.route("/containers", methods=["GET"])
# def index():



@api.route("/containers/running",methods=["GET"])
def running():
    containers  =  cm.DockerInfo()
    running_containers = containers['running_containers']
    jsonresp = {"containers":running_containers}
    return jsonify(jsonresp)


@api.route("/containers/all", methods=["GET"])
def all():
	all_containers = cm.AllContainers()
	jsonresp  = {"all_containers":all_containers}
	return jsonify(jsonresp)


# @api.route("images/pull",methods=["POST"])
# def pull():
#     ImageName =  request.data["image"]
    
    
