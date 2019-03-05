from flask import Flask
from flask_migrate import Migrate
from decouple import config

from app.models import configure
from app.routes import api



def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config('APP_DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    configure(app)
    Migrate(app=app, db=app.db)
    register_blueprints(app)

    return app

def register_blueprints(app):
    app.register_blueprint(api.api_bp)