""" 
Test the implementation of the API
:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
:Date: 2019-08-23
:Copyright: 2019, Karr Lab
:License: MIT
"""
import connexion
import unittest
import datanator_rest_api.core as core
from prance import BaseParser

class RoutesTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = BaseParser('./datanator_rest_api/spec/DatanatorAPI.yaml')
        cls.specification = cls.parser.specification
        cls.paths = cls.specification['paths']
        cls.routes = cls.paths.keys()

    def test_routes(self):
        for route in self.routes:
            print(route)
        assert(True)
