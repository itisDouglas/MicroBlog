from flask import Flask
from config import Config

app = Flask(__name__)
#lower case config is name of the python module config.py
#upper case Config is the class Config
app.config.from_object(Config)

from app import routes