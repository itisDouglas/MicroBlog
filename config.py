#this configuration holds all configuraitons for the app
#configuration settings are defined as class variables inside the config class
#flask uses value of the secret key as a cryptographic key useful to generate signatoures or tokens
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'