import unittest
from datanator_rest_api.query import query_taxon_tree
import tempfile
import shutil
import configparser
import os
import json

class TestQueryTaxonTree(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cache_dirname = tempfile.mkdtemp()
        cls.db = 'datanator'
        parser = configparser.ConfigParser(allow_no_value=True)
        parser.read(os.path.expanduser('~/.wc/datanator.ini'))
        cls.username = parser.get('mongodb', 'user')
        cls.password = parser.get('mongodb', 'password')
        cls.MongoDB = parser.get('mongodb', 'server')
        port = int(parser.get('mongodb', 'port'))
        replSet = parser.get('mongodb', 'replSet')

        cls.src = query_taxon_tree.QueryTaxonTree(
            cache_dirname=cls.cache_dirname, MongoDB=cls.MongoDB, db=cls.db,
                 verbose=True, max_entries=20, username = cls.username, password = cls.password)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.cache_dirname)

    # @unittest.skip('passed')
    def test_get_all_species(self):
        result = []
        generator = self.src.get_all_species()
        for i, name in enumerate(generator):
            if i > 100:
                break
            result.append(json.loads(name))
        self.assertEqual(len(result), 101)
        self.assertEqual(result[38]['tax_name'], "'Amaranthus retroflexus' phytoplasma")

    def test_get_name_by_id(self):
        ids = [743725, 2107591]
        names = self.src.get_name_by_id(ids)
        self.assertEqual(names[0], 'Candidatus Diapherotrites')


    # @unittest.skip('passed')
    def test_get_anc_by_name(self):
        names = ['Candidatus Diapherotrites', 'Candidatus Forterrea multitransposorum CG_2015-17_Forterrea_25_41']
        result_ids, result_names = self.src.get_anc_by_name(names)
        self.assertEqual(result_ids[0], [131567, 2157, 1783276])

    # @unittest.skip('passed')
    def test_get_anc_by_id(self):
        ids = [743725, 2107591, 9606, 9031]
        result_ids, result_names = self.src.get_anc_by_id(ids)
        self.assertEqual(result_ids[0], [131567, 2157, 1783276])
        self.assertEqual(result_ids[1], [131567, 2157, 1783276, 743725, 2107589, 2107590])

    # @unittest.skip('passed')
    def test_get_common_ancestor(self):
        names = ['Candidatus Diapherotrites', 'Candidatus Forterrea multitransposorum CG_2015-17_Forterrea_25_41']
        ancestor, distances = self.src.get_common_ancestor(names[0], names[1])
        self.assertEqual(ancestor, 1783276)
        self.assertEqual(distances[0], 1)
        self.assertEqual(distances[1], 4)

    def test_get_rank(self):
        ids = [131567, 2759, 33154, 33208, 6072, 33213, 33511, 7711, 9526, 314295, 9604, 207598, 9605, 9606]
        ranks = self.src.get_rank(ids)
        self.assertEqual(ranks[3], 'kingdom')
        self.assertEqual(ranks[1], '+')

class TestQueryTaxonTreeMock(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cache_dirname = tempfile.mkdtemp()
        cls.db = 'test'
        parser = configparser.ConfigParser(allow_no_value=True)
        parser.read(os.path.expanduser('~/.wc/datanator.ini'))
        cls.username = parser.get('mongodb', 'user')
        cls.password = parser.get('mongodb', 'password')
        cls.MongoDB = parser.get('mongodb', 'server')
        port = int(parser.get('mongodb', 'port'))
        replSet = parser.get('mongodb', 'replSet')

        cls.src = query_taxon_tree.QueryTaxonTree(
            cache_dirname=cls.cache_dirname, MongoDB=cls.MongoDB, db=cls.db, collection_str='test_taxon_tree',
                 verbose=True, max_entries=20, username = cls.username, password = cls.password)
        dic_0 = {'tax_id': 0, 'tax_name': 's0', 'anc_id': [5,4,3,2,1], 'anc_name': ['s5', 's4', 's3', 's2', 's1']}
        dic_1 = {'tax_id': 1, 'tax_name': 's1', 'anc_id': [5,4,3,2], 'anc_name': ['s5', 's4', 's3', 's2']}
        dic_2 = {'tax_id': 2, 'tax_name': 's2', 'anc_id': [5,4,3], 'anc_name': ['s5', 's4', 's3']}
        dic_3 = {'tax_id': 3, 'tax_name': 's3', 'anc_id': [5,4], 'anc_name': ['s5', 's4']}
        dic_4 = {'tax_id': 4, 'tax_name': 's4', 'anc_id': [5], 'anc_name': ['s5']}
        dic_5 = {'tax_id': 5, 'tax_name': 's5', 'anc_id': [], 'anc_name': []}
        dic_6 = {'tax_id': 6, 'tax_name': 's6', 'anc_id': [5,4,3,2], 'anc_name': ['s5', 's4', 's3', 's2']}
        dic_7 = {'tax_id': 7, 'tax_name': 's7', 'anc_id': [5,4,3,2,6], 'anc_name': ['s5', 's4', 's3', 's2', 's6']}
        dic_8 = {'tax_id': 8, 'tax_name': 's8', 'anc_id': [5,4,3,2,6,7], 'anc_name': ['s5', 's4', 's3', 's2', 's6', 's7']}
        dic_9 = {'tax_id': 9, 'tax_name': 's9', 'anc_id': [5,4,3], 'anc_name': ['s5', 's4', 's3']}
        dic_10 = {'tax_id': 10, 'tax_name': 's10', 'anc_id': [5,4,3,9], 'anc_name': ['s5', 's4', 's3', 's9']}
        dic_11 = {'tax_id': 11, 'tax_name': 's11', 'anc_id': [5,4,3,2,1,0], 'anc_name': ['s5', 's4', 's3', 's2', 's1', 's0']}
        dic_12 = {'tax_id': 12, 'tax_name': 's12', 'anc_id': [5,4,3,2,1,0], 'anc_name': ['s5', 's4', 's3', 's2', 's1', 's0']}
        dic_13 = {'tax_id': 13, 'tax_name': 's13', 'anc_id': [5,4,3,2,1], 'anc_name': ['s5', 's4', 's3', 's2', 's1']}
        cls.src.collection.insert_many([dic_0,dic_1,dic_2,dic_3,dic_4,
            dic_5,dic_6,dic_7,dic_8,dic_9,dic_10,dic_11,dic_12,dic_13])        

    @classmethod
    def tearDownClass(cls):
        cls.src.db_obj.drop_collection(cls.src.collection_str)
        shutil.rmtree(cls.cache_dirname)

    def test_get_equivalent_species(self):
        ids_0, names_0 = self.src.get_equivalent_species(0, 2, max_depth=2)
        self.assertEqual(ids_0, [13,6,7])
        ids_1, names_1 = self.src.get_equivalent_species(0, 3, max_depth=2)
        self.assertEqual(ids_1, [13,6,7,9,10])
        ids_2, names_2 = self.src.get_equivalent_species(0, 3, max_depth=1)
        self.assertEqual(ids_1, [13,6,7,9, 10])
        ids_2 = self.src.get_equivalent_species(0, 0, max_depth=1)
        self.assertEqual('Either input has to be greater than 0', ids_2)
        ids_3 = self.src.get_equivalent_species(0, 1, max_depth=0)
        self.assertEqual('Either input has to be greater than 0', ids_3)
        ids_4, names_4 = self.src.get_equivalent_species(2, 2, max_depth=2)
        self.assertEqual(ids_4, [9,10])
        ids_5, names_5 = self.src.get_equivalent_species(4, 2, max_depth=2)
        self.assertEqual(ids_5, [])