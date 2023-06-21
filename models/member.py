#!/usr/bin/python3

""" Module for Member Class Definition """

from models.base_model import sa
from models.user import User
from sqlalchemy import Column, Integer, Identity


class Member(User):
    """Member object"""
    __tablename__ = 'members'
    member_id = Column(Integer,
                       Identity(
                           always=True,
                           start=1,
                           increment=1,
                           nomaxvalue=True),
                       primary_key=True)
    books_rented = sa.relationship('Book', backref='member', lazy=True)

    def __init__(self):
        """Instantiates new member instances"""
        pass

    # TODO - update member details

    # TODO - rent book

    # TODO - return rented book

    # TODO - pay book fee

    # TODO - delete member
