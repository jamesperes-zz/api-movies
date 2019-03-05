from unittest import TestCase
from app.load import create_app

class TestLoad(TestCase):
    def setUp(self):
        self.app  = create_app()

    def test_factory_create_app(self):
        self.assertIsNotNone(self.app)