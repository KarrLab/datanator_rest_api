""" Datanator API Utils

:Author: Bilal Shaikh <bilalshaikh42@gmail.com>
:Date: 2019-08-16
:Copyright: 2019, Karr Lab
:License: MIT
"""
from openapi_resolver import OpenapiResolver
import yaml
import os
import json
from openapi_spec_validator import openapi_v3_spec_validator, validate_spec


def validateAPI(api_file: str):
    """Opens the API specification and validates against the open api schema

    Args:
        api_file (str): The path to the file
    Raises:
        OpenAPIValidationError: The provided specification is invalid
        ExtraParametersError: A required paramter has no corresponding properties description
        ParameterDuplicateError: A parameter has been included more than once in the definition
        UnresolvableParamaterError:
    """
    with open(api_file, 'r') as schema_file:
        schema = yaml.safe_load(schema_file)
        validate_spec(schema)


def parseAPI(api_dir: str, src_file: str, dst_file: str):
    """ Takes the root open api yaml file and resolves the embedded refrences for local and remote yaml files. 
        Generates a complete JSON specification of the API 

    Args:
        api_dir (str): The directory storing the api definition
        src_file (str): The name of the root api file
        dst_file (str): The name of the output file
    """
    os.chdir(api_dir)
    with open(src_file) as api_src, open(dst_file, 'w') as api_dst:
        ret = yaml.safe_load(api_src)
        resolver = OpenapiResolver(ret)
        resolver.resolve()
        res = resolver.dump()
        api_dst.write(res)

    validateAPI(dst_file)


def uploadAPI(api_file):
    pass


if __name__ == "__main__":
    parseAPI('.', 'root.yaml', 'DatanatorAPI.yaml')
