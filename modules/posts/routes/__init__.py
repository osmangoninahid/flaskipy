# coding=utf-8
from flask import Flask, Blueprint
from config import API_VERSION
from ..controllers import *


posts_app = Flask(__name__)
# Configurations
posts_app.config.from_object('config')

@posts_app.errorhandler(404)
def not_found(error):
    return "Error Message: {0}".format(error)

# Routers blueprint
flaskipy_post = Blueprint("flaskipy_post", __name__, url_prefix="/{0}".format(API_VERSION))

flaskipy_post.add_url_rule(
    "/posts",
    endpoint="index",
    view_func=index,
    methods=['GET'])

flaskipy_post.add_url_rule(
    "/posts",
     endpoint="create",
     view_func=create,
     methods=['POST'])

flaskipy_post.add_url_rule(
    "/posts/<id>",
    endpoint="get",
    view_func=get,
    methods=['GET'])

flaskipy_post.add_url_rule(
    "/posts/<id>",
    endpoint="update",
    view_func=update,
    methods=['PUT'])

flaskipy_post.add_url_rule(
    "/posts/<id>",
    endpoint="delete",
    view_func=delete,
    methods=['DELETE'])
