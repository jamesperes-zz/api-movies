from flask import Flask
from flask_migrate import Migrate
from decouple import config

from app.models import configure

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config('APP_DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    configure(app)
    Migrate(app=app, db=app.db)

    return app