from flask import jsonify, current_app, request, abort
from flask_restful import Resource, reqparse

from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

from app.models import Movie, MovieSchema, Cast, UserModel


parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)

class MovieList(Resource):
    @jwt_required
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


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {'message': 'User {} already exists'.format(data['username'])}
        
        new_user = UserModel(
            username = data['username'],
            password = UserModel.generate_hash(data['password'])
        )
        
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])

        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}
        
        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        else:
            return {'message': 'Wrong credentials'}

      
class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}
      
      
class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}
      
      
class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}
