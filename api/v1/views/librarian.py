#!/usr/bin/python3

from flask import request, jsonify, Response
from models.librarian import Librarian
from api.v1.views import app_views


@app_views.route('/librarians', methods=['GET'], strict_slashes=False)
def get_all_librarians():
    """Returns all librarians registered in the library"""
    librarians = [librarian.to_dict()
                  for librarian in Librarian.query.all() if librarian]
    return jsonify(librarians)


@app_views.route('/librarians', methods=['POST'], strict_slashes=False)
def add_librarian():
    """Returns newly created librarian information"""
    librarian: Librarian = Librarian(**request.form.to_dict())
    librarian.save()
    return Response(status=201)


@app_views.route('/librarians/<int:librarian_id>',
                 methods=['GET'], strict_slashes=False)
def get_single_librarian(librarian_id: int):
    """Returns librarian information from the given id"""
    librarian = Librarian.query.get_or_404(
        librarian_id, 'Librarian not found!')
    return jsonify(librarian.to_dict())


@app_views.route('/librarians/<int:librarian_id>',
                 methods=['PUT'], strict_slashes=False)
def update_librarian(librarian_id: int):
    """Returns updated librarian information after updating with new details"""
    librarian = Librarian.query.get_or_404(
        librarian_id, 'Librarian not found!')
    librarian.update(**request.form.to_dict())
    return jsonify(librarian.to_dict())


@app_views.route('/librarians/<int:librarian_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_librarian(librarian_id: int):
    """Deletes the librarian"""
    librarian = Librarian.query.get_or_404(
        librarian_id, 'Librarian not found!')
    librarian.delete()
    return Response(status=204)


@app_views.route('/librarians/search', methods=['GET'], strict_slashes=False)
def search_librarians():
    """Returns librarians with the given search query"""
    librarians = [librarian.to_dict() for librarian in
                  Librarian.query.filter_by(**request.args.to_dict()).all()
                  if librarian]
    return jsonify(librarians)
