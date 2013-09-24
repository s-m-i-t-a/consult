# -*- coding: utf-8 -*-

from flask_cbv.views.generic import View


class HomeView(View):
    template = 'home.html'


class AboutView(View):
    template = 'about.html'
