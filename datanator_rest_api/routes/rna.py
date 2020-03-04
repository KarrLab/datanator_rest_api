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
        taxon_distance=True, species='homo sapiens'):
            result = []
            docs, _ = query_manager.RnaManager().rna_manager().get_doc_by_protein_name(protein_name, _from=_from,
                                                                                          size=size)
            for doc in docs:
                if taxon_distance:
                    for sub_doc in doc['halflives']:
                        name = sub_doc.get('species')
                        dist = query_manager.TaxonManager().txn_manager().get_canon_common_ancestor(name, species, org_format='tax_name')
                        sub_doc['taxon_distance'] = dist
                    result.append(doc)
                else:
                    result.append(doc)
            return result