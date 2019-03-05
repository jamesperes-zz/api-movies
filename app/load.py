from flask import Flask
from app.models import configure

def create_app():
    app = Flask(__name__)

    configure(app)

    return app