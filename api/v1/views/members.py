#!/usr/bin/python3

from flask import render_template
from api.v1.views import app_views


@app_views.route('/members', methods=['GET'], strict_slashes=False)
def members():
    """Returns members page"""
    return render_template('members.html')
