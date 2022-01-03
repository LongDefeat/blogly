"""Blogly Models"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DEFAULT_IMAGE_URL = ""

def connect_db(app):
    """Connects to app"""
    db.app = app
    db.init_app(app)

# MODELS GO BELOW HERE!

class User(db.Model):
    """User on site."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                    primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    user_photo = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        """Returns User's name"""
        return f"{self.first_name} {self.last_name}"
    