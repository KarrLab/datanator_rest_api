""" Proteins Controller

:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
         Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2019-08-21
:Copyright: 2019, Karr Lab
:License: MIT
"""


from datanator_query_python.config import query_manager


p_manager = query_manager.Manager().protein_manager()

def get():
    return("")


def put(body):
    return ("")


def post(body):
    return ("")


class precise_abundance:

    def get(uniprot_id=None, kegg_orthology=None):
        if uniprot_id is not None and kegg_orthology is None:
            return p_manager.get_abundance_by_id(uniprot_id)
        elif uniprot_id is None and kegg_orthology is not None:
            return p_manager.get_abundance_by_ko(kegg_orthology)
        else: 
            return [{'uniprot_id': 'One and only one input option is allowed.', 'abundances': []}]


class proximity_abundance:

    def get(uniprot_id, distance, depth):
        return p_manager.get_equivalent_protein_with_anchor(uniprot_id, distance, max_depth=depth)

    
    class proximity_abundance_kegg:

        def get(kegg_id, distance, anchor='homo sapiens'):
            return p_manager.get_all_kegg(kegg_id, anchor, distance)


class meta:

    class meta_combo:

        def get(uniprot_id=None, ncbi_taxon_id=None, species_name=None, name=None):
            if uniprot_id is not None:   # uniprot_id
                return p_manager.get_meta_by_id(uniprot_id)
            elif name is not None and ncbi_taxon_id is not None and species_name is None:  # name + taxon_id
                return p_manager.get_meta_by_name_taxon(name, ncbi_taxon_id)
            elif name is not None and species_name is not None:   # name + species_name
                return p_manager.get_meta_by_name_name(name, species_name)
            else:
                return wrong

    class meta_single:

        def get(name=None, ncbi_taxon_id=None, ko=None):
            if name is not None and ncbi_taxon_id is None and ko is None:  # name only
                return p_manager.get_info_by_text_abundances(name)
            # elif name is None and ncbi_taxon_id is not None and ko is None:  # taxon_id only
            #     return p_manager.get_info_by_taxonid_abundance(ncbi_taxon_id)
            elif name is None and ncbi_taxon_id is None and ko is not None:  # ko only
                return p_manager.get_info_by_ko_abundance(ko)
            else:
                return [{'uniprot_ids': {}, 'ko_name': ['invalid input'], 'ko_number': 'This combination of input is invalid.'}]


class summary:

    class num_organism:

        def get():
            return p_manager.get_unique_organism()

    class num_protein:
        
        def get():
            return p_manager.get_unique_protein()

    class num_abundances():

        def get():
            return p_manager.collection.count_documents({'abundances': {"$exists": True}})

    
    class num_publications():

        def get():
            return p_manager.paxdb_collection.count_documents({})


class similar_protein:

    class refseq:
        def get(uniprot_id, identity=90):
            return query_manager.uniprot_manager().get_similar_proteins(uniprot_id, identity=identity)


class related:

    class related_reactions:
        def get(ko):
            lists = p_manager.get_info_by_ko(ko)
            uniprot_ids = lists[0]['uniprot_ids']
            kinlaw_ids = query_manager.RxnManager().rxn_manager().get_reaction_by_subunit(uniprot_ids)
            return list(kinlaw_ids)
