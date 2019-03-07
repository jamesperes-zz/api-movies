from unittest import TestCase
from flask import url_for
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from decouple import config
from app.load import create_app
from app.models import Movie

class BaseTest(TestCase):
    def setUp(self):
        self.app  = create_app(test=True)
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.app.db.create_all()
        movie = Movie(title =  "titulo do filme",
                        brazilian_title = "titulo do filme em português",
                        year_of_production= "2019",
                        director="nome do diretor do filme",
                        genre="gênero do filme",
                        id=444)
        self.app.db.session.add(movie)
        self.app.db.session.commit()

    def tearDown(self):
        self.app.db.session.remove()
        self.app.db.drop_all()



class TestValidMovie(BaseTest):
 
    def test_status_movie_list(self):
        response = self.client.get(url_for('api.movielist'))
        self.assertEqual(200, response.status_code)
        self.assertIs(list, type(response.json.get('movies')))


    def test_status_movie_detail(self):
        response = self.client.get(url_for('api.moviedetail', movie_id=444))
        self.assertEqual(200, response.status_code)
    
    def test_status_movie_detail_not_found(self):
        response = self.client.get(url_for('api.moviedetail', movie_id=42))
        self.assertEqual(404, response.status_code)


    def test_status_movie_register(self):
        json_data =  {
                        "title": "007",
                        "brazilian_title": "James Bond",
                        "year_of_production": "1989",
                        "director": "Bruce",
                        "genre": "Ação",
                        "cast": [{
                                "role": "James Bond",
                                "name": "James Peres"
                            },
                        ]
                    }
        response = self.client.post(url_for('api.movieregister'), json=json_data)
        self.assertEqual(201, response.status_code)
