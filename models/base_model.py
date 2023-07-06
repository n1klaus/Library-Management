#!/usr/bin/python3

""" Module for Base Class Model Definition """

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


sa: SQLAlchemy = SQLAlchemy()


class BaseModel(sa.Model):
    """BaseModel object"""
    __abstract__ = True
    created_at = sa.Column(sa.DateTime, default=datetime.now())
    updated_at = sa.Column(
        sa.DateTime,
        default=datetime.now(),
        onupdate=datetime.now())
    status = sa.Column(
        sa.Enum(
            "Available",
            "NotAvailable"),
        default="Available")

    def __init__(self, *args, **kwargs):
        """Instantiates new base model instances"""
        if kwargs:
            for key, value in kwargs.items():
                if key not in self.__dict__:
                    setattr(self, key, value)

    def save(self):
        """Saves object to database"""
        sa.session.add(self)
        sa.session.commit()

    def delete(self):
        """Deletes object from database"""
        sa.session.delete(self)
        sa.session.commit()

    def update(self, **kwargs):
        """Update object details"""
        if kwargs:
            for key_attr, val_attr in kwargs.items():
                setattr(self, key_attr, val_attr)
            self.save()

    def to_dict(self) -> dict:
        """Returns dictionary representation of the object"""
        my_dict: dict = dict(sorted(self.__dict__.items()))
        if '_sa_instance_state' in my_dict:
            del my_dict['_sa_instance_state']
        if 'password' in my_dict:
            del my_dict['password']
        return my_dict

    def count(self):
        """Returns object count in database"""
        sa.session.count(self)

    def __repr__(self):
        """Returns the canonical representation of the object"""
        return f"{self.to_dict()}"
