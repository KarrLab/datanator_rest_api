""" Metabolites collection controller
This file defines the methods for the operations on the Metabolites collection.
The root class contains the HTTP methods for the /metabolites/ path
Any subpaths are contained in an internal class

:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
         Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2019-08-20
:Copyright: 2019, Karr Lab
:License: MIT
"""
from flask import request
from datanator_query_python.config import query_manager


def put(body):
    return ("test")


def post():
    return ("")


def get(inchi_key=None):
    return ("")


class concentrations:
    def get(inchi, consensus=False):
        return query_manager.Manager().eymdb_manager().get_conc_from_inchi(inchi, consensus=consensus)


class concentration:

    def get(metabolite, species=None, abstract=False):
        return query_manager.Manager().metabolite_manager().molecule_name_query(metabolite, species, abstract_default=abstract)
