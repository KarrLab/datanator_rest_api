""" API init

:Author: Bilal Shaikh <bilalshaikh42@gmail.com>
:Date: 2019-08-16
:Copyright: 2019, Karr Lab
:License: MIT
"""
import datanator_rest_api.spec.utils as utils
if __name__ == "__main__":

    utils.parseAPI('.', 'root.yaml', 'DatanatorAPI.yaml')
