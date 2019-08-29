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
from datanator_query_python import front_end_query
from datanator_query_python import config

def put(body):
    return ("test")


def post():
    return ("test")


def get(inchi_key=None):
    print(inchi_key)
    return{"test": inchi_key}


class Manager:
    def __init__(self):
        username = config.Config.USERNAME
        password = config.Config.PASSWORD
        server = config.Config.SERVER
        authDB = config.Config.AUTHDB
        self.manager = front_end_query.QueryFrontEnd(
            MongoDB=server, username=username, password=password,
            authDB=authDB)

class concentrations(object):
    def get(inchi_key=None):
        print(inchi_key)
        print(request.args)
        return{"test": inchi_key}

class concentration:
    
    def get(metabolite, species=None, abstract=False):
        return Manager().manager.get_metabolite_concentration(metabolite, species, abstract_default=abstract)