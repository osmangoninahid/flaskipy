# coding=utf-8
from flask import Flask, jsonify
from .posts import post_routes
from .users import user_routes
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configurations
app.config.from_object('config')

@app.errorhandler(404)
def not_found(error):
    # return "Error Message: {0}".format(error)
    response = {
        'success': False,
        'message': "Error Message: {0}".format(error)
    }

    return jsonify(response), 404

def connect_to_db(app, db_uri="postgres://uaqklaqg:q9mPWIe3uYXDgVTLRt1r3WTs9201fxvW@stampy.db.elephantsql.com:5432/uaqklaqg"):
    """Connect the database to Flask app."""
    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)

connect_to_db(app)

# Routes Register
# register post routers
app.register_blueprint(post_routes)
app.register_blueprint(user_routes)
