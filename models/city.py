#!/usr/bin/python3
"""module that contains city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """class representing city objects"""
    state_id = ''
    name = ''
