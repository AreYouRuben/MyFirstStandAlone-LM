from flask import Blueprint
from flask import render_template

page = Blueprint('page', __name__)

@page.route('/')
def index():
    return render_template('index.html', title='Home')

@page.route('/mnist')
def mnist():
    return render_template('mnistPage.html', title='Guess the number')