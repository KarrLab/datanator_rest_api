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
        result = self.client.get('/taxon/canon_rank_distance/?ncbi_id=9606')
        self.assertEqual(result.status_code, 200)

    def test_canon_rank_distance_by_name(self):
        result = self.client.get('/taxon/canon_rank_distance_by_name/?name=homo sapiens')
        self.assertEqual(result.status_code, 200)
        result = self.client.get('/taxon/canon_rank_distance_by_name/?name=xxxxx')
        self.assertEqual(result.status_code, 404)

    def test_is_child(self):
        result = self.client.get('/taxon/is_child/?src_tax_ids=550690&target_tax_id=523')
        self.assertEqual(result.status_code, 200)

    def test_canon_rank_common_distance(self):
        result = self.client.get('/taxon/canon_rank_common_distance/?org_0=562&org_1=4464674')
        self.assertEqual(result.status_code, 200)

    def test_taxon_distribution(self):
        result = self.client.get('/taxon/summary/taxon_distribution/')
        self.assertEqual(result.status_code, 200)