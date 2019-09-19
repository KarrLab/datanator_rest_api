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
            '/metabolites/concentrations/?inchi=1S/C10H16N5O13P3/c11-8-5-9(13-2-12-8)15(3-14-5)10-7(17)6(16)4(26-10)1-25-30(21,22)28-31(23,24)27-29(18,19)20/h2-4,6-7,10,16-17H,1H2,(H,21,22)(H,23,24)(H2,11,12,13)(H2,18,19,20)/t4-,6-,7-,10-/m1/s1')
        dic_0 = json.loads(result_0.data)
        self.assertEqual(result_0.status_code, 200)
