from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager #works with application's user model

app = Flask(__name__)
#lower case config is name of the python module config.py
#upper case Config is the class Config
app.config.from_object(Config)
db = SQLAlchemy(app) #represents database
migrate = Migrate(app, db) #represents migration engine
login = LoginManager(app)
login.login_view = 'login' #redirect user to login form if want to see restricted page
#similar to url_for() call

from app import routes, models