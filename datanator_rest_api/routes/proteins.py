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
        authDB = config.Config.AUTHDB
        self.manager = query_protein.QueryProtein(
            server=server, username=username, password=password,
            authSource=authDB)

def get_abundance_uniprotid(uniprot_id):
        return Manager().manager.get_abundance_by_id(uniprot_id)

