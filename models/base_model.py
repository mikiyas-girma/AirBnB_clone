#!/usr/bin/python3

from datetime import datetime
import uuid


class BaseModel:

    def __init__(self):
        self.id = uuid.uuid4().hex
        self.created_at = datetime.datetime.now
        self.updated_at = self.created_at
