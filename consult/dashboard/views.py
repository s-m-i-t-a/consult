# -*- coding: utf-8 -*-

from flask import Blueprint, render_template


dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/', endpoint='dashboard', methods=['GET'])
def index():
    render_template('dashboard/index.html')
