"""
Routes and views for the flask application.
"""
import json
from datetime import datetime
from flask import render_template
from AntiMarkup import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Enter a Markup',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='The Hall of Shame',
        year=datetime.now().year,
        jsondata=json.load(open(r"AntiMarkup\markups.json")),
        message='The Top 10 Worst Car Dealers in the US'
    )

@app.route('/search')
def search():
    """Renders the search page."""
    return render_template(
        'search.html',
        title = 'Search',
        year=datetime.now().year,
        message='Search by year, make and model.'
        
    )