from flask import Blueprint
from flask_restful import Api
from app.views import MovieList


api_bp = Blueprint('api', __name__)
movies = Api(api_bp, prefix="/v1")

movies.add_resource(MovieList, '/movies')
