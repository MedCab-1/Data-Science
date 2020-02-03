# Imports
from flask import Flask, jsonify, request
from decouple import config
from .models import DB, Strain
import basilica
import numpy as np
import pandas as pd



def create_app():
    '''Create and configure an instance of the Flask application'''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    @app.route('/')
    def root():
        return "welcome to the api"

    return app