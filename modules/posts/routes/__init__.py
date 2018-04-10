# coding=utf-8
from flask import Blueprint
from config import API_VERSION
from ..controllers import *

# Routers blueprint
post_routes = Blueprint("post_routes", __name__, url_prefix="/{0}".format(API_VERSION))

post_routes.add_url_rule(
    "/posts",
    endpoint="get_all_post",
    view_func=get_all_post,
    methods=['GET'])

post_routes.add_url_rule(
    "/posts",
     endpoint="create_post",
     view_func=create_post,
     methods=['POST'])

post_routes.add_url_rule(
    "/posts/<id>",
    endpoint="get_post",
    view_func=get_post,
    methods=['GET'])

post_routes.add_url_rule(
    "/posts/<id>",
    endpoint="update_post",
    view_func=update_post,
    methods=['PUT'])

post_routes.add_url_rule(
    "/posts/<id>",
    endpoint="delete_post",
    view_func=delete_post,
    methods=['DELETE'])
