""" Datanator API Utils

:Author: Bilal Shaikh <bilalshaikh42@gmail.com>
:Date: 2019-08-16
:Copyright: 2019, Karr Lab
:License: MIT
"""
from openapi_resolver import OpenapiResolver
import yaml
import os


def parseAPI(api_dir: str, src_file: str, dst_file: str):
    """ Takes the root open api yaml file and resolves the embedded refrences for local and remote yaml files. 
        Generates a complete JSON specification of the API 

    Args:
        api_dir: The directory storing the api definition
        src_file: The name of the root api file
        dst_file: The name of the output file
    """
    os.chdir(api_dir)

    with open(src_file) as api_src, open(dst_file, 'w') as api_dst:
        ret = yaml.safe_load(api_src)
        resolver = OpenapiResolver(ret)
        resolver.resolve()
        api_dst.write(resolver.dump())


def validateAPI(api_file):
    pass


def uploadAPI(api_file):
    pass


if __name__ == "__main__":
    parseAPI('./spec', 'openapi.yaml', 'DatanatorAPI.yaml')
