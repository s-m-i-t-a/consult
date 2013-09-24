# -*- coding: utf-8 -*-

from flask.ext.testing import TestCase

from app import app, db


class Spec(TestCase):
    def create_app(self):
        return app

    def before(self):
        pass

    def after(self):
        pass

    def setUp(self):
        self.before()

    def tearDown(self):
        self.after()

        # smazeme vsechny vytvorene kolekce
        dtb = db.connection[app.config['MONGODB_SETTINGS']['DB']]
        if (app.config['MONGODB_SETTINGS']['USER'] and
                app.config['MONGODB_SETTINGS']['PASSWORD']):
            dtb.authenticate(app.config['MONGODB_SETTINGS']['USER'],
                             app.config['MONGODB_SETTINGS']['PASSWORD'])

        for name in dtb.collection_names():
            if not name.startswith('system'):
                dtb.drop_collection(name)
