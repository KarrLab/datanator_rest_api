"""  Reactions Controller

:Author: Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2019-10-21
:Copyright: 2019, Karr Lab
:License: MIT
"""


from datanator_query_python.config.query_manager import RxnManager
from datanator_query_python.config import query_manager
from datanator_rest_api.util import paginator


r_manager = RxnManager().rxn_manager()

class kinlaw_by_rxn:

    def get(substrates, products, _from, size, bound, dof):
        projection = {'_id': 0}
        count, docs = r_manager.get_kinlaw_by_rxn(substrates, products, dof=dof, 
                                                                   projection=projection, bound=bound)
        manager = paginator.Paginator(count, docs)
        return manager.page(_from=_from, size=size)


class kinlaw_by_name:

    def get(substrates, products, _from, size, bound, taxon_distance=True, 
            species='homo sapiens', projection="{'_id': 0, 'kegg_meta.gene_ortholog': 0, 'anc_id': 0, 'anc_name': 0}"):
        result = []
        projection = eval(projection)
        print(substrates)
        print(products)
        _, docs = r_manager.get_kinlaw_by_rxn_name(substrates, products, 
                                                   projection=projection, bound=bound, skip=_from, limit=size)
        for doc in docs:
            if taxon_distance:
                name = doc['taxon_name']
                dist = query_manager.TaxonManager().txn_manager().get_canon_common_ancestor(name, species, org_format='tax_name')
                doc['taxon_distance'] = dist
                result.append(doc)
            else:
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
        return docs


class summary:

    class num_organism:

        def get():
            return r_manager.get_unique_organisms()

    class num_entries:
        
        def get():
            return r_manager.get_unique_entries()