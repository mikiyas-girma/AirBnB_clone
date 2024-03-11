#!/usr/bin/python3

"""so that it can be considered as package"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
"""file storage instance for all models
"""
storage.reload()
