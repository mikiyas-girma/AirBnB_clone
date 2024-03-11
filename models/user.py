#!/usr/bin/python3
"""modules that contain user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """represents a user having attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
