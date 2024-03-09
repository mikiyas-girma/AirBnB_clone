#!/usr/bin/python3

"""unit tests for base model"""

import unittest
from models.base_model import BaseModel
import datetime


class TestBase(unittest.TestCase):
    """testing the base model class"""

    def setUp(self):
        self.model = BaseModel()
        self.model.name = "JIT"

    def TearDown(self):
        """
            deleting instance.
        """
        del self.model

    def test_id_type(self):
        """check id type is string"""
        self.assertEqual("<class 'str'>", str(type(self.model.id)))

    def test_unique_id(self):
        """ check for each model unique id should be there"""
        self.new_model = BaseModel()
        self.assertNotEqual(self.model.id, self.new_model.id)

    def test_name(self):
        """check attribute can be added"""
        self.assertEqual("JIT", self.model.name)

    def test_first_equal(self):
        """at first created_at and updated_at time is equal"""
        self.assertEqual(self.model.updated_at.date,
                         self.model.created_at.date)

    def test_after_update(self):
        """check after updation date will not be the same"""
        old_update = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at.date, old_update)

    def test_diff_instance(self):
        """test that two model are not the same instance"""
        dict_model = self.model.to_dict()
        new_model = BaseModel(dict_model)
        self.assertNotEqual(self.model, new_model)

    def test_date_type(self):
        """test both created_at and update_at type are datetime"""
        dict_model = self.model.to_dict()
        new_model = BaseModel(dict_model)
        self.assertTrue(isinstance(new_model.created_at, datetime.datetime))
        self.assertTrue(isinstance(new_model.updated_at, datetime.datetime))

    def test_dict_class(self):
        """check the __class__ key exists in dict """
        self.assertEqual('BaseModel', (self.model.to_dict())["__class__"])

    def test_str_representation(self):
        """test the custom string representation of BaseModel instance"""
        cls_name = self.model.__class__.__name__
        exp_str = f"[{cls_name}] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), exp_str)

    def test_to_dict_return_type(self):
        """check the return type of to_dict method"""
        dict_model = self.model.to_dict()
        self.assertEqual("<class 'dict'>", str(type(dict_model)))
