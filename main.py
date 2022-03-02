from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    request.get_data()
    return "<h1>Hi!</h1>"

@app.route("/user/<name>", methods=["GET"])
def user(name):
    return "hello {}".format(name)