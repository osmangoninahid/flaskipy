# coding=utf-8
from flask import Blueprint
from config import API_VERSION
from ..controllers import *

# Routers blueprint
user_routes = Blueprint("user_routes", __name__, url_prefix="/{0}".format(API_VERSION))

user_routes.add_url_rule(
    "/users",
    endpoint="get_all_user",
    view_func=get_all_user,
    methods=['GET'])

user_routes.add_url_rule(
    "/users",
     endpoint="add_user",
     view_func=add_user,
     methods=['POST'])

user_routes.add_url_rule(
    "/users/<id>",
    endpoint="get_user",
    view_func=get_user,
    methods=['GET'])

user_routes.add_url_rule(
    "/users/<id>",
    endpoint="update_user",
    view_func=update_user,
    methods=['PUT'])

user_routes.add_url_rule(
    "/users/<id>",
    endpoint="delete_user",
    view_func=delete_user,
    methods=['DELETE'])
