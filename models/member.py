#!/usr/bin/python3

""" Module for Member Class Definition """

from models.base_model import sa
from models.user import User


class Member(User):
    """Member object"""
    __tablename__ = 'members'
    member_id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(
        sa.Integer,
        sa.ForeignKey(
            'users.user_id',
            onupdate='CASCADE',
            ondelete='CASCADE'))
    books_rented = sa.relationship('Book', backref='member', lazy=True)

    def __init__(self, *args, **kwargs):
        """Instantiates new member instances"""
        self.member_id = None
        super().__init__(*args, **kwargs)

    def charge_book_fee(self, fee: float):
        """Charges the member with the book fee to authorize payment for book rent"""
        account = sa.Query('Account').get_or_404(account_id=self.account_id)
        account.deduct_book_fee(fee)
        self.save()
