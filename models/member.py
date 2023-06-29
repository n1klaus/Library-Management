#!/usr/bin/python3

""" Module for Member Class Definition """

from models.base_model import sa
from models.user import User
from sqlalchemy import Column, Integer, Identity, ForeignKey


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
    user_id = Column(
        Integer,
        ForeignKey(
            'users.user_id',
            onupdate='cascade',
            ondelete='cascade'))
    books_rented = sa.relationship('Book', backref='member', lazy=True)

    def __init__(self, *args, **kwargs):
        """Instantiates new member instances"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def charge_book_fee(self, fee: float):
        """Charges the member with the book fee to authorize payment for book rent"""
        account = sa.Query('Account').get_or_404(account_id=self.account_id)
        account.deduct_book_fee(fee)
        self.save()
