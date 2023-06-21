#!/usr/bin/python3

""" Module for User Class Definition """

from models.base_model import BaseModel, sa
from sqlalchemy import Column, String, ForeignKey, Integer, Identity


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
    first_name = Column(String(60), nullable=True)
    last_name = Column(String(60), nullable=True)
    email = Column(String(60), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    account_id = Column(Integer,
                        ForeignKey('accounts.account_id', onupdate='cascade', ondelete='cascade'))

    def __init__(self, *args, **kwargs):
        """Instantiates new user instances"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    # TODO - update user settings

    # TODO delete user
