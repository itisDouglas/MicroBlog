from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin #flask-login provides this mixin class. works with user model
from hashlib import md5

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        #this tells python how to pritn objects of this class
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size
        )

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


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    #user_loader is registered with flask-login with its decorator
    #id that flask-login passes to function is going to be a string
    #so databases that use numeric IDS need to conver the string to intenger as yous ee