#this configuration holds all configuraitons for the app
#configuration settings are defined as class variables inside the config class
#flask uses value of the secret key as a cryptographic key useful to generate signatoures or tokens
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #good practice to set configuration from environment variables
    #provide fallback value when environment doens't define variable
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')#server
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)#port 
    MAIL_USE_TLS= os.environ.get('MAIL_USE_TLS') is not None #boolean flag
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')#optional username
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')#optional password
    ADMINS=['dougcueva@gmail.com']