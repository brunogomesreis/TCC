"""
The flask application package.
"""

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://bruno:ewxt7ds21@cluster0-b1ugb.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)
mongo.init_app(app)

import testeProjectFlask.views
