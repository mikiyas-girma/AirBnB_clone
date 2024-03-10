#!/usr/bin/python3
"""a module containing a base model for all objects"""

from datetime import datetime
import uuid


class BaseModel:
    """illustrates a base class """
    def __init__(self, *args, **kwargs):
        """initializes an instance of a BaseModel class"""

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ('created_at', 'updated_at'):
                        self.__setattr__(key, datetime.fromisoformat(value))
                    else:
                        self.__setattr__(key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.id = str(uuid.uuid4())

    def save(self):
        """updates the time an instance is last update"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary consisting of all key and values
            contained in BaseModel instance along with class name
        """
        dic = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dic[key] = value.isoformat()
            else:
                dic[key] = value
            dic['__class__'] = self.__class__.__name__
        return dic

    def __str__(self):
        """returns a custom string representation of BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
