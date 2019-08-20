""" API init

:Author: Bilal Shaikh <bilalshaikh42@gmail.com>
:Date: 2019-08-16
:Copyright: 2019, Karr Lab
:License: MIT
"""
from .specUtils import specUtils
if __name__ == "__main__":

    specUtils.parseAPI('.', 'root.yaml', 'DatanatorAPI.yaml')
