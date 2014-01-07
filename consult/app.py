# -*- coding: utf-8 -*-

import os

from consult import create_app


app = create_app(os.getenv('APP_CONFIGURATION', 'Production'))


if __name__ == '__main__':
    app.run()
