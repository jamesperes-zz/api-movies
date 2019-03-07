from flask import jsonify, current_app, request, abort
from flask_restful import Resource
from app.models import Movie, MovieSchema, Cast


class MovieList(Resource):

    def get(self):
        movies = Movie.query.all()
        movies_schema = MovieSchema(many=True)
        output = movies_schema.dump(movies).data
        return {'movies' : output}

class MovieDetail(Resource):

    def get(self, movie_id):
        movies = Movie.query.filter(Movie.id == movie_id)
        movies_schema = MovieSchema(many=True)
        output = movies_schema.dump(movies).data
        if len(output) < 1:
            abort(404)
        return output[0]

class MovieRegister(Resource):

    def post(self):
        try:
            movie = self.register_movie(request.json)
            movie = self.register_cast(request.json, movie)    
            movie_schema = MovieSchema()
            output = movie_schema.dump(movie).data
        except Exception as e:
            return str(e), 400
        return 'ok', 201

    def register_movie(self, json):
        title = json['title']
        brazilian_title = json['brazilian_title']
        year_of_production = json['year_of_production']
        director = json['director']
        genre = json['genre']
        movie = Movie(title=title, brazilian_title=brazilian_title, year_of_production=year_of_production,
                        director=director, genre=genre)
        current_app.db.session.add(movie)
        current_app.db.session.commit()
        return movie

    def register_cast(self, json, movie):
        for cast in json['cast']:
            role = cast['role']
            name = cast['name']
            cast_info = Cast(role=role, name=name, movie_id=movie.id)
            current_app.db.session.add(cast_info)
            current_app.db.session.commit()
        return movie