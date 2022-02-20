from crypt import methods
from enum import unique
from flask import Flask, request 
from flask_wtf import FlaskForm
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "its secret"
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "sqlite:///" + os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app) #database instance


@app.route('/')
def index():
    request.get_data()
    return "<h1>Hi!</h1>"

#  >>> app.url_map
@app.route("/user/<name>", methods=["GET", "POST"])
def user(name):
    return "hello {}".format(name)

@app.route('/render')
def render():
    return ""

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    users = db.relationship("Operation", backref="user")
    def __repr__(self):
        return "<User %r>"


class Operation(db.Model):
    __tablename__ = "operations"
    id = db.Column(db.Integer, primary_key = True)
    operation = db.Column(db.String(64), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))  #db
    def __repr__(self):
        return "<Operation %r>" % self.operation
