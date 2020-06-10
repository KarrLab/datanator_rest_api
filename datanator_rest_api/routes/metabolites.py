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
from datanator_rest_api.util import taxon_distance
from collections import deque
from bson.objectid import ObjectId


ey_manager = query_manager.Manager().eymdb_manager()
m_manager = query_manager.Manager().metabolite_manager()
mm_manager = query_manager.metabolites_meta_manager()
mc_manager = query_manager.Manager().metabolite_concentration_manager()
dist_manager = taxon_distance.TaxonDist()


def put(body):
    return ("test")


def post():
    return ("")


def get(inchi, species, last_id='000000000000000000000000', page_size=20):
    last_id = ObjectId(last_id)
    print(len(inchi))
    return ey_manager.get_meta_from_inchis(inchi, species, last_id=last_id, page_size=page_size)


class concentrations:

    def get(inchikey, species='Escherichia coli', taxon_distance=False):
        query = {'inchikey': inchikey}
        result = m_manager.db_obj['metabolite_concentrations'].find_one(filter=query, projection={'_id': 0})
        if not result:
            return {}
        if taxon_distance:
            _ = dist_manager.arrange_distance_objs(result["concentrations"], target_species=species, tax_field='species_name', org_format='tax_name')
        return result

    class similar_compounds:

        def get(inchikey, threshold=0.6, target_species='homo sapiens', taxon_distance=False):
            docs = mc_manager.get_similar_concentrations(inchikey, threshold=threshold)
            doc = concentrations.get(inchikey, species=target_species, taxon_distance=False)
            if doc != {}:
                doc['similarity_score'] = 1.0
                docs.insert(0, doc)
            if not taxon_distance or docs == []:
                return docs
            else:
                queried_species = deque()
                distance_obj = {}
                for doc in docs:
                    for i, concentration in enumerate(doc['concentrations']):
                        queried_species, distance_obj, concentration = dist_manager.get_dist_object(concentration, queried_species, distance_obj,
                                                                                         target_species, tax_field='species_name', org_format='tax_name')
                        doc['concentrations'][i] = concentration
                return docs


class summary:

    class concentration_count():
    
        def get():
            return mc_manager.get_conc_count()


    class ymdb_conc_count():
        def get():
            return 1462


    class ecmdb_conc_count():
        def get():
            return 1196


    class ecmdb_ref_count():
        def get():
            # docs = ey_manager.collection_ecmdb.aggregate([
            #         {"$project": {"concentrations": 1}},
            #         {"$match": {"concentrations": {"$ne": None}}},
            #         {"$unwind": "$concentrations"},
            #         {"$group": {
            #             "_id": "$concentrations.reference.pubmed_id",
            #             "count": {"$sum": 1}
            #         }}
            #     ])
            # count = 0
            # for doc in docs:
            #     count += 1
            # return count
            return 43


    class ymdb_ref_count():
        def get():
            # docs = ey_manager.collection_ymdb.aggregate([
            #         {"$project": {"concentrations": 1}},
            #         {"$match": {"concentrations": {"$ne": None}}},
            #         {"$unwind": "$concentrations"},
            #         {"$group": {
            #             "_id": "$concentrations.reference.pubmed_id",
            #             "count": {"$sum": 1}
            #         }}
            #     ])
            # count = 0
            # for doc in docs:
            #     count += 1
            # return count
            return 1462 


    class curated_ref_count():
        def get():
            return 4

    
    class ecmdb_doc_count():
        
        def get():
            return ey_manager.collection_ecmdb.count_documents({})


    class ymdb_doc_count():
        
        def get():
            return ey_manager.collection_ymdb.count_documents({})

    
    class get_distinct():
        def get(_input):
            return len(m_manager.db_obj['metabolite_concentrations'].distinct(_input))


class meta:

    def get(inchikey, projection="{'_id': 0, 'kegg_meta.gene_ortholog': 0}"):
        projection = eval(projection)
        doc =  mm_manager._collection.find_one({'InChI_Key': inchikey}, projection=projection,
                                              collation=mm_manager.collation)
        if doc:
            return doc
        else:
            return {}


class concentration_only:

    def get(inchi_key):
        return ey_manager.get_conc_from_inchi(inchi_key, inchi_key=True, projection={'_id':0, 'concentrations': 1})