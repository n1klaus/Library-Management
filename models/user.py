#!/usr/bin/python3

""" Module for User Class Definition """

from models.base_model import BaseModel, sa
from sqlalchemy.orm import validates
import re


class User(BaseModel):
    """User object"""
    __tablename__ = "users"
    user_id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(60))
    last_name = sa.Column(sa.String(60))
    email = sa.Column(sa.String(60), nullable=False, unique=True)
    password = sa.Column(sa.String(60), nullable=False)
    account_id = sa.Column(sa.Integer,
                           sa.ForeignKey('accounts.account_id', onupdate='CASCADE', ondelete='SET NULL'))

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
        self.user_id = None
        super().__init__(*args, **kwargs)

    # TODO - login

    # TODO - logout

    # TODO - reset password
