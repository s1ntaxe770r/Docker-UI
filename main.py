from flask import Flask 
import docker



app =  Flask(__name__)

@app.route("/")
def index():
    return "hi"

if __name__ == "__main__":
    app.run(debug=True)




















