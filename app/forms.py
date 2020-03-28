"""
    FLASK-WTF uses python classes to represent web forms
    a form class defines fields of the form as class variables

"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

#this is my login form
class LoginForm(FlaskForm):
    #data validators argument is used to attach validation behaviors to field
    #dataRequired validator simply checks that the field is not submitted empty
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')


#this is my regsitration form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    #will be asking user password twice to avoid typos
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Register')

    def validate_username(self, username):
        """
            To be used as a custom validator by WTF-Forms.

            WTF-Forms will take antyhing in the form of validate_<field_name>
            as a custom validator. It invokes them in addtion to the stock validators.
            These methods are to make sure that username and email aren't already in 
            the database.
            So, these methods issue database queries looking for no results.
            Validation error is raised if a result exists. 
        """
        user = User.query.filter_by(username=username.data).first()
        #an if statement looking to see if username already taken
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user= User.query.filter_by(email=email.data).first()
        #an if statement looking to see if email already taken
        if user is not None:
            raise ValidationError('Please use different email address.')