#!/usr/bin/python3

"""module that contain tests for State"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def test_state_name(self):
        """Test the name attribute of the State class"""
        state = State()
        self.assertEqual(state.name, '')

    def test_state_name_assignment(self):
        """Test assigning a value to the name attribute of the State class"""
        state = State()
        state.name = 'California'
        self.assertEqual(state.name, 'California')

    def test_state_name_type(self):
        """Test the type of the name attribute of the State class"""
        state = State()
        self.assertIsInstance(state.name, str)


if __name__ == '__main__':
    unittest.main()
