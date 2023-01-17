from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from datetime import timedelta

def create_app():
    app = Flask(__name__)
    app.secret_key = "YctkDFvaTj"
    app.permanent_session_lifetime = timedelta(minutes=5)

    CORS(app)
    api = Api(app)

    return app, api

app, api = create_app()