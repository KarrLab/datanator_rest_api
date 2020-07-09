from datanator_rest_api.util import paginator
import unittest


class TestPaginator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):        
        cls.files = [0,1,2,3,4,5,6,7,8,9,10,11]
        cls.count = len(cls.files)
        cls.src = paginator.Paginator(cls.count, cls.files)

    def test_page(self):
        result_0 = self.src.page()
        self.assertEqual(result_0, [0,1,2,3,4,5,6,7,8,9])
        result_1 = self.src.page(1, 10)
        self.assertEqual(result_1, [10, 11])
        result_2 = self.src.page(2, 10)
        self.assertEqual(result_2, [])