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
import tempfile


class SpecUtils(object):
    @staticmethod
    def validateAPI(res_api: str):
        """Opens the API specification and validates against the open api schema

        Args:
            res_api (str): A string containing the resolved API definition
        Raises:
            OpenAPIValidationError: The provided specification is invalid
            ExtraParametersError: A required paramter has no corresponding properties description
            ParameterDuplicateError: A parameter has been included more than once in the definition
            UnresolvableParamaterError:
        """
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml') as t:
            t.write(res_api)
            with open(t.name, 'r') as spec_file:
                schema = yaml.safe_load(spec_file)
                validate_spec(schema)

    @staticmethod
    def parseAPI(api_dir: str = "./datanator_rest_api/spec/", src_file: str = "root.yaml"):
        """ Takes the root open api yaml file and resolves the embedded refrences for local and remote yaml files. 
            Generates a complete JSON specification of the API 

        Args:
            api_dir (str): The directory storing the api definition
            src_file (str): The name of the root api file
        Returns: 
            str : A string containing the parsed API
        """

        os.chdir(api_dir)

        with open(src_file) as api_src:
            ret = yaml.safe_load(api_src)
            resolver = OpenapiResolver(ret)
            resolver.resolve()
            res = resolver.dump()
        return res

    @staticmethod
    def writeAPI(res_api, dst_file):
        """ A simple wrapper for file writing. 
        Takes in a resolved api definition and writes it to a file. 

        Args:
            res_api (str): The API with refrences resolved
            dst_file (str): The path for the OpenAPI Specification file to write 
        """
        with open(dst_file, 'w') as api_dst:
            api_dst.write(res_api)

    @staticmethod
    def uploadAPI(api_file):
        pass


if __name__ == "__main__":
    res_api = SpecUtils.parseAPI(api_dir='.', src_file='root.yaml')
    try:
        SpecUtils.validateAPI(res_api)
    except Exception as e:
        print(e)
    else:
        with open("DatanatorAPI.yaml", 'w') as dst_file:
            dst_file.write(res_api)
