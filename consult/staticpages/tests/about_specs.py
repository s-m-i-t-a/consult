# -*- coding: utf-8 -*-
import httplib

from should_dsl import should

from tests.base import Spec

from staticpages.views import AboutView

ABOUT_PAGE_URL = u'/o-nas/'


class AboutViewSpec(Spec):
    def should_about_page_url_resolves_to_about_page_view(self):
        urls = self.app.url_map.bind('localhost').match(ABOUT_PAGE_URL)
        view = urls[0]
        f = self.app.view_functions[view]

        f.view_class | should | be(AboutView)

    def should_GET_request_return_status_ok(self):
        response = self.client.get(ABOUT_PAGE_URL)
        response.status_code | should | equal_to(httplib.OK)
