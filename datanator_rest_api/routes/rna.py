"""  RNA Controller

:Author: Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2019-08-21
:Copyright: 2019, Karr Lab
:License: MIT
"""

from datanator_query_python.config import query_manager
import simplejson as json
from collections import deque
from datanator_rest_api.util import taxon_distance


rna_manager = query_manager.RnaManager().rna_manager()
dist_manager = taxon_distance.TaxonDist()


def append_taxon_distance(doc, result, species):
    for sub_doc in doc['halflives']:
        name = sub_doc.get('species')
        dist = query_manager.TaxonManager().txn_manager().get_canon_common_ancestor(name, species, org_format='tax_name')
        sub_doc['taxon_distance'] = dist
    result.append(doc)

def get_kegg_meta(ko):
    return rna_manager.db_obj['kegg_orthology'].find_one(filter={'kegg_orthology_id': ko},
                                                         projection={'_id': 0}, 
                                                         collation=rna_manager.collation)

class halflife:

    class get_info_by_name:

        def get(protein_name='Protein translocase subunit SecD', _from=0, size=10, 
        taxon_distance=True, species='homo sapiens'):
            result = []
            docs, _ = rna_manager.get_doc_by_names(protein_name, _from=_from,
                                                   size=size)
            for doc in docs:
                ko = doc.get('ko_number')
                doc['kegg_meta'] = get_kegg_meta(ko)
                doc = json.loads(json.dumps(doc, ignore_nan=True))
                if taxon_distance:
                    append_taxon_distance(doc, result, species)
                else:
                    result.append(doc)
            return result

    
    class get_info_by_ko:

        def get(ko_number, _from=0, size=10, 
                taxon_distance=True, species='homo sapiens'):
            result = []
            docs, _ = rna_manager.get_doc_by_ko(ko_number, _from=_from,
                                                size=size)
            for doc in docs:
                doc['kegg_meta'] = get_kegg_meta(ko_number)
                doc = json.loads(json.dumps(doc, ignore_nan=True))
                if taxon_distance:
                    append_taxon_distance(doc, result, species)
                else:
                    result.append(doc)
            return result

    
class modification:


    class get_modifications_by_ko:
        def get(ko_number, _from=0, size=10, target_organism='Escherichia coli', taxon_distance=False):
            result = []
            query = {"kegg_orthology_id": ko_number}
            docs = rna_manager.db_obj['rna_modification'].find(filter=query, skip=_from,
                                                                limit=size, projection={'_id': 0})
            if not docs:
                return []
            else:
                if not taxon_distance:
                    for doc in docs:
                        result.append(doc)
                else:
                    queried_species = deque()
                    distance_obj = {}
                    for doc in docs: # iterate documents
                        mods = doc.get('modifications')
                        if not mods:  # document has no modifications field
                            result.append(doc)
                        else: # iterate modification field in document and calc taxon distance
                            for i, mod in enumerate(mods):
                                queried_species, distance_obj, mod = dist_manager.get_dist_object(mod, queried_species, distance_obj,
                                                                                                  target_organism, tax_field='organism', org_format='tax_name')
                                doc['modifications'][i] = mod
                            result.append(doc)
                return result


class summary:

    class get_total_docs:
        
        def get():
            return rna_manager.collection.count_documents({})

    class get_publication_num:

        def get():
            return len(rna_manager.collection.distinct('halflives.reference.doi'))

    class get_distinct:
        
        def get(_input):
            return len(rna_manager.collection.distinct(_input))