#!/usr/bin/python3

from flask import request, jsonify, Response
from models.member import Member
from models.account import Account
from api.v1.views import app_views


@app_views.route('/members', methods=['GET'], strict_slashes=False)
def get_all_members():
    """Returns all members"""
    members = [member.to_dict() for member in Member.query.all() if member]
    return jsonify(members)


@app_views.route('/members', methods=['POST'], strict_slashes=False)
def add_member():
    """Returns newly created member information"""
    member: Member = Member(**request.form.to_dict())
    member.save()
    return Response(status=201)


@app_views.route('/members/<int:member_id>',
                 methods=['GET'], strict_slashes=False)
def get_single_member(member_id: int):
    """Returns member with given id"""
    member = Member.query.get_or_404(member_id, 'Member not found!')
    return jsonify(member.to_dict())


@app_views.route('/members/<int:member_id>',
                 methods=['PUT'], strict_slashes=False)
def update_member(member_id: int):
    """Returns updated member information updated with the new details"""
    member = Member.query.get_or_404(member_id, 'Member not found!')
    member.update(**request.form.to_dict())
    return jsonify(member.to_dict())


@app_views.route('/members/{member_id:int}',
                 methods=['DELETE'], strict_slashes=False)
def delete_member(member_id: int):
    """Deletes member"""
    member = Member.query.get_or_404(member_id, 'Member not found!')
    member.delete()
    return Response(status=204)


@app_views.route('/members/search', methods=['GET'], strict_slashes=False)
def search_members():
    """Returns members matching with the given search query"""
    members = [member.to_dict() for member in
               Member.query.filter_by(**request.args.to_dict()).all()
               if member]
    return jsonify(members)


@app_views.route('/members/<int:member_id>/account/<int:account_id>',
                 methods=['GET'], strict_slashes=False)
def get_member_account(member_id: int, account_id: int):
    """Returns members account information"""
    member = Member.query.get_or_404(member_id, 'Member not found!')
    account: Account = Account.query.get_or_404({'member_id': member_id,
                                                 'account_id': account_id},
                                                'Account not found!')
    return jsonify(account.to_dict())
