# coding=utf-8
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt(Flask(__name__))


class User(db.Model):
    """A User class"""

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.Text, unique = True, nullable=False)
    full_name = db.Column(db.Text,nullable=True)
    email = db.Column(db.Text,nullable=True)
    password = db.Column(db.Text,nullable=False)
    status = db.Column(db.Text, nullable=True)
    meta_data = db.Column(db.JSON, nullable=True)

    def __init__(self, user_name, password, full_name=None, email=None, status="Active", meta_data=None):
        self.user_name = user_name
        self.full_name = full_name
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.status = status
        self.meta_data = meta_data

    @staticmethod
    def verify_password(pw_hash,password):
        return bcrypt.check_password_hash(pw_hash, password)

    @staticmethod
    def generate_pwd_hash(password):
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def __repr__(self):
        """Display when printing a User object"""

        return "<User: {}>".format(self.user_name)

    def as_dict(self):
        """Convert object to dictionary"""

        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
