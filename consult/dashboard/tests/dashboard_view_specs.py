# -*- coding: utf- -*-
import httplib

from dashboard.views import DashboardView

DASHBOARD_URL = u'/dashboard/'


class SpecHomeView(object):
    def should_dashboard_url_resolves_to_dashboard_view(self, app):
        urls = app.url_map.bind('localhost').match(DASHBOARD_URL)
        view = urls[0]
        f = app.view_functions[view]

        assert f.view_class is DashboardView

    def should_GET_request_return_status_ok(self, client):
        response = client.get(DASHBOARD_URL)
        assert response.status_code == httplib.OK
