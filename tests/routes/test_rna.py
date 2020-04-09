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

    def test_get_info_by_name(self):
        docs_0 = self.client.get('/rna/halflife/get_info_by_name/?protein_name=something&_from=0&size=10')
        self.assertEqual(docs_0.status_code, 200)

    def test_get_info_by_ko(self):
        docs_0 = self.client.get('/rna/halflife/get_info_by_ko/?ko_number=K13280&_from=0&size=10')
        self.assertEqual(docs_0.status_code, 200)

    def test_get_total_docs(self):
        result = self.client.get('/rna/meta/get_total_docs/')
        self.assertEqual(result.status_code, 200)