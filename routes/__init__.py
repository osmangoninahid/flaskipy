# coding=utf-8
from flask import Flask, Blueprint
from config import API_PREFIX, API_VERSION
from modules import posts_app


app = Flask(__name__)
# Configurations
app.config.from_object('config')

@app.errorhandler(404)
def not_found(error):
    return "Error Message: {0}".format(error)

# Routes Register
# flaskipy = Blueprint("flaskipy", __name__, url_prefix="/{0}".format(API_VERSION))
# flaskipy.add_url_rule("/search", endpoint="home", view_func=home, methods=['GET'])
app.register_blueprint(posts_app)
