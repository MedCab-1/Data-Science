# Imports
from flask import Flask, jsonify, request
import basilica
import numpy as np
import pandas as pd
from .models import DB

def predict(user_input):
    # df = pd.read_csv('')
    


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        DB.create_all()
        return "welcome to the api"

    # Strains route
    

    return app