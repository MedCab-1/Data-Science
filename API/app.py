# Imports
from flask import Flask, render_template, request
import basilica
import numpy as np
import pandas as pd

# from .models import DB, User
# from .predict import predict_


def create_app():
    '''Create and configure an instance of the Flask application'''
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = config('HEROKU_POSTGRESQL_COBALT_URL')
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # DB.init_app(app)

    @app.route('/')
    def root():
        # DB.create_all()
        return render_template('base.html', title='Home', '''users=...''')

    # app.route('/profile')

    return app