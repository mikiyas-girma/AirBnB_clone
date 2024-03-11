#!/usr/bin/python3

"""module containing test for User"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def test_user_attributes(self):
        """
        Test that User class has the correct attributes
        """

        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_user_attribute_types(self):
        """
        Test that User class attributes have the correct types
        """

        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_user_attribute_defaults(self):
        """
        Test that User class attributes have the correct default values
        """

        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')


if __name__ == '__main__':
    unittest.main()
