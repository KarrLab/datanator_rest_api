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

    def test_precise_proteins(self):
        result_0 = self.client.get('/proteins/precise_abundance/?uniprot_id=Q9D0T1')
        result_1 = self.client.get('/proteins/precise_abundance/?uniprot_id=q9D0T1')
        result_2 = self.client.get('/proteins/precise_abundance/?uniprot_id=q9D0T1,p12345')
        self.assertEqual(result_1.status_code, 200)
        self.assertEqual(result_2.status_code, 200)
        self.assertEqual(result_0.status_code, 200)
        result_3 = self.client.get('/proteins/precise_abundance/?kegg_orthology=K00940')
        result_4 = self.client.get('/proteins/precise_abundance/?kegg_orthology=K00940&uniprot_id=Q9D0T1')
        self.assertEqual(result_3.status_code, 200)
        self.assertEqual(result_4.status_code, 200)


    # @unittest.skip('passed')
    def test_proximity_proteins(self):
        result_0 = self.client.get('/proteins/proximity_abundance/?uniprot_id=Q9D0T1&distance=100&depth=100')
        self.assertEqual(result_0.status_code, 200)

    # @unittest.skip('passed')
    def test_meta(self):
        result_0 = self.client.get(
            '/proteins/meta/meta_combo/?uniprot_id=Q54ST0,Q9d0t1')       
        self.assertEqual(result_0.status_code, 200)
        # result_1 = self.client.get(
        #     '/proteins/meta/meta_single/?ncbi_taxon_id=9606')
        # self.assertEqual(result_1.status_code, 200)
        result_2 = self.client.get(
            '/proteins/meta/meta_single/?name=Nucleoside diphosphate kinase')
        self.assertEqual(result_2.status_code, 200)
        result_3 = self.client.get(
            '/proteins/meta/meta_combo/?ncbi_taxon_id=9606&name=alcohol dehydrogenase')
        self.assertEqual(result_3.status_code, 200)
        result_4 = self.client.get(
            '/proteins/meta/meta_combo/?ncbi_taxon_id=9606&name=phosphofructokinase&species_name=escherichia coli')
        self.assertEqual(result_4.status_code, 200)
        result_5 = self.client.get(
            '/proteins/meta/meta_single/?ncbi_taxon_id=9606&name=alcoo')
        self.assertEqual(result_5.status_code, 200)
        result_6 = self.client.get(
            '/proteins/meta/meta_combo/?ncbi_taxon_id=9606')
        self.assertEqual(result_6.status_code, 500)

    def test_proximity_proteins_kegg(self):
        result_0 = self.client.get('/proteins/proximity_abundance/proximity_abundance_kegg/?kegg_id=K03154&anchor=Thermus%20thermophilus%20HB27&distance=3')
        self.assertEqual(result_0.status_code, 200)

    def test_summary_organism(self):
        result = self.client.get('/proteins/summary/num_organism/')
        self.assertEqual(result.status_code, 200)

    def test_summary_protein(self):
        result = self.client.get('/proteins/summary/num_protein/')
        self.assertEqual(result.status_code, 200)

    def test_similar_protein_refseq(self):
        result = self.client.get('/proteins/similar_protein/refseq/?uniprot_id=q9vb24&identity=90')
        self.assertEqual(result.status_code, 200)