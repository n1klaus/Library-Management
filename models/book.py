#!/usr/bin/python3

""" Module for Book Class Definition """

from models.base_model import BaseModel, sa
from sqlalchemy import Column, Numeric, String, Integer, Identity, ForeignKey, DateTime


class Book(BaseModel):
    """Book object"""
    __tablename__ = "books"
    book_id = Column(Integer,
                     Identity(
                         always=True,
                         start=1,
                         increment=1,
                         nomaxvalue=True),
                     primary_key=True)
    book_title = Column(String(256), nullable=False)
    book_author = Column(String(256), nullable=False)
    book_isbn = Column(Integer, nullable=False, unique=True)
    book_fee = Column(Numeric(scale=2))
    book_rent_start_date = Column(DateTime)
    book_rent_end_date = Column(DateTime)
    # book_rented_to = Column(Integer,
    #                         ForeignKey('members.member_id', onupdate='cascade', ondelete='cascade'))
    # book_rented_by = Column(Integer,
    #                         ForeignKey('librarians.librarian_id', onupdate='cascade', ondelete='cascade'))
    # book_category = Column(Integer,
    #                        ForeignKey('book_categories.book_category_id', onupdate='cascade', ondelete='cascade'))

    def __init__(self, *args, **kwargs):
        """Instantiates new book instances"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    # TODO - replace book

    # TODO - update book details

    # TODO - delete book

    # TODO - update book charge fee

    # TODO - update book availability

    # TODO - update book condition
