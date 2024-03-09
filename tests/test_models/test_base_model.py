#!/usr/bin/python3

"""unit tests for base model"""

import unittest
from models.base_model import BaseModel
import sys
import datetime


class TestBase(unittest.TestCase):
    """testing the base model class"""

    def setUp(self):
        self.model = BaseModel()
        self.model.name = "JIT"

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
        self.assertEqual(self.model.updated_at.date,
                         self.model.created_at.date)

    def test_after_update(self):
        old_update = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at.date, old_update)
