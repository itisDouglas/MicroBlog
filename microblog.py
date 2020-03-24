""" 
    this script is a top-level scrip that defines the Flask Application instance.

    Flask application instance is called 'app' and is member of the 'app'

    @app.shell_context_processor decorator registers function as a shell context function.
    When 'flask shell' command runs it'll invoke this function.
    It will register the items returned by it in the shell session. 
"""
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User': User, 'Post': Post}