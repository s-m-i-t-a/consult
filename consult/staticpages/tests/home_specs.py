# -*- coding: utf-8 -*-
import httplib

from should_dsl import should

from tests.base import Spec

from staticpages.views import HomeView

HOME_PAGE_URL = u'/'


class HomeViewSpec(Spec):
    def should_home_page_url_resolves_to_home_page_view(self):
        urls = self.app.url_map.bind('localhost').match(HOME_PAGE_URL)
        view = urls[0]
        f = self.app.view_functions[view]

        f.view_class | should | be(HomeView)

    def should_GET_request_return_status_ok(self):
        response = self.client.get(HOME_PAGE_URL)
        response.status_code | should | equal_to(httplib.OK)
