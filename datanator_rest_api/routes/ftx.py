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
                                                                        size=size, fields=fields)
        return r


    class indices_in_page:
        
        def get(query_message, iof, index, from_, size, fields):
            r = query_manager.FtxManager().ftx_manager().simple_query_string(query_message, index, from_=from_, 
                                                                            size=size, fields=fields)
            result = query_manager.FtxManager().ftx_manager().get_index_in_page(r, iof)
            return result

    
    class num_of_index:

        def get(query_message, index, from_, size, fields):
            r = query_manager.FtxManager().ftx_manager().get_single_index_count(query_message, index, size,
                                                                                fields=fields, from_=from_)
            return r


    class frontend_num_of_index:

        def get(query_message, indices, size, fields):
            result = []
            indices = indices.split(',')
            r = {}
            for index in indices:
                if index == 'protein':
                    r = query_manager.FtxManager().ftx_manager().get_protein_ko_count(query_message, size,
                                                                                      fields=fields)
                else:
                    r = query_manager.FtxManager().ftx_manager().get_single_index_count(query_message, index, size,
                                                                                        fields=fields)
                result.append(r)
            return result


    class protein_ranked_by_ko:

        def get(query_message, from_, size, fields):
            r = query_manager.FtxManager().ftx_manager().get_protein_ko_count_abundance(query_message, size,
                                                                              fields=fields, from_=from_)
            return r
