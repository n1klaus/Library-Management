#!/usr/bin/python3

from flask import request, render_template, jsonify, redirect
from models.member import Member
from models.account import Account
from api.v1.views import app_views


@app_views.route('/members', methods=['GET'], strict_slashes=False)
def get_all_members():
    """Returns all members"""
    members = Member.query.all()
    return jsonify(members)


@app_views.route('/members', methods=['POST'], strict_slashes=False)
def add_member():
    """Returns newly created member information"""
    member: Member = Member(request.form)
    member.save()
    return jsonify(member)


@app_views.route('/members/{member_id:int}',
                 methods=['GET'], strict_slashes=False)
def get_single_member(member_id: int):
    """Returns member with given id"""
    member = Member.query.filter_by(member_id=member_id).one()
    return jsonify(member)


@app_views.route('/members/{member_id:int}',
                 methods=['PUT'], strict_slashes=False)
def update_member(member_id: int):
    """Returns updated member information updated with the new details"""
    member: Member = Member.query.filter_by(member_id=member_id).one()
    member.update(request.form)
    return jsonify(member)


@app_views.route('/members/{member_id:int}',
                 methods=['DELETE'], strict_slashes=False)
def delete_member(member_id: int):
    """Deletes member"""
    member: Member = Member.query.filter_by(member_id=member_id).one()
    member.delete()
    return redirect('/', 301)


@app_views.route('/members/search', methods=['GET'], strict_slashes=False)
def search_members():
    """Returns members matching with the given search query"""
    members = Member.query.filter_by(request.data).all()
    return jsonify(members)


@app_views.route('/members/account/{account_id:int}',
                 methods=['GET'], strict_slashes=False)
def get_member_account(account_id: int):
    """Returns members account information"""
    account: Account = Account.query.filter_by(account_id=account_id).one()
    return jsonify(account)
