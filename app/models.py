# Add any model classes for Flask-SQLAlchemy here
from . import db

class MovieForm(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),  unique=True)
    description = db.Column(db.String(255))
    num_rooms = db.Column(db.Integer)
    num_brooms = db.Column(db.Integer)
    price = db.Column(db.String(255))
    ptype =  db.Column(db.String(255))
    location = db.Column(db.String(255))
    pname = db.Column(db.String(255))
