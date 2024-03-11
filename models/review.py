#!/usr/bin/python3
"""module containing Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class representing Review instances"""
    place_id = ''
    user_id = ''
    text = ''
