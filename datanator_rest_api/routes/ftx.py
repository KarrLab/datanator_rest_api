""" Full text search
perform full text search

:Author: Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2019-10-20
:Copyright: 2019, Karr Lab
:License: MIT
"""
from datanator_query_python.config import query_manager


class text_search:

    def get(query_message, index, from_, size, fields):
        r = query_manager.FtxManager().ftx_manager().simple_query_string(query_message, index, from_=from_, 
                                                                        size=size, fields=fields, lenient=True,
                                                                        analyze_wild_card=True)
        return r


    class indices_in_page:
        
        def get(query_message, iof, index, from_, size, fields):
            r = query_manager.FtxManager().ftx_manager().simple_query_string(query_message, index, from_=from_, 
                                                                            size=size, fields=fields, lenient=True,
                                                                            analyze_wild_card=True)
            result = query_manager.FtxManager().ftx_manager().get_index_in_page(r, iof)
            return result

    
    class num_of_index:

        def get(query_message, index, size, fields):
            r = query_manager.FtxManager().ftx_manager().get_single_index_count(query_message, index, size,
                                                                                fields=fields, lenient=True,
                                                                                analyze_wild_card=True)
            return r
