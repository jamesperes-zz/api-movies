from flask import Blueprint
from flask_restful import Api
from app.views import MovieList, MovieDetail, MovieRegister
from app import views

api_bp = Blueprint('api', __name__)
movies = Api(api_bp, prefix="/v1")

movies.add_resource(MovieList, '/movies')
movies.add_resource(MovieDetail, '/movies/<movie_id>')
movies.add_resource(MovieRegister, '/movies/register')

movies.add_resource(views.UserRegistration, '/registration')
movies.add_resource(views.UserLogin, '/login')
movies.add_resource(views.TokenRefresh, '/token/refresh')