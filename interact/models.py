from interact import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

users_contact_users = db.Table('users_contact_users',
                               db.Column('user_id', db.Integer, db.ForeignKey('User.id')),
                               db.Column('user_id', db.Integer, db.ForeignKey('User.id'))
                               )


class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    linkedin_url = db.Column(db.String(120), unique=True, nullable=False)
    color = (db.Column(db.String(120), unique=True, nullable=True))
    phone_number = (db.Column(db.String(20), unique=True, nullable=True))
    title = (db.Column(db.String(250), unique=False, nullable=False))
    image_url = (db.Column(db.String(250), unique=False, nullable=False))
    access_token = (db.Column(db.String(2500), unique=True, nullable=False))
    children = db.relationship("User",
                               secondary=users_contact_users)

    def __init__(self, name, linkedin_url, color, phone_number, title, image_url, access_token):
        self.name = name
        self.linkedin_url = linkedin_url
        self.color = color
        self.phone_number = phone_number
        self.title = title
        self.image_url = image_url
        self.access_token = access_token
