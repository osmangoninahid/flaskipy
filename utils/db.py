# coding=utf-8
from flask_sqlalchemy import SQLAlchemy


def connect_to_db(app, db_uri="postgres://uaqklaqg:q9mPWIe3uYXDgVTLRt1r3WTs9201fxvW@stampy.db.elephantsql.com:5432/uaqklaqg"):
    """Connect the database to Flask app."""

    db = SQLAlchemy()
    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)

