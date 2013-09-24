# -*- coding: utf-8 -*-

from flask import Blueprint

from .views import AboutView, HomeView


staticpages = Blueprint('staticpages', __name__, template_folder='templates')


staticpages.add_url_rule('/', view_func=HomeView.as_view('home'))
staticpages.add_url_rule('/o-nas/', view_func=AboutView.as_view('about'))
