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

    def test_save_method(self):
        """
            Tests the save method of the FileStorage class.
            > Create some test objects
            > Add the test objects to the storage
            > Save the storage to a file
            > Read the contents of the file
            >Check if the objects are correctly encoded and saved
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()

        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)

        self.storage.save()

        with open('obj.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        self.assertIn(obj1.__class__.__name__ + "." + obj1.id, json_data)
        self.assertIn(obj2.__class__.__name__ + "." + obj2.id, json_data)
        self.assertIn(obj3.__class__.__name__ + "." + obj3.id, json_data)
        self.assertEqual(json_data[obj1.__class__.__name__ +
                                   "." + obj1.id], obj1.to_dict())
        self.assertEqual(json_data[obj2.__class__.__name__ +
                                   "." + obj2.id], obj2.to_dict())
        self.assertEqual(json_data[obj3.__class__.__name__
                                   + "." + obj3.id], obj3.to_dict())
