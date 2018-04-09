from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Post(db.Model):
    """A Post class"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    slug = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    author = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    status = db.Column(db.Text, nullable=True)
    meta_data = db.Column(db.JSON, nullable=True)

    def __init__(self, title, description=None):
        self.title = title
        self.description = description

    def __repr__(self):
        """Display when printing a Post object"""

        return "<Post: {}>".format(self.name)

    def as_dict(self):
        """Convert object to dictionary"""

        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
