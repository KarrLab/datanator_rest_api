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

    @unittest.skip('need front_end_query to be fixed')
    def test_concentration(self):
        result_1 = self.client.get("/metabolites/concentration/?species=homo sapiens&metabolite=atp")
        dic_1 = json.loads(result_1.data)
        self.assertEqual(result_1.status_code, 200)
        self.assertTrue('concentrations' in dic_1[0][0])
    
    # def test_get(self):
    #     result_0 = json.loads(self.client.get('/metabolites/?inchi_key=test_inchi_key').data)
    #     self.assertEqual({"test": 'test_inchi_key'}, result_0)
    
    def test_concentrations(self):
        result_0 = self.client.get(
            '/metabolites/concentrations/?inchikey=XJLXINKUBYWONI-NNYOXOHSSA-O')
        self.assertEqual(result_0.status_code, 200)

    def test_summary_conc_count(self):
        result_0 = self.client.get(
            '/metabolites/summary/concentration_count/')
        self.assertEqual(result_0.status_code, 200)

    def test_summary_ecmdb_count(self):
        result_0 = self.client.get(
            '/metabolites/summary/ecmdb_doc_count/')
        self.assertEqual(result_0.status_code, 200) 

    def test_summary_ymdb_count(self):
        result_0 = self.client.get(
            '/metabolites/summary/ymdb_doc_count/')
        self.assertEqual(result_0.status_code, 200)

    def test_summary_ymdb_conc_count(self):
        result_0 = self.client.get(
            '/metabolites/summary/ymdb_conc_count/')
        self.assertEqual(result_0.status_code, 200)

    def test_summary_ecmdb_conc_count(self):
        result_0 = self.client.get(
            '/metabolites/summary/ecmdb_conc_count/')
        self.assertEqual(result_0.status_code, 200)

    def test_get_ref_count(self):
        result_0 = self.client.get(
            '/metabolites/summary/get_ref_count/')
        self.assertEqual(result_0.status_code, 200)

    def test_get_distinct(self):
        result_0 = self.client.get(
            '/metabolites/summary/get_distinct/?_input=concentrations.reference.id')
        self.assertEqual(result_0.status_code, 200)            

    def test_meta(self):
        result_1 = self.client.get("/metabolites/meta/?inchikey=UHDGCWIWMRVCDJ-XVFCMESISA-N")
        self.assertEqual(result_1.status_code, 200)

    def test_concentration_only(self):
        result_1 = self.client.get("/metabolites/concentration_only/?inchi_key=UHDGCWIWMRVCDJ-XVFCMESISA-N")
        self.assertEqual(result_1.status_code, 200)

    def test_similar_concentrations(self):
        result_1 = self.client.get("/metabolites/concentrations/similar_compounds/?inchikey=XJLXINKUBYWONI-NNYOXOHSSA-O&threshold=0.7")
        self.assertEqual(result_1.status_code, 200)                