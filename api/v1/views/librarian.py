#!/usr/bin/python3

from flask import request, render_template, jsonify, redirect
from models.librarian import Librarian
from api.v1.views import app_views


@app_views.route('/librarians', methods=['GET'], strict_slashes=False)
def get_all_librarians():
    """Returns all librarians registered in the library"""
    librarians = Librarian.query.all()
    return jsonify(librarians)


@app_views.route('/librarians', methods=['POST'], strict_slashes=False)
def add_librarian():
    """Returns newly created librarian information"""
    librarian: Librarian = Librarian(request.form)
    librarian.save()
    return jsonify(librarian)


@app_views.route('/librarians/{librarian_id: int}',
                 methods=['GET'], strict_slashes=False)
def get_single_librarian(librarian_id: int):
    """Returns librarian information from the given id"""
    librarian = Librarian.query.filter_by(librarian_id=librarian_id).one()
    return jsonify(librarian)


@app_views.route('/librarians/{librarian_id:int}',
                 methods=['PUT'], strict_slashes=False)
def update_librarian(librarian_id: int):
    """Returns updated librarian information after updating with new details"""
    librarian = Librarian.query.filter_by(librarian_id=librarian_id).one()
    librarian.update(request.form)
    return jsonify(librarian)


@app_views.route('/librarians/{librarian_id:int}',
                 methods=['DELETE'], strict_slashes=False)
def delete_librarian(librarian_id: int):
    """Deleted the librarian"""
    librarian = Librarian.query.filter_by(librarian_id=librarian_id).one()
    librarian.delete()
    return redirect('/', 301)


@app_views.route('/librarians/search', methods=['GET'], strict_slashes=False)
def search_librarians():
    """Returns librarians with the given search query"""
    librarians = Librarian.query(filter_by=request.data).all()
    return jsonify(librarians)
