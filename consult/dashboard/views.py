# -*- coding: utf-8 -*-

from flask_cbv.views.generic import View


class DashboardView(View):
    template = 'dashboard/index.html'
