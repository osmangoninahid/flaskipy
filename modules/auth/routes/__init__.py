# coding=utf-8
from flask import Blueprint
from config import API_VERSION
from ..controllers import *

# Routers blueprint
auth_routes = Blueprint("auth_routes", __name__, url_prefix="/{0}".format(API_VERSION))

auth_routes.add_url_rule(
    "/login",
     endpoint="login",
     view_func=login,
     methods=['POST'])

auth_routes.add_url_rule(
    "/signup",
     endpoint="signup",
     view_func=signup,
     methods=['POST'])
