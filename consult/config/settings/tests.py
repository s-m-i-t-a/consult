# -*- coding: utf-8 -*-

from config.settings.base import *


TESTING = True

MONGODB_SETTINGS = get_dtb_config("mongodb://localhost/consult_tests")
