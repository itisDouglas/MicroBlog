#routes module holds the different URLs that the app implements
#a bunch of view functions
from app import app
from flask import render_template, flash, redirect,url_for, request
from werkzeug.urls import url_parse
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
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