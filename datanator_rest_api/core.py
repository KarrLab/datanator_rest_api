""" API Server
Provides an automatic implementation of the rest api using the connexion library
:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
:Date: 2019-08-19
:Copyright: 2019, Karr Lab
:License: MIT
"""
import connexion
from datanator_rest_api.server import AutoResolver
import re
from flask_cors import CORS


def createApp(apiName="DatanatorAPI.yaml", entryModule="datanator_rest_api.routes", specification_dir="./spec", resolver=AutoResolver, validate_responses=False):
    app = connexion.App(__name__, specification_dir=specification_dir)
    app.add_api(apiName, resolver=resolver(entryModule),

                validate_responses=validate_responses, strict_validation=True)
    CORS(app)
    return app


if __name__ == "__main__": # pragma: no cover

    app = createApp()
    app.run(port=8080, debug=True)
