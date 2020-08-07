""" Full text search
perform full text search

:Author: Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2020-08-05
:Copyright: 2019, Karr Lab
:License: MIT
"""
from datanator_query_python.query_schema_2 import query_observation

o_manager = query_observation.QueryObs()

class get_protein_datatype:
    def get(identifier, datatype="half-life", limit=10, skip=0):
        identifier = {"namespace": identifier["namespace"],
                      "value": identifier["value"]}
        return o_manager.get_protein_datatype(identifier,
                                              datatype=localization,
                                              limit=limit,
                                              skip=skip)