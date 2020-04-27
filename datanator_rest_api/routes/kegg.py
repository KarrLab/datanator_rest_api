""" Metabolites collection controller
This file defines the methods for the operations on the Metabolites collection.
The root class contains the HTTP methods for the /metabolites/ path
Any subpaths are contained in an internal class

:Author: Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2020-02-06
:Copyright: 2019, Karr Lab
:License: MIT
"""
from datanator_query_python.config.query_manager import KeggManager
from datanator_rest_api.util import paginator


k_manager = KeggManager().kegg_manager()

class get_meta:

    def get(kegg_ids, _from=0, size=10):
        docs, count = k_manager.get_meta_by_kegg_ids(kegg_ids)
        manager = paginator.Paginator(count, list(docs))
        return manager.page(_from=_from, size=size)