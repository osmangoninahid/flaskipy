# coding=utf-8
from flask import Flask, Blueprint
from config import API_PREFIX, API_VERSION
from ..controllers import *


posts_app = Flask(__name__)
# Configurations
posts_app.config.from_object('config')

@posts_app.errorhandler(404)
def not_found(error):
    return "Error Message: {0}".format(error)

# Routes Register
flaskipy_post = Blueprint("flaskipy_post", __name__, url_prefix="/{0}/{1}".format(API_PREFIX, API_VERSION))
flaskipy_post.add_url_rule("/posts", endpoint="get", view_func=get, methods=['GET'])
posts_app.register_blueprint(flaskipy_post)
