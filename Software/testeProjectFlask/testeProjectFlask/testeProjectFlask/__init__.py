"""
The flask application package.
"""

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/ProjetoMedidorRespiracao"
mongo = PyMongo(app)
mongo.init_app(app)

import testeProjectFlask.views
