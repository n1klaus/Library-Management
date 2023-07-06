#!/usr/bin/python3

""" Module for Book Category Class Definition """

from models.base_model import BaseModel, sa


class BookCategory(BaseModel):
    """Book object"""
    __tablename__ = 'book_categories'
    book_category_id = sa.Column(sa.Integer, primary_key=True)
    book_category_name = sa.Column(sa.String(60))
    listed_books = sa.relationship(
        'Book', backref='single_book_category', lazy=True)

    def __init__(self, *args, **kwargs):
        """Instantiates new book category instances"""
        self.book_category_id = None
        super().__init__(*args, **kwargs)
