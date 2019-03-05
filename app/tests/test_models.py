from unittest import TestCase
from app.load import create_app
from app.models import Movie


class TestLoad(TestCase):
    def setUp(self):
        self.app  = create_app()
        self.app.db.create_all()
        
    def tearDown(self):
        self.app.db.drop_all()