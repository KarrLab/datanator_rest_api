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

    def test_get_info_by_uniprot(self):
        docs_0 = self.client.get('/rna/halflife/get_info_by_uniprot/?uniprot_id=P09119&_from=0&size=10')
        self.assertEqual(docs_0.status_code, 200)

    def test_get_total_docs(self):
        result = self.client.get('/rna/summary/get_total_docs/')
        self.assertEqual(result.status_code, 200)

    def test_get_publication_num(self):
        result = self.client.get('/rna/summary/get_publication_num/')
        self.assertEqual(result.status_code, 200)

    def test_get_distinct(self):
        result = self.client.get('/rna/summary/get_distinct/?_input=halflives.species')
        self.assertEqual(result.status_code, 200)

    def test_get_modifications_by_ko(self):
        docs_0 = self.client.get('/rna/modification/get_modifications_by_ko/?ko_number=K14218&_from=0&size=10')
        self.assertEqual(docs_0.status_code, 200)

    def test_get_total_modifications(self):
        docs_0 = self.client.get('/rna/summary/get_total_modifications/')
        self.assertEqual(docs_0.status_code, 200)

    def test_get_total_halflife_obs(self):
        docs_0 = self.client.get('/rna/summary/get_total_halflife_obs/')
        self.assertEqual(docs_0.status_code, 200)