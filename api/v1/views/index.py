#!/usr/bin/python3

from flask import render_template
from api.v1.views import app_views


@app_views.route('/', methods=['GET'])
@app_views.route('/index', methods=['GET'])
def home():
    """Returns home page"""
    return render_template('home.html')


@app_views.route('/help', methods=['GET'], strict_slashes=False)
def help():
    """Returns help page"""
    return render_template('help.html')


@app_views.route('/settings', methods=['GET'], strict_slashes=False)
def settings():
    """Returns settings page"""
    return render_template('settings.html')
