from flask import Flask, render_template
from Api.api import api


app = Flask(__name__)
app.register_blueprint(api, url_prefix="/api")


@app.route("/")
def index():

    return "WIP"
