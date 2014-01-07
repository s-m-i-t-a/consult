# -*- coding: utf-8 -*-


def register_blueprints(app):
    '''
    Place your blueprints import here.

    E.g.

    from intiny.catalog.blueprints import catalogs
    app.register_blueprint(catalogs)
    '''
    from flask_musers.blueprints import auth
    app.register_blueprint(auth)

    from staticpages.blueprints import staticpages
    app.register_blueprint(staticpages)

    from dashboard.blueprints import dashboard
    app.register_blueprint(dashboard)
