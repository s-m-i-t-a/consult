# -*- coding: utf-8 -*-
'''
Settings for consult project.

'''

import os

from unipath import Path

from config.utils import get_dtb_config

BASE_DIR = Path(__file__).ancestor(2)


DEBUG = False

TESTING = False


SECRET_KEY = os.environ['SECRET_KEY']


MONGODB_SETTINGS = get_dtb_config(os.environ['DATABASE_URL'])
