""" Full text search
perform full text search

:Author: Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2019-10-20
:Copyright: 2019, Karr Lab
:License: MIT
"""
from datanator_query_python.config import query_manager


f_manager = query_manager.FtxManager().ftx_manager()

class text_search:

    def get(query_message, index, from_, size, fields, _source_includes=[]):
        r = f_manager.simple_query_string(query_message, index, from_=from_, 
                                          size=size, fields=fields, _source_includes=_source_includes)
        return r


    class indices_in_page:
        
        def get(query_message, iof, index, from_, size, fields):
            r = f_manager.simple_query_string(query_message, index, from_=from_, 
                                              size=size, fields=fields)
            result = f_manager.get_index_in_page(r, iof)
            return result

    
    class num_of_index:

        def get(query_message, index, from_, size, fields):
            r = f_manager.get_single_index_count(query_message, index, size,
                                                 fields=fields, from_=from_)
            return r


    class frontend_num_of_index:

        def get(query_message, indices, size, fields, from_=0):
            result = []
            indices = indices.split(',')
            r = {}
            for index in indices:
                if index == 'protein' or index == 'rna':
                    r = f_manager.get_index_ko_count(query_message, size,
                                                     index=index, fields=fields, from_=from_)
                else:
                    r = f_manager.get_single_index_count(query_message, index, size,
                                                         fields=fields)
                result.append(r)
            return result


    class gene_ranked_by_ko:

        def get(query_message, from_, size, fields=['*']):
            r = f_manager.get_genes_ko_count(query_message, size,
                                             fields=fields, from_=from_)
            return r
