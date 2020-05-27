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

    def test_kinlawid_by_rxn(self):
        s = """/reactions/kinlaw_by_rxn/?substrates=XJLXINKUBYWONI-NNYOXOHSSA-N&substrates=ODBLHEXUDAPZAU-UHFFFAOYSA-N\
        &products=GPRLSGONYQIRFK-UHFFFAOYSA-N&products=KPGXRSRHYNQIFN-UHFFFAOYSA-N&_from=0&size=10&bound=loose&dof=0"""
        docs_0 = self.client.get(s)
        self.assertEqual(docs_0.status_code, 200)

    def test_kinlawid_doc(self):
        docs_0 = self.client.get('/reactions/kinlaw_doc/?kinlaw_id=10&_from=0&size=10')
        self.assertEqual(docs_0.status_code, 200)

    def test_kinlaw_entryid(self):
        docs_0 = self.client.get('/reactions/kinlaw_entry/?entry_id=6593&last_id=0&size=10')
        self.assertEqual(docs_0.status_code, 200)

    def test_kinlaw_by_name(self):
        docs_0 = self.client.get("/reactions/kinlaw_by_name/?substrates=Riboflavin-5-phosphate&substrates=2-Hydroxypentanoate&products=reduced%20FMN&_from=0&size=10&bound=loose")
        self.assertEqual(docs_0.status_code, 200)

    def test_summary_organism(self):
        result = self.client.get('/reactions/summary/num_organism/')
        self.assertEqual(result.status_code, 200)

    def test_summary_protein(self):
        result = self.client.get('/reactions/summary/num_entries/')
        self.assertEqual(result.status_code, 200)
    
    def test_summary_num_parameter_km(self):
        result = self.client.get('/reactions/summary/num_parameter_km/')
        self.assertEqual(result.status_code, 200)

    def test_summary_num_parameter_kcat(self):
        result = self.client.get('/reactions/summary/num_parameter_kcat/')
        self.assertEqual(result.status_code, 200)

    @unittest.skip("takes 24.7s")
    def test_get_distinct(self):
        result = self.client.get('/reactions/summary/get_distinct/?_input=pH')
        self.assertEqual(result.status_code, 200)

    def test_get_ph_freq(self):
        result = self.client.get('/reactions/summary/get_frequency/?field=ph')
        self.assertEqual(result.status_code, 200)
        result = self.client.get('/reactions/summary/get_frequency/?field=temperature')
        self.assertEqual(result.status_code, 200)

    def test_get_brenda_obs(self):
        result = self.client.get('/reactions/summary/get_brenda_obs/?parameter=k_ms')
        self.assertEqual(result.status_code, 200)