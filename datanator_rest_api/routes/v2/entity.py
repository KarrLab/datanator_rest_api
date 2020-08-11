""" Full text search
perform full text search

:Author: Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2020-08-10
:Copyright: 2019, Karr Lab
:License: MIT
"""
from datanator_query_python.query_schema_2 import query_entity

e_manager = query_entity.QueryEn()

class get_entity_meta:
    def get(identifier, datatype="metabolite", limit=10, skip=0):
        identifier = {"namespace": identifier["namespace"],
                      "value": identifier["value"]}
        return e_manager.query_entity(identifier,
                                    datatype=datatype,
                                    limit=limit,
                                    skip=skip)