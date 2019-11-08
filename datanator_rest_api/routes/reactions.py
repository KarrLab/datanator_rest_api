"""  Reactions Controller

:Author: Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2019-10-21
:Copyright: 2019, Karr Lab
:License: MIT
"""


from datanator_query_python.config.query_manager import RxnManager
from datanator_rest_api.util import paginator


class kinlaw_by_rxn:

    def get(substrates, products, _from, size, dof):
        projection = {'_id': 0}
        print(projection)
        count, docs = RxnManager().rxn_manager().get_kinlaw_by_rxn(substrates, products, dof=dof, projection=projection)
        manager = paginator.Paginator(count, docs)
        return manager.page(_from=_from, size=size)


class kinlaw_doc:
    
    def get(kinlaw_id, _from, size):
        projection = {'_id': 0}
        docs, count = RxnManager().rxn_manager().get_reaction_doc(kinlaw_id, projection=projection)
        manager = paginator.Paginator(count, docs)
        return manager.page(_from=_from, size=size)


class kinlaw_entry:

    def get(entry_id):
        result = RxnManager().rxn_manager().get_kinlaw_by_entryid(entry_id)
        return result