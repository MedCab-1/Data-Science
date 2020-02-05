# Imports
from flask import Flask, jsonify, request
from decouple import config
from .models import DB, Strain
import basilica
import numpy as np
import pandas as pd
import joblib
import sklearn

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

        # import the model
        model = joblib.load('static/picklemonster.pkl')
        #get user input token
        json = request.get_json(force=True)
        
        #pull input from token
        user_input = json['input']
        
        #plug input into the model
        prediction = model.predict(user_input)

        #turns out input doesn't need embedded, saving in case
        # Set input to a list, so we can embed input
        # user_input_list = [user_input]

        # Embed input 
        # with basilica.Connection('72a5b6d3-09a2-974d-adb0-eee91584cfc7') as c:
        #     user_input_symptoms_embeddings = c.embed_sentences(user_input_list)

        # return user_input_symptoms_embeddings

        # run the function to save the embedding value in session memory
        # (Find out more about this)
        # user_input_symptoms_embedding = calculate_user_text_embedding(
        #     user_input, user_input_embedding)


        # We now have the user input embedded. We want to compare this to
        # The embedded database.
        return jsonify({"prediction": prediction})

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
