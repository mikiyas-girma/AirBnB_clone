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

    def test_name(self):
        """check attribute can be added"""
        self.assertEqual("JIT", self.model.name)
