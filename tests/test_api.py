import unittest
from swagger_tester import swagger_test


class ApiTestCase(unittest.TestCase):

    def test_1(self):
        swagger_test('./spec/DatanatorAPI.yaml')
