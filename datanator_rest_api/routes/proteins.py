""" Proteins Controller

:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
         Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2019-08-21
:Copyright: 2019, Karr Lab
:License: MIT
"""
from datanator_query_python.config import query_manager


def get():
    return("get")


def put(body):
    return ("put")


def post(body):
    return ("post")

class precise_abundance:

    def get(uniprot_id):
        return query_manager.Manager().protein_manager().get_abundance_by_id(uniprot_id)


class proximity_abundance:

    def get(uniprot_id, distance, depth):
        return query_manager.Manager().protein_manager().get_equivalent_protein(uniprot_id, distance, max_depth=depth)


class meta:

    class meta_combo:

        def get(uniprot_id=None, ncbi_taxon_id=None, species_name=None, name=None):
            if uniprot_id is not None:   # uniprot_id
                return query_manager.Manager().protein_manager().get_meta_by_id(uniprot_id)
            elif name is not None and ncbi_taxon_id is not None and species_name is None:  # name + taxon_id
                return query_manager.Manager().protein_manager().get_meta_by_name_taxon(name, ncbi_taxon_id)
            elif name is not None and species_name is not None:   # name + species_name
                return query_manager.Manager().protein_manager().get_meta_by_name_name(name, species_name)
            else:
                return 'Please try another input combination'

    class meta_single:

        def get(name=None, ncbi_taxon_id=None, ko=None):
            if name is not None and ncbi_taxon_id is None and ko is None:  # name only
                return query_manager.Manager().protein_manager().get_info_by_text(name)
            elif name is None and ncbi_taxon_id is not None and ko is None:  # taxon_id only
                return query_manager.Manager().protein_manager().get_info_by_taxonid(ncbi_taxon_id)
            elif name is None and ncbi_taxon_id is None and ko is not None:  # ko only
                return query_manager.Manager().protein_manager().get_info_by_ko(ko)
            else:
                return "This combination of input is not valid."
