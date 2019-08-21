import datanator_rest_api.spec as spec
import unittest
import os


class ApiTestCase(unittest.TestCase):

    def test_valid_syntax(self):
        """Tests that the yaml files have valid syntax and compile properly
        """
        spec.SpecUtils.parseAPI()

 