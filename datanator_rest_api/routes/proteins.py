""" Proteins Controller

:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
         Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2019-08-21
:Copyright: 2019, Karr Lab
:License: MIT
"""


from datanator_query_python.config import query_manager
from datanator_query_python.aggregate import pipelines
from datanator_rest_api.util import taxon_distance
import simplejson as json


p_manager = query_manager.Manager().protein_manager()
p_manager_new = query_manager.Manager().protein_manager(database="datanator-test")
dist_manager = taxon_distance.TaxonDist()


def get():
    return("")


def put(body):
    return ("")


def post(body):
    return ("")


class precise_abundance:

    def get(uniprot_id=None, target_species='homo sapiens',
            taxon_distance=False):
        docs = p_manager.get_abundance_by_id(uniprot_id)
        result = []
        if taxon_distance:
            docs = dist_manager.arrange_distance_objs(docs, target_species=target_species, tax_field='species_name', org_format='tax_name')
        for doc in docs:
            doc = json.loads(json.dumps(doc, ignore_nan=True))
            result.append(doc)
        return result


class proximity_abundance:

    def get(uniprot_id, distance, depth):
        return p_manager.get_equivalent_protein_with_anchor(uniprot_id, distance, max_depth=depth)

    
    class proximity_abundance_kegg:

        def get(kegg_id, distance, anchor='homo sapiens'):
            return p_manager_new.get_all_ortho(kegg_id, anchor, distance)


class meta:

    class meta_combo:

        def get(uniprot_id=None, ncbi_taxon_id=None, species_name=None, name=None):
            if uniprot_id is not None:   # uniprot_id
                return p_manager_new.get_ortho_by_id(uniprot_id[0])
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

    
    class num_obs_abundances():
        def get():
            pipeline = pipelines.Pipeline().aggregate_total_array_length("observation")
            for doc in p_manager.db_obj['pax'].aggregate(pipeline):
                return doc['total']


    class num_obs_modifications():
        def get():
            # pipeline = pipelines.Pipeline().aggregate_total_array_length("modifications.reference")
            # pipeline.insert(0, {"$match": {"modifications.reference": {"$exists": True}}})
            # for doc in p_manager.db_obj['uniprot'].aggregate(pipeline, hint="modifications.reference_1"):
            #     return doc['total'] 
            return 13470

    
    class num_publications():

        def get():
            return p_manager.paxdb_collection.count_documents({})


# class similar_protein:

#     class refseq:
#         def get(uniprot_id, identity=90):
#             return query_manager.uniprot_manager().get_similar_proteins(uniprot_id, identity=identity)


class related:

    class related_reactions_by_kegg:
        def get(ko):
            lists = p_manager_new.get_info_by_orthodb(ko)
            uniprot_ids = lists[0]['uniprot_ids']
            kinlaw_ids = query_manager.RxnManager().rxn_manager().get_reaction_by_subunit(uniprot_ids)
            return list(kinlaw_ids)

    class related_reactions_by_uniprot:
        def get(uniprot_id):
            kinlaw_ids = query_manager.RxnManager().rxn_manager().get_reaction_by_subunit([uniprot_id])
            return list(kinlaw_ids)            
