""" 
Test the implementation of the API
:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
:Date: 2019-08-23
:Copyright: 2019, Karr Lab
:License: MIT
"""
import connexion
import pytest
import datanator_rest_api.core as core
from prance import BaseParser


@pytest.fixture()
def routes():
    parser = BaseParser('./datanator_rest_api/spec/DatanatorAPI.yaml')
    specification = parser.specification
    paths = specification['paths']
    return list(paths.items())


def test_routes(routes):

    for route, routespec in routes:
        print(route)
        print(routespec)
        print("++++++++++++++++++")
    assert(True)
