#!/usr/bin/python3

from flask import jsonify, request, Response
from models.library import Library
from api.v1.views import app_views


@app_views.route('/libraries/{library_id:int}',
                 methods=['GET'], strict_slashes=False)
def get_library_details(library_id: int):
    """Returns library information"""
    library: Library = Library.query.get_or_404(
        library_id, 'Library not found')
    return jsonify(library.to_dict())


@app_views.route('/libraries/{library_id:int}',
                 methods=['PUT'], strict_slashes=False)
def update_library(library_id: int):
    """Updates library information"""
    library: Library = Library.query.get_or_404(
        library_id, 'Library not found')
    library.update(request.form.to_dict())
    return jsonify(library.to_dict())


@app_views.route('/libraries/{library_id:int}',
                 methods=['DELETE'], strict_slashes=False)
def delete_library(library_id: int):
    """Deletes the library"""
    library: Library = Library.query(library_id=library_id).one()
    library.delete()
    return Response(status=204)
