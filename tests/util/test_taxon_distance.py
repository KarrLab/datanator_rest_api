from datanator_rest_api.util import taxon_distance
from collections import deque
import unittest


class TestTaxonDist(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.src = taxon_distance.TaxonDist(debugging=True)

    @classmethod
    def tearDownClass(cls):
        # cls.src.manager.client.close()
        pass

    def test_get_dist_object(self):
        queried_species = deque()
        distance_obj = {}
        target_species = 9606
        tax_field = 'tax_id'
        docs = [{'tax_id': 2012491}, {'tax_id': 1936271}, {'tax_id': 1841599}, {'tax_id': 1936271}]
        for i, doc in enumerate(docs):
            queried_species, distance_obj, doc = self.src.get_dist_object(doc, queried_species, distance_obj,
                                                                          target_species, tax_field=tax_field)
            if i == 3:
                self.assertFalse(doc['queried'])
        self.assertEqual(len(queried_species), 3)

    def test_arrange_distance_objs(self):
        target_species = 9606
        tax_field = 'tax_id'
        docs = [{'tax_id': 2012491}, {'tax_id': 1936271}, {'tax_id': 1841599}, {'tax_id': 1936271}]
        result = self.src.arrange_distance_objs(docs, target_species=target_species, tax_field=tax_field, org_format='tax_id')
        self.assertFalse(result[3]['queried'])
        self.assertEqual(len(result), 4)
        