import datanator_rest_api.spec as spec
import unittest
import os


class ApiTestCase(unittest.TestCase):

    def test_valid_syntax(self):
        """Tests that the yaml files have valid syntax and compile properly
        """
        spec.SpecUtils.parseAPI()

    def test_openapi_spec(self):
        """Tests that the resolved yaml file adheres to OpenAPI specification
        """
        api_spec = spec.SpecUtils.parseAPI()
        spec.SpecUtils.validateAPI(api_spec)
