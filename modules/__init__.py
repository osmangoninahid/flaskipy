# coding=utf-8
from .posts import flaskipy_post
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def connect_to_db(app, db_uri="postgres://uaqklaqg:q9mPWIe3uYXDgVTLRt1r3WTs9201fxvW@stampy.db.elephantsql.com:5432/uaqklaqg"):
    """Connect the database to Flask app."""
    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)

if __name__ == '__main__':
    connect_to_db(app)
