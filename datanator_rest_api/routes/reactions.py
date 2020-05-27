"""  Reactions Controller

:Author: Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2019-10-21
:Copyright: 2019, Karr Lab
:License: MIT
"""


from datanator_query_python.config.query_manager import RxnManager
from datanator_query_python.aggregate import pipelines
from datanator_query_python.config import query_manager
from datanator_rest_api.util import paginator, taxon_distance
from collections import deque


r_manager = RxnManager().rxn_manager()
dist_manager = taxon_distance.TaxonDist()

def get_kegg_meta(ec, projection):
    return r_manager.db_obj['kegg_orthology'].find_one(filter={'definition.ec_code': ec},
                                                       projection=projection)


class kinlaw_by_rxn:

    def get(substrates, products, _from, size, bound, dof,
            taxon_distance=False, species='homo sapiens',
            projection="{'kegg_meta.gene_ortholog': 0, 'kegg_meta._id': 0, '_id': 0}"):
        result = []
        projection = eval(projection)
        _, docs = r_manager.get_kinlaw_by_rxn(substrates, products, dof=dof, 
                                              projection=projection, bound=bound,
                                              skip=_from, limit=size)
        if taxon_distance:
            result = dist_manager.arrange_distance_objs(docs, target_species=species, tax_field='taxon_name', org_format='tax_name')
        for doc in docs:
            result.append(doc)
        return result


class kinlaw_by_name:

    def get(substrates, products, _from, size, bound, taxon_distance=True, 
            species='homo sapiens', projection="{'kegg_meta.gene_ortholog': 0, 'kegg_meta._id': 0, '_id': 0}"):
        result = []
        projection = eval(projection)
        _, docs = r_manager.get_kinlaw_by_rxn_name(substrates, products, 
                                                   projection=projection, bound=bound, skip=_from, limit=size)
        if taxon_distance:
            docs = dist_manager.arrange_distance_objs(docs, target_species=species, tax_field='taxon_name', org_format='tax_name')
        for doc in docs:
            result.append(doc)
        return result


class kinlaw_doc:
    
    def get(kinlaw_id, _from, size):
        projection = {'_id': 0}
        docs, count = r_manager.get_reaction_doc(kinlaw_id, projection=projection)
        manager = paginator.Paginator(count, docs)
        return manager.page(_from=_from, size=size)

    class with_prm:

        def get(kinlaw_ids, _from=0, size=10):
            result, _ = r_manager.get_rxn_with_prm(kinlaw_ids, _from=_from, size=size)
            return result


class kinlaw_entry:

    def get(entry_id, target_organism=None, last_id=0, size=10):
        docs = r_manager.get_info_by_entryid(entry_id, target_organism=target_organism,
                                             size=size, last_id=last_id)
        return list(docs)


class summary:

    class num_organism:

        def get():
            return r_manager.get_unique_organisms()

    class num_entries:
        
        def get():
            return r_manager.get_unique_entries()

    class num_parameter_km:

        def get():
            return r_manager.collection.count_documents({'parameter.observed_name': 'Km'}, collation=r_manager.collation)


    class num_parameter_kcat:

        def get():
            return r_manager.collection.count_documents({'parameter.observed_name': {
                                                         '$in': ['kcat', 'k_cat']}}, 
                                                         collation=r_manager.collation)


    class get_distinct:

        def get(_input):
            return r_manager.collection.distinct(_input)


    class num_refs:
        def get():
            docs = r_manager.collection.aggregate([
                    { "$match": {"resource.namespace": "pubmed"}},
                    { "$redact": {
                        "$cond": {
                            "if": {"$eq": [ {"$ifNull": ["$namespace", "pubmed"]}, "pubmed"]},
                            "then": "$$DESCEND",
                            "else": "$$PRUNE"
                        }
                    }},
                    {"$unwind": "$resource"},
                    {"$group": {
                        "_id": "$resource.id",
                        "count": {"$sum": 1}
                    }}
                ])
            tmp = deque()
            for doc in docs:
                tmp.append(doc)
            return len(tmp)          


    class get_frequency:

        def get(field):
            nums = r_manager.db_obj['sabio_rk'].count_documents({})
            return [doc for doc in r_manager.db_obj['sabio_rk'].aggregate(
                    [{'$group': { '_id' : '${}'.format(field), 'count' : {'$sum' : 1}}},
                     {"$project": { 
                        "count": 1, 
                        "percentage": { 
                                "$multiply": [{"$divide": ["$count", nums]}, 100]
                            }
                        }
                     },
                     {"$sort": {"count": -1 }}
                    ]
                    )]


    class get_brenda_obs:
        def get(parameter):
            pipeline = pipelines.Pipeline().aggregate_total_array_length(parameter)
            for doc in r_manager.db_obj['ec'].aggregate(pipeline):
                return doc['total']