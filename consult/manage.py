# -*- coding: utf-8 -*-

import os.path
import sys

from flask.ext.script import Manager, Server
from config.wsgi import app

from tests.commands.nosetest import Nosetest

manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runserver",
                    Server(use_debugger=True,
                           use_reloader=True,
                           host='0.0.0.0'))

manager.add_command('tests', Nosetest())


if __name__ == "__main__":
    manager.run()
