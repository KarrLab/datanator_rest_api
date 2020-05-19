from datanator_query_python.config import query_manager


class TaxonDist:

    def __init__(self, debugging=False):
        self.debugging = debugging

    def get_dist_object(self, doc, queried_species, distance_obj,
                    target_species, org_format='tax_id',
                    tax_field='species_name', obj_name='taxon_distance'):
        """Return taxon_distance object for frontend.

        Args:
            doc(:obj:`Obj`): documents that need to be processed.
            queried_species (:obj:`deque`): already queried species.
            distance_obj (:obj:`Obj`): distance objects containing already queries species.
            target_species (:obj:`str` or :obj:`int`): target species.
            org_format (:obj:`str`, optional): format of species identifier (tax_id or tax_name). Defaults to 'tax_id'.
            tax_field(:obj:`str`, optional): field containing taxon information in documents.
            obj_name(:obj:`str`, optional): name of the object containing taxon distance information.

        Return:
            (:obj:`tuple` of :obj:`list`, :obj:`Obj`, :obj:`Obj`)
        """
        self.manager = query_manager.TaxonManager().txn_manager()
        name = doc[tax_field]
        if name not in queried_species:
            dist = self.manager.get_canon_common_ancestor(name, target_species, org_format=org_format)
            distance_obj[name] = dist
            queried_species.append(name)
            doc[obj_name] = dist
            if self.debugging:
                doc['queried'] = True
        else:
            doc[obj_name] = distance_obj[name]
            if self.debugging:
                doc['queried'] = False
        return queried_species, distance_obj, doc