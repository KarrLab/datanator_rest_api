import connexion
import unittest
import datanator_rest_api.core as core
import json

class ImplementationTestCase(unittest.TestCase):

    def setUp(self):

        self.AutoResolver = core.AutoResolver
        self.app = connexion.App(__name__)
        self.app.add_api('../../../datanator_rest_api/spec/DatanatorAPI.yaml', 
            resolver=self.AutoResolver(
            "datanator_rest_api.routes"), validate_responses=True)
        self.client = self.app.app.test_client()
        self.client.testing = True

    def test_get_entity_value(self):
        result_0 = self.client.get(
            '/v2/observation/get_entity_value/?identifier[namespace]=gene_name&identifier[value]=EMC3&entity=protein&datatype=localization&limit=10')
        self.assertEqual(result_0.status_code, 200)
        result_0 = self.client.get(
            '/v2/observation/get_entity_value/?identifier[namespace]=gene_id&identifier[value]=100003563&entity=RNA&datatype=localization&limit=10')
        self.assertEqual(result_0.status_code, 200)