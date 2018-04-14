# coding=utf-8
from flask import Blueprint
from config import API_VERSION
from ..controllers import *

# Routers blueprint
blogs_route = Blueprint("blogs_route", __name__, url_prefix="/{0}".format(API_VERSION))

blogs_route.add_url_rule(
    "/blogs",
    endpoint="index",
    view_func=index,
    methods=['GET'])

blogs_route.add_url_rule(
    "/blogs",
     endpoint="create",
     view_func=create,
     methods=['POST'])

blogs_route.add_url_rule(
    "/blogs/<int:id>",
    endpoint="get",
    view_func=get,
    methods=['GET'])

blogs_route.add_url_rule(
    "/blogs/<int:id>",
    endpoint="update",
    view_func=update,
    methods=['PUT'])

blogs_route.add_url_rule(
    "/blogs/<int:id>",
    endpoint="delete",
    view_func=delete,
    methods=['DELETE'])
