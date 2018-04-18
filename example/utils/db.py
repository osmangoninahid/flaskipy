# coding=utf-8
from flask_sqlalchemy import SQLAlchemy
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


def connect_to_db(app):
    """Connect the database to Flask app."""
    db_uri = "postgres://{0}:{1}@{2}:{3}/{4}".format(
        DB_USER,
        DB_PASSWORD,
        DB_HOST,
        DB_PORT,
        DB_NAME)

    db = SQLAlchemy()
    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
