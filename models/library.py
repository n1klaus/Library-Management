#!/usr/bin/python3

""" Module for Library Class Definition """

from models.base_model import BaseModel, sa
from sqlalchemy import Column, Integer, Identity


class Library(BaseModel):
    """Library object"""
    __tablename__ = 'libraries'
    library_id = Column(Integer,
                        Identity(
                            always=True,
                            start=1,
                            increment=1,
                            nomaxvalue=True),
                        primary_key=True)

    def __init__(self, *args, **kwargs):
        """Instantiates new library instances"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
