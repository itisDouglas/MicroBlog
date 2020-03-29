#routes module holds the different URLs that the app implements
#a bunch of view functions
from app import app,db
from flask import render_template, flash, redirect,url_for, request
from werkzeug.urls import url_parse
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from datetime import datetime

"""
    notice how the app instantiation occurs in the __init__.py file, not in the routes file. There is a high level of abstraction ocurring here. 
"""

@app.route('/')
@app.route('/index')
@login_required #this decorator is used to protect unauthed vies from anoymous users
def index():
    user = {'username': 'Doug'}
    posts = [{
        'author': {'username': 'John'},
        'body': 'Beautify day in Portland!'
    },
    {
        'author': {'username': 'Susan'},
        'body': 'The avengers movie was so cool!'
    }
    ]
    return render_template('index.html', title='Home', posts=posts)


#GET returns information to the client(our web browser)
#POST requests used when browser submits form data to the server
#form.validate_on_submit() does all the processing work

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
            return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data) 
        #this will register that user is logged in
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', 
    title='Sign In',
    form=form)

#this logs a user out
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


#this handles user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        #make sure isn't already logged in
    form = RegistrationForm()
    if form.validate_on_submit():
        #creating a new user
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


#this will handle user profile pages
@app.route('/user/<username>')
#this makes it so only logged in users can acess
@login_required
def user(username):
    #try to load user from db using a query by username
    user = User.query.filter_by(username=username).first_or_404()
    #first_or_404 sends 404 result if there's no result back to client
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author':user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)


@app.before_request
def before_request():
    """
        This decorator registers decorated function to be executed before view function.

        Can insert code that want to execute before any view function in the application.
        This simply cheks if current_user is logged in and that sets last_seen field to current time. 
    """
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title="Edit Profile",
    form=form)

