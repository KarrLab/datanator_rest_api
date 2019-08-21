""" Server.py
Provides an automatic implementation of the rest api using the connexion library
:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
:Date: 2019-08-19
:Copyright: 2019, Karr Lab
:License: MIT
"""
import connexion
from connexion.resolver import Resolver as Resolver
from connexion.resolver import RestyResolver
from connexion.mock import MockResolver
import re


class MyResolver(RestyResolver):

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
            x_router_controller = operation.router_controller

            name = self.default_module_name
            resource_name = path_match.group('resource_name')

            if x_router_controller:
                name = x_router_controller

            elif resource_name:
                resource_controller_name = resource_name.replace('-', '_')
                name += '.' + resource_controller_name

            return name

        def get_path_name():
            return path_match.group('extended_path').replace('/', '.') if path_match.group('extended_path') else ''

        def get_function_name():
            method = operation.method

            is_collection_endpoint = \
                method.lower() == 'get' \
                and path_match.group('resource_name') \
                and not path_match.group('extended_path')

            return self.collection_endpoint_name if is_collection_endpoint else method.lower()

        return '{}.{}{}'.format(get_controller_name(), get_path_name(), get_function_name())


if __name__ == "__main__":

    app = connexion.App(__name__, specification_dir='spec/')
    app.add_api('DatanatorAPI.yaml', resolver=MyResolver(
        "datanator_rest_api.routes"), validate_responses=False)
    app.run(port=8080, debug=True)
