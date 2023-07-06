#!/usr/bin/python3

""" Module for Library Class Definition """

from models.base_model import BaseModel, sa


class Library(BaseModel):
    """Library object"""
    __tablename__ = 'libraries'
    library_id = sa.Column(sa.Integer, primary_key=True)

    def __init__(self, *args, **kwargs):
        """Instantiates new library instances"""
        self.library_id = None
        super().__init__(*args, **kwargs)
