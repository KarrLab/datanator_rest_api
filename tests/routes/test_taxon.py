import connexion
import unittest
import datanator_rest_api.core as core
import json

class ImplementationTestCase(unittest.TestCase):

    def setUp(self):

        self.AutoResolver = core.AutoResolver
        self.app = connexion.App(__name__)
        self.app.add_api('../../datanator_rest_api/spec/DatanatorAPI.yaml', 
            resolver=self.AutoResolver(
            "datanator_rest_api.routes"), validate_responses=True)
        self.client = self.app.app.test_client()
        self.client.testing = True

    def test_canon_rank_distance(self):
        result_0 = self.client.get('/taxon/canon_rank_distance/?species=9606')
        result_1 = self.client.get('/taxon/canon_rank_distance/?species=homo sapiens')
        self.assertEqual(result_0.status_code, 200)
        self.assertEqual(result_1.status_code, 200)