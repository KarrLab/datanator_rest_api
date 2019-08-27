import datanator_rest_api.spec as spec
import datanator_rest_api.core as core
import unittest
import os
import connexion
import pytest


class SpecTestCase(unittest.TestCase):

    def test_valid_syntax(self):
        """Tests that the yaml files have valid syntax and compile properly
        """
        spec.SpecUtils.parseAPI()

    def test_openapi_spec(self):
        """Tests that the resolved yaml file adheres to OpenAPI specification
        """
        api_spec = spec.SpecUtils.parseAPI()
        spec.SpecUtils.validateAPI(api_spec)
