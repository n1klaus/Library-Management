#!/usr/bin/python3

""" Module for Librarian Class Definition """

from models.user import User
from sqlalchemy import Column, Integer, Identity


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

    def __init__(self):
        """Instantiates new librarian instances"""
        pass

    # TODO - issue book

    # TODO - return book

    # TODO - charge book fee

    # TODO - update member status

    # TODO - update book status
