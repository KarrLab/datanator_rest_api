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
        result_0 = self.client.get('/metabolites/test')
        self.assertEqual(result_0.status_code, 200)
        dic_0 = json.loads(result_0.data)
        self.assertTrue('Test' in dic_0)
        result_1 = self.client.get('/metabolites/concentration/atp?Species=homo sapiens')
        dic_1 = json.loads(result_1.data)
        self.assertEqual(result_1.status_code, 200)
        self.assertTrue('concentrations' in dic_1[0][0])
    
    def test_get(self):
        result_0 = json.loads(self.client.get('/metabolites/?inchi_key=test_inchi_key').data)
        self.assertEqual({"test": 'test_inchi_key'}, result_0)
    
    def test_concentrations(self):
        result_0 = json.loads(self.client.get('/metabolites/concentrations/?inchi_keys=test_inchi_keys').data)
        self.assertEqual({"test": ['test_inchi_keys']}, result_0)