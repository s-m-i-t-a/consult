# -*- coding: utf-8 -*-
import httplib

from staticpages.views import HomeView

HOME_PAGE_URL = u'/'


class SpecHomeView(object):
    def should_home_page_url_resolves_to_home_page_view(self, app):
        urls = app.url_map.bind('localhost').match(HOME_PAGE_URL)
        view = urls[0]
        f = app.view_functions[view]

        assert f.view_class is HomeView

    def should_GET_request_return_status_ok(self, client):
        response = client.get(HOME_PAGE_URL)
        assert response.status_code == httplib.OK
