#!/usr/bin/python3

""" Module for Librarian Class Definition """

from models.base_model import sa
from models.user import User


class Librarian(User):
    """Librarian object"""
    __tablename__ = 'librarians'
    librarian_id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(
        sa.Integer,
        sa.ForeignKey(
            'users.user_id',
            onupdate='CASCADE',
            ondelete='CASCADE'))
    book_rents_authorized = sa.relationship(
        'Book', backref='librarian', lazy=True)

    def __init__(self, *args, **kwargs):
        """Instantiates new librarian instances"""
        self.librarian_id = None
        super().__init__(*args, **kwargs)
