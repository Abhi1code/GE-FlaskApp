from flask import Flask, request, jsonify, json
import logging as logger
logger.basicConfig(level="DEBUG")

app = Flask(__name__)

# if __name__ == '__main__':
#     logger.debug("starting the application")
#     from api import *
#     app.run(host="127.0.0.1", port=5000, debug=True, load_dotenv=True)

@app.route("/")
def hello():
    return "Hello world;"


@app.route('/login/', methods=["GET", "POST"])
def login_page():

        if request.method == "GET":
            key = request.json['key']
            # attempted_password = request.form['password']
            return {"message" : "inside get method " + key}

        if request.method == "POST":
            key = request.json['key']
            # attempted_password = request.form['password']
            return {"message" : "inside post method " + key}


app.run(host='0.0.0.0')