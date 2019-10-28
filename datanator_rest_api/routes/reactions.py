"""  Reactions Controller

:Author: Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2019-10-21
:Copyright: 2019, Karr Lab
:License: MIT
"""


from datanator_query_python.config.query_manager import RxnManager


class KinlawIdByRxn:

    def get(substrates, products, dof=0, projection={'kinlaw_id': 1, '_id': 0}):
        count, docs = RxnManager().rxn_manager().get_kinlaw_by_rxn(substrates, products, dof=dof, projection=projection)
        return count, docs