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
            "datanator_rest_api.routes"), validate_responses=False)
        self.client = self.app.app.test_client()
        self.client.testing = True

    def test_concentration(self):
        pass
    
    def test_get(self):
        result_0 = json.loads(self.client.get('/metabolites/?inchi_key=test_inchi_key').data)
        self.assertEqual({"test": 'test_inchi_key'}, result_0)
    
    def test_concentrations(self):
        result_0 = json.loads(self.client.get('/metabolites/concentrations/?inchi_keys=test_inchi_keys').data)
        self.assertEqual({"test": ['test_inchi_keys']}, result_0)