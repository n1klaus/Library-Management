#!/usr/bin/python3

""" Module for Account Class Definition """

from models.base_model import BaseModel, sa


class Account(BaseModel):
    """Account object"""
    __tablename__ = "accounts"
    account_id = sa.Column(sa.Integer, primary_key=True)
    account_balance = sa.Column(sa.Numeric(scale=2))
    account_status = sa.Column(
        sa.Enum(
            "Available",
            "Pending payment",
            "Locked",
            "Suspended"),
        default="Available")

    def __init__(self, *args, **kwargs):
        """Instantiates new account instances"""
        self.account_id = None
        super().__init__(*args, **kwargs)

    def deduct_book_fee(self, fee: float):
        """Charges the member with the book fee to authorize payment for book rent"""
        if self.account_status == 'Available':
            self.account_balance -= fee
            if self.account_balance <= -500:
                raise Exception(
                    'Cannot have outstanding debt of more than KSH.500')
            self.save()
