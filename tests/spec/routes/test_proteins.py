import connexion
import unittest
import datanator_rest_api.core as core
from prance import BaseParser
import json

class ImplementationTestCase(unittest.TestCase):

    def setUp(self):

        self.AutoResolver = core.AutoResolver
        self.app = connexion.App(__name__)
        self.app.add_api('../../../datanator_rest_api/spec/DatanatorAPI.yaml', 
            resolver=self.AutoResolver(
            "datanator_rest_api.routes"), validate_responses=False)
        self.client = self.app.app.test_client()
        self.client.testing = True

    def test_proteins(self):
        result_0 = json.loads(self.client.get('/proteins/abundance/?uniprot_id=Q9D0T1').data)
        result_1 = json.loads(self.client.get('/proteins/abundance/?uniprot_id=q9D0T1').data)
        result_2 = json.loads(self.client.get('/proteins/abundance/?uniprot_id=q9D0T1,p12345').data)
        self.assertTrue(len(result_0[0]['abundances']) == 56)
        self.assertEqual(result_0, result_1)
        self.assertEqual(result_2[0]['uniprot_id'], 'P12345')