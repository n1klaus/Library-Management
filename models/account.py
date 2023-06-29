#!/usr/bin/python3

""" Module for Account Class Definition """

from models.base_model import BaseModel
from sqlalchemy import Column, Numeric, Enum, Integer, Identity


class Account(BaseModel):
    """Account object"""
    __tablename__ = "accounts"
    account_id = Column(Integer,
                        Identity(
                            always=True,
                            start=1,
                            increment=1,
                            nomaxvalue=True),
                        primary_key=True)
    account_balance = Column(Numeric(scale=2))
    account_status = Column(
        Enum(
            "Available",
            "Payment required",
            "Locked",
            "Suspended"),
        default="Available")

    def __init__(self, *args, **kwargs):
        """Instantiates new account instances"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def deduct_book_fee(self, fee: float):
        """Charges the member with the book fee to authorize payment for book rent"""
        if self.account_status == 'Available':
            self.account_balance -= fee
            if self.account_balance <= -500:
                raise Exception(
                    'Cannot have outstanding debt of more than KSH.500')
            self.save()
