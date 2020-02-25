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


class canon_rank_distance_by_name:

    def get(name):
        results = TaxonManager().txn_manager().get_canon_rank_distance_by_name(name, front_end=True)
        return results


class is_child:
    
    def get(src_tax_ids, target_tax_id):
        return TaxonManager().txn_manager().each_under_category(src_tax_ids, target_tax_id)


class canon_rank_common_distance:

    def get(org_0, org_1):
        return TaxonManager().txn_manager().get_canon_common_ancestor(org_0, org_1)