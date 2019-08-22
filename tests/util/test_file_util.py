import unittest
from datanator_rest_api.util import file_util
import tempfile
import shutil


class TestFileUtil(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cache_dirname = tempfile.mkdtemp()
        cls.src = file_util.FileUtil()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.cache_dirname)

    # @unittest.skip('passed')
    def test_flatten_json(self):
        dic = {
            "a": 1,
            "b": 2,
            "c": [{"d": [2, 3, 4], "e": [{"f": 1, "g": 2}]}],
            'h': [1, 2, 3]
        }
        flat = self.src.flatten_json(dic)
        self.assertEqual(flat['c_0_d_0'], 2)
        self.assertEqual(flat['c_0_e_0_f'], 1)
        self.assertEqual(flat['h_0'], 1)

    # @unittest.skip('passed')
    def test_extract_values(self):
        dic = {
            "a": 1,
            "b": 2,
            "c": [{"d": [2, 3, 4], "e": [{"f": 1, "g": 2}]}],
            'h': [1, 2, 3]
        }
        values = self.src.extract_values(dic, 'g')
        self.assertEqual([2], values)

    def test_get_val_from_dict_list(self):
        dict_list = [{'a':1, 'b': 2, 'c':3}, {'a':10, 'b': 20, 'c':30},
            {'a':100, 'b': 200, 'd':300}]
        key = 'c'
        result = self.src.get_val_from_dict_list(dict_list, key)
        self.assertEqual(result, [3, 30, 'no such key'])

    # @unittest.skip('passed')
    def test_unpack_list(self):
        _list = [ [1], [2], [3, 4] ]
        result = self.src.unpack_list(_list)
        self.assertEqual(result, [1,2,3,4])

    # @unittest.skip('passed')
    def test_access_dict_by_index(self):
        _dict = {'a':0, 'b':1, 'c':2, 'd':3}
        result = self.src.access_dict_by_index(_dict, 3)
        self.assertEqual({'a':0, 'b':1, 'c':2}, result)

    # @unittest.skip('passed')
    def test_replace_dict_key(self):
        _dict = {'a': 0, 'b': 1, 'c': 2}
        replacements = ['d', 'e', 'f']
        result = self.src.replace_dict_key(_dict, replacements)
        self.assertEqual({'d':0, 'e':1, 'f':2}, result)

    def test_distance_to_common(self):
        list1 = ['a', 'b', 'c'] 
        list2 = ['a', 'b', 'd']
        list3 = ['a', 'i', 'g', 'e']
        list4 = ['a', 'i', 'h', 'f']
        list5 = [131567, 2157, 1783276]
        list6 = [131567, 2157, 1783276, 743725, 2107589, 2107590]
        result1 = self.src.get_common(list1, list2)
        result2 = self.src.get_common(list1, list3)
        result3 = self.src.get_common(list1, list4)
        result4 = self.src.get_common(list3, list4)
        result5 = self.src.get_common(list4, list1)
        result6 = self.src.get_common(list5, list6)
        self.assertEqual(result1, 'b')
        self.assertEqual(result2, 'a')
        self.assertEqual(result3, 'a')
        self.assertEqual(result4, 'i')
        self.assertEqual(result5, 'a')
        self.assertEqual(result6, 1783276)

    def test_make_dict(self):
        keys = ['a', 'b', 'c', 'd']
        values = [1, 2, 3, 4]

        result = self.src.make_dict(keys, values)
        self.assertEqual(result['a'], 1)

    def test_search_dict_list(self):
        dict_list = [
            {'name': "Tom", 'age': 10},
            {'name': "Mark", 'age': 5},
            {'name': "Pam", 'age': 7}
            ]
        result = self.src.search_dict_list(dict_list, 'name', value = 'Tom')
        result_1 = self.src.search_dict_list(dict_list, 'ah', value = 'chu')
        result_2 = self.src.search_dict_list(dict_list, 'ah', value = '')
        result_3 = self.src.search_dict_list(dict_list, 'name', value = '')
        self.assertEqual(result, [{'name': "Tom", 'age': 10}])
        self.assertEqual(result_1, [])
        self.assertEqual(result_2, [])
        self.assertEqual(result_3, dict_list)

    def test_merge_dict(self):
        dicts = [ {'a': 1, 'b': 2}, {'c': 3}, {'d': 4} ]
        result = self.src.merge_dict(dicts)
        self.assertEqual(result, {'a':1,'b':2,'c':3,'d':4})

    def test_exists_key_value_pair(self):
        dictionary = {'name': "Tom", 'age': 10, 'grade': 3}
        k_1, k_2, v_1, v_2 = 'age', 'grade', 10, 11
        test_1 = self.src.exists_key_value_pair(dictionary, k_1, v_1)
        test_2 = self.src.exists_key_value_pair(dictionary, k_1, v_2)
        self.assertTrue(test_1)
        self.assertTrue(not test_2)