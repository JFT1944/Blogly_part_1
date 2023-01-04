"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
db = SQLAlchemy()

def connect_db(app):

    db.app = app
    db.init_app(app)




# models below
class User(db.Model):
    '''User'''

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
                    
    first_name = db.Column(db.String(50), nullable=False, unique=True)

    last_name = db.Column(db.String(50), nullable=False, unique=True)

    image_url = db.Column(db.String(150), nullable=True)