from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def configure(app):
    db.init_app(app)
    ma.init_app(app)
    app.db = db


class Movie(db.Model):
  
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    brazilian_title = db.Column(db.String(128),  nullable=False)
    year_of_production = db.Column(db.Integer,  nullable=False)
    director = db.Column(db.String(128),  nullable=False)
    genre = db.Column(db.String(128),  nullable=False)

    def __repr__(self):
        return "<Title: {}>".format(self.title)


class Cast(db.Model):
    __tablename__ = 'casts'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    movie = db.relationship('Movie', backref='cast')

    def __repr__(self):
        return '<Name {}>'.format(self.name)


class CastSchema(ma.ModelSchema):
    class Meta:
        fields= ('name', 'role')


class MovieSchema(ma.ModelSchema):
    class Meta:
        model = Movie

    cast = ma.Nested(CastSchema, many=True)