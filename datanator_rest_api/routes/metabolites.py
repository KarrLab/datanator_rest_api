""" Metabolites collection controller
This file defines the methods for the operations on the Metabolites collection.
The root class contains the HTTP methods for the /metabolites/ path
Any subpaths are contained in an internal class

:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
:Author: Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2019-08-20
:Copyright: 2019, Karr Lab
:License: MIT
"""
from datanator_query_python.config import query_manager
from bson.objectid import ObjectId

def put(body):
    return ("test")


def post():
    return ("")


def get(inchi, species, last_id='000000000000000000000000', page_size=20):
    last_id = ObjectId(last_id)
    print(len(inchi))
    return query_manager.Manager().eymdb_manager().get_meta_from_inchis(inchi, species, last_id=last_id, page_size=page_size)


class concentrations:
    def get(inchi, consensus=False):
        return query_manager.Manager().eymdb_manager().get_conc_from_inchi(inchi, consensus=consensus)


class summary:

    class concentration_count():
    
        def get():
            return query_manager.Manager().eymdb_manager().get_concentration_count()


class concentration:

    def get(metabolite, species='Escherichia coli', abstract=False):
        return query_manager.Manager().metabolite_manager().molecule_name_query(metabolite, species, abstract_default=abstract)


class meta:

    def get(inchi_key):
        return query_manager.metabolites_meta_manager().get_metabolites_meta(inchi_key)


class concentration_only:

    def get(inchi_key):
        return query_manager.Manager().eymdb_manager().get_conc_from_inchi(inchi_key, inchi_key=True, projection={'_id':0, 'concentrations': 1})