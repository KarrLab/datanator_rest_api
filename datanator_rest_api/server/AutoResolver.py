from connexion.resolver import RestyResolver
import re


class AutoResolver(RestyResolver):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def resolve_operation_id_using_rest_semantics(self, operation):
        """
        Resolves the operationId using REST semantics
        :type operation: connexion.operations.AbstractOperation
        """
        path_match = re.search(
            r'^/?(?P<resource_name>([\w\-](?<!/))*)(?P<trailing_slash>/*)(?P<extended_path>.*)$', operation.path
        )

        def get_controller_name():

            name = self.default_module_name
            resource_name = path_match.group('resource_name')

            if resource_name:
                resource_controller_name = resource_name.replace('-', '_')
                name += '.' + resource_controller_name

            return name

        def get_path_name():
            return path_match.group('extended_path').replace('/', '.') if path_match.group('extended_path') else ''

        def get_function_name():
            method = operation.method

            return method.lower()

        return '{}.{}{}'.format(get_controller_name(), get_path_name(), get_function_name())
