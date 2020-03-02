"""  RNA Controller

:Author: Zhouyang Lian < zhouyang.lian@familian.life >
:Date: 2019-08-21
:Copyright: 2019, Karr Lab
:License: MIT
"""

from datanator_query_python.config import query_manager


class halflife:


    class get_info_by_protein_name:

        def get(protein_name='Protein translocase subunit SecD', _from=0, size=10, 
        taxon_distance=True, ncbi_taxonomy_id=9606):
            result = []
            docs, _ = query_manager.RnaManager().rna_manager().get_doc_by_protein_name(protein_name, _from=_from,
                                                                                          size=size)
            for doc in docs:
                if taxon_distance:
                    for sub_doc in doc['halflives']:
                        _id = sub_doc['ncbi_taxonomy_id']
                        sub_doc['taxon_distance'] = query_manager.TaxonManager().txn_manager().get_common_ancestor(_id, ncbi_taxonomy_id, org_format='_id')
                else:
                    result.append(doc)
            return result