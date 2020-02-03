# Imports
from flask import Flask, jsonify, request
import basilica
import numpy as np
import pandas as pd



def create_app():
    '''Create and configure an instance of the Flask application'''
    app = Flask(__name__)

    @app.route('/')
    def root():
        return "welcome to the api"

    return app