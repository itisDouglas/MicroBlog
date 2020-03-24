from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        #this tells python how to pritn objects of this class
        return '<User {}>'.format(self.username)

class Post(db.Model):
    """
        REpresents blog posts written by users.
        You'll want to work with UTC dates and times in a server app.
        user_id is a foreign that connects with user.id
        Backref argument defines name of filed that will be added to objects of the "many" class that points back at the "one" object.
        the 'lazy' argument defines how db query for relationship will be issues
    """
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post> {}'.format(self.body)