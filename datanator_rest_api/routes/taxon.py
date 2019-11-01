"""  Reactions Controller

:Author: Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2019-10-28
:Copyright: 2019, Karr Lab
:License: MIT
"""


from datanator_query_python.config.query_manager import TaxonManager


class canon_rank_distance:

    def get(ncbi_id):
        results = TaxonManager().txn_manager().get_canon_rank_distance(ncbi_id, front_end=True)
        return results