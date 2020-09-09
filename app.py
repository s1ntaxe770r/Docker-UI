from flask import Flask ,render_template
from Api.api import api_route
import docker


app =  Flask(__name__)
app.register_blueprint(api_route,url_prefix='/api')


@app.route("/")
def index():

	return "WIP"



















