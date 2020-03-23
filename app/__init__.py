from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
#lower case config is name of the python module config.py
#upper case Config is the class Config
app.config.from_object(Config)
db = SQLAlchemy(app) #represents database
migrate = Migrate(app, db) #represents migration engine

from app import routes, models