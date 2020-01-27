"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from testeProjectFlask import app
from testeProjectFlask import mongo
import plotly
import plotly.graph_objs as go
from flask_pymongo import PyMongo
import pandas as pd
import numpy as np
import json

#mongo = PyMongo(app)
#mongo.init_app(app)
users = mongo.db.users

def create_plot():


    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        #go.Bar(
        #    x=df['x'], # assign x as the dataframe column 'x'
        #    y=df['y']
        #)
        go.Scatter(
                    x = df['x'],
                    y = df['y'],
                    #mode = 'markers'
                )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""

    bar = create_plot()
    return render_template(
        'index.html', 
        plot=bar,
        selectedExperiment = "saparada de teste"
)


@app.route('/cadastro')
def cadastro():
    """Renders the contact page."""    

    return render_template(
        'cadastro.html',
        title='Cadastro',
        year=datetime.now().year,
    )

@app.route('/about')
def about():
    """Renders the about page."""

    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        names = ["teste","saparada","DJ"]
    )

#@app.route('/cadastro', methods = ['GET', 'POST', 'DELETE'])
#def cadastro