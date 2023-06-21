#!/usr/bin/python3

""" Module for Base Class Definition """

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Identity, Enum, Integer, DateTime
from datetime import datetime

sa: SQLAlchemy = SQLAlchemy()


class BaseModel(sa.Model):
    """BaseModel object"""
    __abstract__ = True
    id = Column(Integer,
                Identity(
                    always=True,
                    start=1,
                    increment=1,
                    nomaxvalue=True),
                primary_key=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(
        DateTime,
        default=datetime.now(),
        onupdate=datetime.now())
    status = Column(
        Enum(
            "Available",
            "NotAvailable"),
        default="Available")

    def __init__(self, *args, **kwargs):
        """Instantiates new base model instances"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    # TODO - save object
    def save(self):
        """Saves object to database"""
        sa.session.add(self)
        sa.session.commit()

    # TODO - delete object
    def delete(self):
        """Deletes object from database"""
        sa.session.delete(self)
        sa.session.commit()

    # TODO - get dictionary object
    def to_dict(self) -> dict:
        """Returns dictionary representation of the object"""
        my_dict: dict = self.__dict__
        del my_dict['_sa_instance_state']
        return my_dict

    # TODO - get object count
    def count(self):
        """Returns object count in database"""
        sa.session.count(self)

    def __repr__(self):
        """Returns the canonical representation of the object"""
        return f"[{self.id}] => {self.to_dict()}"
