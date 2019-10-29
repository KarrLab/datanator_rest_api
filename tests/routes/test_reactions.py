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
        docs_0 = self.client.get('/reactions/kinlaw_by_rxn/?substrates=XJLXINKUBYWONI-NNYOXOHSSA-N,ODBLHEXUDAPZAU-UHFFFAOYSA-N&products=GPRLSGONYQIRFK-UHFFFAOYSA-N,KPGXRSRHYNQIFN-UHFFFAOYSA-N')
        self.assertEqual(docs_0.status_code, 200)