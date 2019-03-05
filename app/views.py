from flask import jsonify
from flask_restful import Resource
from app.models import Movie, MovieSchema


class MovieList(Resource):

    def get(self):
        movies = Movie.query.all()
        movies_schema = MovieSchema(many=True)
        output = movies_schema.dump(movies).data
        return {'movies' : output}