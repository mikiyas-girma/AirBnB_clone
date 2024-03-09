#!/usr/bin/python3

from datetime import datetime
import uuid


class BaseModel:

    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.id = uuid.uuid4().hex

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                self.__dict__.__setitem__(key, value.isoformat())
        self.__dict__.__setitem__('__class__', self.__class__.__name__)
        return self.__dict__

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
