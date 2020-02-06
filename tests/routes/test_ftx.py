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

    def test_text_search(self):
        s = """ftx/text_search/?query_message=something&index=ecmdb%2Cymdb%2Cmetabolites_meta%2Cprotein%2Csabio_rk&from_=0&size=10&fields\
        =protein_name&fields=synonyms&fields=enzymes&fields=ko_name&fields=gene_name&fields=name&fields=reaction_participant.substrate.substrate_name\
        &fields=reaction_participant.substrate.substrate_synonym&fields=reaction_participant.product.product_name&fields=\
        reaction_participant.product.substrate_synonym&fields=enzymes.enzyme.enzyme_name&fields=enzymes.subunit.canonical_sequence&fields=species"""
        result = self.client.get(s)
        self.assertEqual(result.status_code, 200)

    def test_text_search_in_page(self):
        s = """/ftx/text_search/indices_in_page/?query_message=glucose&index=ecmdb%2Cymdb%2Cmetabolites_meta%2Cprotein%2Csabio_rk&iof=ecmdb&\
from_=0&size=10&fields=protein_name&fields=synonyms&fields=enzymes&fields=ko_name&fields=gene_name&\
fields=name&fields=reaction_participant.substrate.substrate_name&fields=reaction_participant.substrate.substrate_synonym&\
fields=reaction_participant.product.product_name&\
fields=reaction_participant.product.substrate_synonym&fields=enzymes.enzyme.enzyme_name\
&fields=enzymes.subunit.canonical_sequence"""
        result = self.client.get(s)
        self.assertEqual(result.status_code, 200)