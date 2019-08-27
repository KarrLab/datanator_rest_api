""" Proteins Controller

:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
:Date: 2019-08-21
:Copyright: 2019, Karr Lab
:License: MIT
"""
from datanator_query_python.query import query_protein
from datanator_query_python.config import config



def search():
    return("search")


def get():
    return("get")


def put(body):
    return ("put")


def post(body):
    return ("post")


class Manager:
    def __init__(self):
        username = config.Config.USERNAME
        password = config.Config.PASSWORD
        server = config.Config.SERVER
        self.manager = query_protein.QueryProtein(
            server=server, username=username, password=password)


class abundance:

    def get(self, distance, protein_id, depth):
        if distance is None:
            return Manager.manager.get_abundance_by_id(protein_id)
        else:
            return Manager.manager.get_equivalent_protein(protein_id, distance, max_depth=depth)

