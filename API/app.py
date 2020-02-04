# Imports
from flask import Flask, jsonify, request
from decouple import config
from .models import DB, Strain
import basilica
import numpy as np
import pandas as pd
from .models import DB

def predict(user_input_symptoms):
    '''A function that takes user input symptoms and returns strains that best match input'''
    # Get the data
    df = pd.read_csv('symptoms.csv')

    # unpickle
    unpickled = pd.read_pickle('pickled_model')

    # Set input to a list, so we can embed input
    user_input_list = [user_input]

    # Embed input
    with basilica.Connection('72a5b6d3-09a2-974d-adb0-eee91584cfc7') as c:
        user_input_symptoms_embeddings = c.embed_sentences(user_input_list)

    return user_input_symptoms_embeddings

    # run the function to save the embedding value in session memory
    # (Find out more about this)
    user_input_symptoms_embedding = calculate_user_text_embedding(
        user_input, user_input_embedding)


    # We now have the user input embedded. We want to compare this to
    # The embedded database.




def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    @app.route('/')
    def root():
        DB.create_all() # Is this correct or really bad?
        return "welcome to the api"

    @app.route('/strains', methods=['POST'])
    def strains():
        '''Function to take user input, receive JSON front-end token, 
        translate token, verify input, feed input into model to create output
        (Output could be: that single strain, and perhaps the local clusters.)'''

        # Receive JSON token (input?)
        # By default this function will only load the
        # json data if the mimetype is application/json
        # This is overriden by the 'force' command.
        json_token = request.get_json(force=True)

        # Translate token
        text = json_token['input']

        # Verify input
        Assert isinstance(text, str)

        # Feed input into model
        output = predict(text)

        # Give output to sender?
        return output
    
    return app
