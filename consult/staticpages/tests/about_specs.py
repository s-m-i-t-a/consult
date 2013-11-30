# -*- coding: utf-8 -*-
import httplib

from staticpages.views import AboutView

ABOUT_PAGE_URL = u'/o-nas/'


class SpecAboutView(object):
    def should_about_page_url_resolves_to_about_page_view(self, app):
        urls = app.url_map.bind('localhost').match(ABOUT_PAGE_URL)
        view = urls[0]
        f = app.view_functions[view]

        assert f.view_class is AboutView

    def should_GET_request_return_status_ok(self, client):
        response = client.get(ABOUT_PAGE_URL)
        assert response.status_code == httplib.OK
