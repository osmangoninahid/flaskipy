from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A User class"""

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    full_name = db.Column(db.Text)
    email = db.Column(db.Text)
    status = db.Column(db.Text, nullable=True)
    meta_data = db.Column(db.JSON, nullable=True)
    password = db.Column(db.Text)

    def __init__(self, username, password):
        self.username = title
        self.password = password

    def __repr__(self):
        """Display when printing a User object"""

        return "<User: {}>".format(self.name)

    def as_dict(self):
        """Convert object to dictionary"""

        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
