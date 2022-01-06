"""Blogly Models"""
import datetime
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

    posts = db.relatioship("Post", backref="user", cascade="all, delete-orphan")

    @property
    def full_name(self):
        """Returns User's name"""
        return f"{self.first_name} {self.last_name}"
    
class Post(db.Model):
    """Blog Posts on site."""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                    primary_key=True)

    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                 default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"),
                       nullable=False)

    @property
    def show_friendly_date(self):
        """Returns a pleasant format for date"""
        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")
    
    
