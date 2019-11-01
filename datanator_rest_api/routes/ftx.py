""" Full text search
perform full text search

:Author: Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2019-10-20
:Copyright: 2019, Karr Lab
:License: MIT
"""
from datanator_query_python.config import query_manager


class text_search:

    def get(query_message, index, from_=0, size=10, fields=['protein_name', 'synonyms', 'enzymes', 'ko_name', 'gene_name']):
        r = query_manager.FtxManager().ftx_manager().simple_query_string(query_message, index, from_=from_, 
                                                                        size=size, fields=fields)
        return r