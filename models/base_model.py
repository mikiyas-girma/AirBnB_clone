#!/usr/bin/python3

import datetime
import uuid


class BaseModel:

    def __init__(self):
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        self.id = uuid.uuid4().hex

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        a = self.__dict__
        return a


b = BaseModel()
print(b)
