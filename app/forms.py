"""
    FLASK-WTF uses python classes to represent web forms
    a form class defines fields of the form as class variables

"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

#this is my login form
class LoginForm(FlaskForm):
    #data validators argument is used to attach validation behaviors to field
    #dataRequired validator simply checks that the field is not submitted empty
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')