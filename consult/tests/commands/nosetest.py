# -*- coding: utf-8 -*-

from flask.ext.script import Command, Option, Group


class Nosetest(Command):
    """
    Run unittests.
    """

    def get_options(self):
        options = []

        return options

    def run(self):
        # TODO: Vytahnout volby pro nastaveni behu testu
        from nose import run_exit
        run_exit(argv=['nosetests',
                       '-i',
                       '^(it|ensure|must|should|deve|specs?|examples?)',
                       '-i',
                       '(specs?|examples?|exemplos?)(.py)?$',
                       '--with-spec',
                       '--spec-color'])
