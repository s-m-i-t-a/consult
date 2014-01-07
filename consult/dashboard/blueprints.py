# -*- coding: utf-8 -*-

from flask import Blueprint

from .views import DashboardView


dashboard = Blueprint('dashboard', __name__, template_folder='templates')


dashboard.add_url_rule('/dashboard/', view_func=DashboardView.as_view('dashboard'))
