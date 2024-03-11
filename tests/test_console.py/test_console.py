#!/usr/bin/python3
"""
Unit tests for console using context manager for capturing stdout
"""

import os
import sys
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """
    Unittest for the console model
    """

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()

    def last_write(self, nr=None):
        """Returns last n output lines"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(lambda c: c[0][0],
                           self.mock_stdout.write.call_args_list[-nr:]))

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_help(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help"))
            self.assertTrue(self.console.onecmd("help quit"))
        def test_help_specific_command(self):
        """Test help with specific command"""
        expected_output = """Help on EOF:

No further documentation available."""
        self.assert_stdout("help EOF", expected_output, "")

    def test_create_command(self):
        """Test create command"""
        expected_output = "Usage: create <class>\n"
        self.assert_stdout("create", expected_output, "")

    def test_create_command_with_class(self):
        """Test create command with class"""
        expected_output = ""
        self.assert_stdout("create BaseModel", expected_output, "")

    def test_show_command(self):
        """Test show command"""
        expected_output = "** class name missing **"
        self.assert_stdout("show", expected_output, "")

    def test_show_command_with_class(self):
        """Test show command with class"""
        expected_output = "** instance id missing **"
        self.assert_stdout("show BaseModel", expected_output, "")

    def test_destroy_command(self):
        """Test destroy command"""
        expected_output = "** class name missing **"
        self.assert_stdout("destroy", expected_output, "")

    def test_destroy_command_with_class(self):
        """Test destroy command with class"""
        expected_output = "** instance id missing **"
        self.assert_stdout("destroy BaseModel", expected_output, "")

    def test_all_command(self):
        """Test all command"""
        expected_output = "[[BaseModel] (1234) {'name': 'test'}]"
        with patch('sys.stdin', StringIO("all BaseModel")), \
             patch('sys.stdout', new=StringIO()) as mock_stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_all_command_with_invalid_class(self):
        """Test all command with invalid class"""
        expected_output = "** class doesn't exist **"
        self.assert_stdout("all InvalidClass", expected_output, "")

    def test_update_command(self):
        """Test update command"""
        expected_output = "** class name missing **"
        self.assert_stdout("update", expected_output, "")

    def test_update_command_with_class(self):
        """Test update command with class"""
        expected_output = "** instance id missing **"
        self.assert_stdout("update BaseModel", expected_output, "")

    def test_update_command_with_instance(self):
        """Test update command with instance"""
        expected_output = "** attribute name missing **"
        self.assert_stdout("update BaseModel.1234", expected_output, "")

    def test_update_command_with_instance_and_attribute(self):
        """Test update command with instance and attribute"""
        expected_output = "** value missing **"
        self.assert_stdout("update BaseModel.1234 name", expected_output, "")

if __name__ == '__main__':
    unittest.main()

