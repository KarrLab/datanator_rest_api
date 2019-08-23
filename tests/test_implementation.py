import connexion
import pytest
import datanator_rest_api.core as core
import unittest


class ImplementationTestCase(unittest.TestCase):

    def setUp(self):
        self.AutoResolver = core.AutoResolver

        self.app = connexion.FlaskApp(__name__)
        self.app.add_api('../datanator_rest_api/spec/DatanatorAPI.yaml', resolver=self.AutoResolver(
            "datanator_rest_api.routes"), validate_responses=False)
        self.client = self.app.app.test_client()
        self.client.testing = True

    def test_1(self):
        response = self.client.get('/datanator/')
        print(type(response.data))
        print(response.data)
        assert(response.status_code == 200)
