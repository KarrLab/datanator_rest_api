import unittest
from swagger_tester import swagger_test


class ApiTestCase(unittest.TestCase):

    def test_1(self):
        swagger_test('./datanator_rest_api/spec/DatanatorAPI.yaml')
