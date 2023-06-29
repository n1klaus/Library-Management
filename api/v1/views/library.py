#!/usr/bin/python3

from flask import render_template, jsonify, request, redirect
from models.library import Library
from api.v1.views import app_views


@app_views.route('/libraries/{library_id:int}',
                 methods=['GET'], strict_slashes=False)
def get_library_details(library_id: int):
    """Returns library information"""
    library: Library = Library.query(library_id=library_id).one()
    return jsonify(library)


@app_views.route('/libraries/{library_id:int}',
                 methods=['PUT'], strict_slashes=False)
def update_library(library_id: int):
    """Updates library information"""
    library: Library = Library.query(library_id=library_id).one()
    library.update(request.form)
    return jsonify(library)


@app_views.route('/libraries/{library_id:int}',
                 methods=['DELETE'], strict_slashes=False)
def delete_library(library_id: int):
    """Deletes the library"""
    library: Library = Library.query(library_id=library_id).one()
    library.delete()
    return redirect('home.html', 301)
