#routes module holds the different URLs that the app implements
#a bunch of view functions
from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm
"""
    notice how the app instantiation occurs in the __init__.py file, not in the routes file. There is a high level of abstraction ocurring here. 
"""

@app.route('/')
@app.route('/index')
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
    return render_template('index.html', title='Home', user=user, posts=posts)


#GET returns information to the client(our web browser)
#POST requests used when browser submits form data to the server
#form.validate_on_submit() does all the processing work
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login reuqested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect('/index')
    return render_template('login.html', 
    title='Sign In',
    form=form)