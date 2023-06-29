#!/usr/bin/python3

""" Module for Librarian Class Definition """

from models.base_model import sa
from models.user import User
from sqlalchemy import Column, Integer, Identity, ForeignKey


class Librarian(User):
    """Librarian object"""
    __tablename__ = 'librarians'
    librarian_id = Column(Integer,
                          Identity(
                              always=True,
                              start=1,
                              increment=1,
                              nomaxvalue=True),
                          primary_key=True)
    user_id = Column(
        Integer,
        ForeignKey(
            'users.user_id',
            onupdate='cascade',
            ondelete='cascade'))
    book_rents_authorized = sa.relationship(
        'Book', backref='librarian', lazy=True)

    def __init__(self, *args, **kwargs):
        """Instantiates new librarian instances"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
