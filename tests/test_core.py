""" Test of datanator_rest_api core module

:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
:Date: 2019-08-20
:Copyright: 2019, Karr Lab
:License: MIT
"""
import connexion
import flask
from datanator_rest_api import core
import unittest


class CoreTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app=core.createApp()
        cls.client = cls.app.app.test_client()
        cls.client.testing = True

    def test_1(self):
        response = self.client.get('/datanator/')
        assert(response.status_code == 200)

    def test_initialization(self):
        
        self.assertIs(type(self.app),connexion.apps.flask_app.FlaskApp,msg="App did not create properly")

    def test_run(self):
        self.assertIs(type(self.client),flask.testing.FlaskClient)
        response = self.client.get('/datanator/')
        assert(response.status_code == 200)
        
        
