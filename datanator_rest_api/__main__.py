""" datanator_rest_api command line interface

:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
:Date: 2019-08-20
:Copyright: 2019, Karr Lab
:License: MIT
"""

import cement
import datanator_rest_api
import datanator_rest_api.core
import datanator_rest_api.spec
import datanator_rest_api.routes


class BaseController(cement.Controller):  # pragma: no cover
    """ Base controller for command line application """

    class Meta:
        label = 'base'
        description = "datanator_rest_api"
        arguments = [
            (['-v', '--version'], dict(action='version',
                                       version=datanator_rest_api.__version__)),
        ]

    @cement.ex(help='command_1 description')
    def cmd1(self):
        """ command_1 description """
        print('command_1 output')

    @cement.ex(help='command_2 description')
    def cmd2(self):
        """ command_2 description """
        print('command_2 output')

    @cement.ex(hide=True)
    def _default(self):
        self._parser.print_help()


class Command3WithArgumentsController(cement.Controller):  # pragma: no cover
    """ Command3 description """

    class Meta:
        label = 'command-3'
        description = 'Command3 description'
        stacked_on = 'base'
        stacked_type = 'nested'
        arguments = [
            (['arg_1'], dict(
                type=str, help='Description of arg_1')),
            (['arg_2'], dict(
                type=str, help='Description of arg_2')),
            (['--opt-arg-3'], dict(
                type=str, default='default value of opt-arg-1', help='Description of opt-arg-3')),
            (['--opt-arg-4'], dict(
                type=float, default=float('nan'), help='Description of opt-arg-4')),
        ]

    @cement.ex(hide=True)
    def _default(self):
        args = self.app.pargs
        args.arg_1
        args.arg_2
        args.opt_arg_3
        args.opt_arg_4


class Cli(cement.App):  # pragma: no cover
    """ Command line application """
    class Meta:
        label = 'datanator_rest_api'
        base_controller = 'base'
        handlers = [
            BaseController,
            Command3WithArgumentsController,
        ]


def main():  # pragma: no cover
    with Cli() as cli:
        cli.run()
