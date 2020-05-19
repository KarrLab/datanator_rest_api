from datanator_query_python.config import query_manager


class TaxonDist:

    def __init__(self):
        pass

    def dist_object(self, doc, queried_species, distance_obj,
                    name, target_species, org_format='tax_id',
                    tax_field='species_name', obj_name='taxon_distance'):
        """Return taxon_distance object for frontend.

        Args:
            doc(:obj:`Obj`): documents that need to be processed.
            queried_species (:obj:`deque`): already queried species.
            distance_obj (:obj:`Obj`): distance objects containing already queries species.
            name (:obj:`str` or :obj:`int`): name of species.
            target_species (:obj:`str` or :obj:`int`): target species.
            org_format (:obj:`str`, optional): format of species identifier (tax_id or tax_name). Defaults to 'tax_id'.
            tax_field(:obj:`str`, optional): field containing taxon information in documents.
            obj_name(:obj:`str`, optional): name of the object containing taxon distance information.

        Return:
            (:obj:`tuple` of :obj:`list`, :obj:`Obj`, :obj:`Obj`)
        """
        name = doc[tax_field]
        if name not in queried_species:
            dist = query_manager.TaxonManager().txn_manager().get_canon_common_ancestor(name, target_species, org_format='tax_name')
            distance_obj[name] = dist
            queried_species.append(name)
            doc['taxon_distance'] = dist
        else:
            doc['taxon_distance'] = distance_obj[name]
        return queried_species, distance_obj, doc