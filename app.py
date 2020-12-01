from flask import Flask, render_template
from Api.api import api
from containerman import ContainerMan as cm 


app = Flask(__name__)
app.register_blueprint(api, url_prefix="/api")


# Todo: implement simple authentication 
@app.route("/")
def index():
    stats = cm.DockerInfo()
    active:str = stats["running_containers"]
    stopped:str = stats["stopped_containers"]
    total:str = str(cm.AllContainers())

    return render_template("index.html",active=active,stopped=stopped,total=total)



