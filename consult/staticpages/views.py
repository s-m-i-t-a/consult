# -*- coding: utf-8 -*-

from flask import Blueprint, render_template


staticpages = Blueprint('staticpages', __name__)


@staticpages.route('/', endpoint='home', methods=['GET'])
def index():
    return render_template('home.html')


@staticpages.route('/about', endpoint='about', methods=['GET'])
def about():
    return render_template('about.html')
