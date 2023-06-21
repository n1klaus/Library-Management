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
    account_total = Column(Numeric(scale=2))
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

    # TODO - update account settings

    # TODO delete account
