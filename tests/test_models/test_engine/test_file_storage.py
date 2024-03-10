#!/usr/bin/python3

import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """test class for unittesting File storage engine"""
    def setUp(self):
        """prepares for test fixture"""
        self.storage = FileStorage()
        self.my_model = BaseModel()

    def tearDown(self):
        """cleaning up """
        try:
            os.remove('obj.json')
        except FileNotFoundError:
            pass

    def test_all(self):
        """returns all objects contae"""
        expected = self.storage._FileStorage__objects
        actual = self.storage.all()
        self.assertEqual(expected, actual)

    def test_new_method(self):
        '''
            Tests that the new method sets the right key and value pair
            in the FileStorage.__object attribute
        '''
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        self.assertTrue(key in self.storage._FileStorage__objects)
