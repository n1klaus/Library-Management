#!/usr/bin/python3

""" Module for Book Category Class Definition """

from models.base_model import BaseModel
from sqlalchemy import Column, Identity, Integer, String


class BookCategory(BaseModel):
    """Book object"""
    __tablename__ = 'book_categories'
    book_category_id = Column(Integer,
                              Identity(
                                  always=True,
                                  start=1,
                                  increment=1,
                                  nomaxvalue=True),
                              primary_key=True)
    book_category_name = Column(String(60))

    def __init__(self, *args, **kwargs):
        """Instantiates new book category instances"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    # TODO - update book category details

    # TODO - delete book category
