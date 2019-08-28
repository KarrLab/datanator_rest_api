""" Proteins Controller

:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
:Date: 2019-08-21
:Copyright: 2019, Karr Lab
:License: MIT
"""
from datanator_query_python.query import query_protein
from datanator_query_python.config import config


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

class precise_abundance:

    def get(uniprot_id):
        return Manager().manager.get_abundance_by_id(uniprot_id)


class proximity_abundance:

    def get(uniprot_id, distance, depth):
        return Manager().manager.get_equivalent_protein(uniprot_id, distance, max_depth=depth)

class meta:
    
    def get(species_name=None, protein_name=None, uniprot_id=None, ncbi_taxon_id=None):

        if uniprot_id is not None:  # uniprot_id exists, follow uniprot_id
            return Manager().manager.get_meta_by_id(uniprot_id)
        elif protein_name is not None and ncbi_taxon_id is None and species_name is None:  # all proteins with name across organisms
            return Manager().manager.get_info_by_text(protein_name)
        elif protein_name is not None and ncbi_taxon_id is not None and species_name is None:  # all proteins with name in taxon_id
            return Manager().manager.get_meta_by_name_taxon(protein_name, ncbi_taxon_id)
        elif protein_name is not None and species_name is not None:  # all proteins with name in species_name
            return Manager().manager.get_meta_by_name_name(protein_name, species_name)
        else:
            return 'No such query combination exists'
