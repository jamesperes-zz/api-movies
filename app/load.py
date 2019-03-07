from flask import Flask
from flask_migrate import Migrate
from decouple import config
from flask_jwt_extended import JWTManager

from app.models import configure
from app.routes import api

from os import path


def create_app(**kwargs):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config('APP_DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    if kwargs.get('test'):
        dirname = path.dirname(__file__)
        app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{dirname}/db.sqlite3'
    configure(app)
    Migrate(app=app, db=app.db)
    register_blueprints(app)
    jwt = JWTManager(app)
    return app

def register_blueprints(app):
    app.register_blueprint(api.api_bp)