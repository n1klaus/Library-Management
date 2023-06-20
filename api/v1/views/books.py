#!/usr/bin/python3

from flask import render_template, jsonify
from models.book import Book
from api.v1.views import app_views


@app_views.route('/books', methods=['GET'], strict_slashes=False)
def books():
    """Returns books page"""
    b = Book()
    return jsonify(str(b))
