#!/usr/bin/python3

""" Module for Book Class Model Definition """

from models.base_model import BaseModel, sa
from datetime import datetime, timedelta


class Book(BaseModel):
    """Book object"""
    __tablename__ = "books"
    book_id = sa.Column(sa.Integer, primary_key=True)
    book_title = sa.Column(sa.String(256), nullable=False)
    book_author = sa.Column(sa.String(256), nullable=False)
    book_isbn = sa.Column(sa.Integer, nullable=False, unique=True)
    book_fee = sa.Column(sa.Numeric(scale=2))
    book_rent_start_date = sa.Column(sa.DateTime)
    book_rent_end_date = sa.Column(sa.DateTime)
    book_is_rented_to = sa.Column(sa.Integer,
                                  sa.ForeignKey('members.member_id',
                                                onupdate='NO ACTION',
                                                ondelete='SET NULL'))
    book_rent_authorized_by = sa.Column(sa.Integer,
                                        sa.ForeignKey('librarians.librarian_id',
                                                      onupdate='NO ACTION',
                                                      ondelete='SET NULL'))
    book_category = sa.Column(sa.Integer,
                              sa.ForeignKey('book_categories.book_category_id',
                                            onupdate='NO ACTION',
                                            ondelete='SET NULL'))
    book_condition = sa.Column(
        sa.Enum(
            "Perfect",
            "Fair",
            "Poor",
            "NotRated",
            "NotRentable"),
        default="Perfect")
    book_rent_status = sa.Column(
        sa.Enum(
            "Available",
            "Rented"),
        default="Available")
    book_language = sa.Column(sa.String(30), nullable=True)

    def __init__(self, *args, **kwargs):
        """Instantiates new book instances"""
        self.book_id = None
        super().__init__(*args, **kwargs)

    def issue_book_to(self, member_id: int, librarian_id: int, duration: int):
        """Issues book to given member_id authorized by the librarian"""
        self.book_is_rented_to = member_id
        self.book_rent_authorized_by = librarian_id
        self.book_rent_status = 'Rented'
        self.book_rent_start_date = datetime.now()
        self.book_rent_end_date = self.book_rent_start_date + \
            timedelta.days(duration)
        self.save()

    def return_book_from(self, member_id: int, librarian_id: int):
        """Returns book from given member_id authorized by the librarian"""
        self.book_is_rented_to = None
        self.book_rent_authorized_by = librarian_id
        self.book_rent_status = 'Available'
        self.book_rent_start_date = None
        self.book_rent_end_date = None
        self.save()
