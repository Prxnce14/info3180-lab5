# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime

class movietemp(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255),  unique=True)
    description = db.Column(db.Text)
    poster = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)



def __init__(self, title, desc, post, time):
        self.title= title
        self.description = desc
        self.poster = post
        self.created_at = time


def __repr__(self):
        return '<movietemp %r>' % self.title
