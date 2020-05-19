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
from collections import deque
from bson.objectid import ObjectId


ey_manager = query_manager.Manager().eymdb_manager()
m_manager = query_manager.Manager().metabolite_manager()
mm_manager = query_manager.metabolites_meta_manager()
mc_manager = query_manager.Manager().metabolite_concentration_manager()

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
            for concentration in result["concentrations"]:
                name = concentration['species_name']
                dist = query_manager.TaxonManager().txn_manager().get_canon_common_ancestor(name, species, org_format='tax_name')
                concentration['taxon_distance'] = dist
        return result

    class similar_compounds:

        def get(inchikey, threshold=0.6, target_species='homo sapiens', taxon_distance=False):
            docs = mc_manager.get_similar_concentrations(inchikey, threshold=threshold)
            if not taxon_distance or docs == []:
                return docs
            else:
                queried_species = deque()
                distance_obj = {}
                for doc in docs:
                    for concentration in doc['concentrations']:
                        name = concentration['species_name']
                        if name not in queried_species:
                            dist = query_manager.TaxonManager().txn_manager().get_canon_common_ancestor(name, target_species, org_format='tax_name')
                            distance_obj[name] = dist
                            queried_species.append(name)
                            concentration['taxon_distance'] = dist
                        else:
                            concentration['taxon_distance'] = distance_obj[name]
                return docs


class summary:

    class concentration_count():
    
        def get():
            return ey_manager.get_concentration_count()

    
    class ecmdb_doc_count():
        
        def get():
            return ey_manager.collection_ecmdb.count_documents({})


    class ymdb_doc_count():
        
        def get():
            return ey_manager.collection_ymdb.count_documents({})


    class get_ref_count:

        def get():
            return len(ey_manager.collection_ecmdb.distinct('syntehsis_reference')) + len(ey_manager.collection_ymdb.distinct('syntehsis_reference'))


class concentration:

    def get(metabolite, species='Escherichia coli', abstract=False):
        return m_manager.molecule_name_query(metabolite, species, abstract_default=abstract)


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