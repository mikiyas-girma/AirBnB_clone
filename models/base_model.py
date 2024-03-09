#!/usr/bin/python3
"""a module containing a base model for all objects"""

from datetime import datetime
import uuid


class BaseModel:
    """illustrates a base class """
    def __init__(self):
        """initializes an instance of a BaseModel class"""
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.id = uuid.uuid4().hex

    def save(self):
        """updates the time an instance is last update"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary consisting of all key and values
            contained in BaseModel instance along with class name
        """
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                self.__dict__.__setitem__(key, value.isoformat())
        self.__dict__.__setitem__('__class__', self.__class__.__name__)
        return self.__dict__

    def __str__(self):
        """returns a custom string representation of BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
