""" Metabolites collection controller
This file defines the methods for the operations on the Metabolites collection.
The root class contains the HTTP methods for the /metabolites/ path
Any subpaths are contained in an internal class

:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
:Date: 2019-08-20
:Copyright: 2019, Karr Lab
:License: MIT
"""


def search():
    return ("test")


def put(body):
    return ("test")


def post():
    return ("test")


def get(inchikey):
    return("test")


class concentrations(object):
    def get():
        return ('concentrations test get')

    def search():
        return("Concentrationstest")
