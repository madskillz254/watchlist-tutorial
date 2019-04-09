from flask import render_template
from app import app

@app.errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('error.html'),404 # We create a view function. that returns fourOwfour.html file and we also pass in the status code we receive 404