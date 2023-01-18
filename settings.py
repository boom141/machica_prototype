from flask import Flask
from datetime import timedelta

def create_app():
    app = Flask(__name__)
    app.secret_key = "YctkDFvaTj"
    app.permanent_session_lifetime = timedelta(minutes=5)

    return app

app = create_app()