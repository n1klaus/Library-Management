#!/usr/bin/python3

""" Module for User Class Definition """

from models.base_model import BaseModel, sa
from sqlalchemy import Column, String, ForeignKey, Integer, Identity
from sqlalchemy.orm import validates
import re


class User(BaseModel):
    """User object"""
    __tablename__ = "users"
    user_id = Column(Integer,
                     Identity(
                         always=True,
                         start=1,
                         increment=1,
                         nomaxvalue=True),
                     primary_key=True)
    first_name = Column(String(60))
    last_name = Column(String(60))
    email = Column(String(60), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    account_id = Column(Integer,
                        ForeignKey('accounts.account_id', onupdate='cascade', ondelete='cascade'))

    @validates('email')
    def validate_email(self, key, address):
        """Validate that the email is valid """
        if re.fullmatch(
            r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}', address)\
                is None:
            raise ValueError("{0} is an invalid email".format(address))
        return address

    def __init__(self, *args, **kwargs):
        """Instantiates new user instances"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    # TODO - login

    # TODO - logout

    # TODO - reset password
