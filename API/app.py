# Imports
from flask import Flask, jsonify, request
from decouple import config
from .models import DB, Strain
from .predict import predict_strains
import basilica
import numpy as np
import pandas as pd


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    @app.route('/')
    def root():
        return "welcome to the api"

    @app.route('/predict', methods=['POST','GET'])
    def predict():
        '''A function that takes user input and returns strains that best match input'''

        # get user input token
        json = request.get_json(force=True)
        
        # pull input from token
        kind = json['type']
        effect = json['effect']
        flavor = json['flavor']

        # compile input into one string
        user_input = str(kind + effect + flavor)[1:-1]
        
        # plug input into the model
        strains = predict_strains(user_input)
        return jsonify({"strains" : strains})

    @app.route('/strain', methods=['POST', 'GET'])
    def strain():
        '''Function to take user input, receive JSON front-end token, 
        translate token, verify input, return the requested strain information
        (Output could be: that single strain, and perhaps the local clusters.)'''

        # Receive JSON token (input?)
        # By default this function will only load the
        # json data if the mimetype is application/json
        # This is overriden by the 'force' command.
        json = request.get_json(force=True)

        # Get the input data from the token
        text = json['strain']

        # Verify input is a string
        assert isinstance(text, str)

        #load and return the strain info from the database
        search = Strain.query.filter(Strain.name==text).first()
        strain_info = {"name" : search.name,
                        "type" : search.kind,
                        "rating" : search.rating,
                        "effects" : search.effects,
                        "flavors" : search.flavor,
                        "description": search.description}
        return jsonify(strain_info)
    
    return app
