from flask import render_template
from app import app


@app.errorhandler(404)
def four_Ow_Four(error):
    '''
    function that describes the behaviour of error page
    '''
    return render_template('fourOwFour.html'), 404
