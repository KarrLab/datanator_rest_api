""" API Server
Provides an automatic implementation of the rest api using the connexion library
:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
:Date: 2019-08-19
:Copyright: 2019, Karr Lab
:License: MIT
"""
import connexion
from datanator_rest_api.server import AutoResolver
from datanator_query_python.config import config
from pymongo.errors import OperationFailure
import re
from flask_cors import CORS
from swagger_ui_bundle import swagger_ui_3_path


def create_app(apiName="DatanatorAPI.yaml", entryModule="datanator_rest_api.routes", 
              specification_dir="./spec", resolver=AutoResolver, validate_responses=False,
              config_class=config.FlaskProfiler):
    option = {"swagger_path": swagger_ui_3_path, "swagger_url":"/"}
    app = connexion.App(
        __name__, specification_dir=specification_dir, options=option)
    app.add_api(apiName, resolver=resolver(entryModule),
                validate_responses=validate_responses, strict_validation=True)
    application = app.app
    application.config.from_object(config_class)
    application.config['flask_profiler'] = application.config['FLASKPROFILER']
    CORS(application)
    # try:
    #     profiler.init_app(application)
    # except OperationFailure:
    #     return app
    return app


if __name__ == "__main__":  # pragma: no cover

    create_app(config_class=config.FlaskProfiler).run(host='0.0.0.0', port=8080)

run = create_app(config_class=config.FlaskProfiler)
