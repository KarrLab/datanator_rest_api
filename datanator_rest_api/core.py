""" Server.py
Provides an automatic implementation of the rest api using the connexion library
:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
:Date: 2019-08-19
:Copyright: 2019, Karr Lab
:License: MIT
"""
import connexion
from connexion.resolver import RestyResolver
import datanator_rest_api.server.metabolites

app = connexion.App(__name__, specification_dir='spec/')
app.add_api('DatanatorAPI.yaml', resolver=RestyResolver(
    "server"), validate_responses=True)
app.run(port=8080)
