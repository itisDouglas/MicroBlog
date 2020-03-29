from flask import render_template
from app import app, db

#rrorhandler decorator is used to declar custom error handlers
@app.errorhandler(404)
def not_found_error(error):
    #returning 404 as the response code
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()#issuing session to a clean slate
    #returning 500 as the response code
    return render_template('500.html'),500