#!/usr/bin/python3

""" Module for Book Class Model Definition """

from models.base_model import BaseModel, sa
from sqlalchemy import Column, Numeric, String, Integer, Identity, ForeignKey, DateTime, Enum
from datetime import datetime, timedelta


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
    book_fee = Column(Numeric(scale=2), nullable=False)
    book_rent_start_date = Column(DateTime)
    book_rent_end_date = Column(DateTime)
    book_is_rented_to = Column(Integer,
                               ForeignKey('members.member_id', onupdate='cascade', ondelete='cascade'))
    book_rent_authorized_by = Column(Integer,
                                     ForeignKey('librarians.librarian_id', onupdate='cascade', ondelete='cascade'))
    book_category = Column(Integer,
                           ForeignKey('book_categories.book_category_id', onupdate='cascade', ondelete='cascade'))
    book_condition = Column(
        Enum(
            "Perfect",
            "Fair",
            "Poor",
            "NotRated",
            "NotRentable"),
        default="Perfect")
    book_rent_status = Column(
        Enum(
            "Available",
            "Rented"),
        default="Available")

    def __init__(self, *args, **kwargs):
        """Instantiates new book instances"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

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
