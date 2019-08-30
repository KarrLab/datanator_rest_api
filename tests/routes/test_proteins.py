import connexion
import unittest
import datanator_rest_api.core as core
from prance import BaseParser
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

    def test_proteins(self):
        result_0 = json.loads(self.client.get('/proteins/precise_abundance/?uniprot_id=Q9D0T1').data)
        result_1 = json.loads(self.client.get('/proteins/precise_abundance/?uniprot_id=q9D0T1').data)
        result_2 = json.loads(self.client.get('/proteins/precise_abundance/?uniprot_id=q9D0T1,p12345').data)
        self.assertTrue(len(result_0[0]['abundances']) == 56)
        self.assertEqual(result_0, result_1)
        self.assertEqual(result_2[0]['uniprot_id'], 'P12345')

    def test_proximity_proteins(self):
        result_0 = json.loads(self.client.get('/proteins/proximity_abundance/?uniprot_id=Q9D0T1&distance=100&depth=100').data)
        self.assertEqual(len(result_0), 100)
        self.assertEqual(result_0[2]['documents'][0]['uniprot_id'], 'P55770')

    def test_meta(self):
        result_0 = json.loads(self.client.get(
            '/proteins/meta/meta_combo/?uniprot_id=Q54ST0,Q9d0t1').data)        
        self.assertEqual(result_0[0]['ncbi_taxonomy_id'], 44689)
        self.assertEqual(result_0[1]['ncbi_taxonomy_id'], 10090)
        result_1 = json.loads(self.client.get(
            '/proteins/meta/meta_single/?ncbi_taxon_id=9606').data)
        self.assertEqual(len(result_1[0]['uniprot_ids']), 12412)
        result_2 = json.loads(self.client.get(
            '/proteins/meta/meta_single/?name=Nucleoside diphosphate kinase').data)
        self.assertEqual(len(result_2), 5)
        result_3 = json.loads(self.client.get(
            '/proteins/meta/meta_combo/?ncbi_taxon_id=9606&name=alcohol dehydrogenase').data)
        self.assertEqual(len(result_3), 13)
        result_4 = json.loads(self.client.get(
            '/proteins/meta/meta_combo/?ncbi_taxon_id=9606&name=phosphofructokinase&species_name=escherichia coli').data)
        self.assertEqual(len(result_4), 3)
        result_5 = json.loads(self.client.get(
            '/proteins/meta/meta_single/?ncbi_taxon_id=9606&name=alcoo').data)
        self.assertEqual(result_5, "This combination of input is not valid.")
        result_6 = json.loads(self.client.get(
            '/proteins/meta/meta_combo/?ncbi_taxon_id=9606').data)
        self.assertEqual(result_6, 'Please try another input combination')
