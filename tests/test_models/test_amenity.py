#!/usr/bin/python3
"""module contains class for unittesting"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test case class for testing the Amenity class.
    """

    def setUp(self):
        """
        Set up the test fixture. This method is called before each test method.
        """
        self.model = Amenity()

    def test_name_initial_value(self):
        """
        Test that the initial value of the 'name' attribute is an empty string.
        """
        self.assertEqual(self.model.name, '')

    def test_name_assignment(self):
        """
        Test that the 'name' attribute can be assigned a value correctly.
        """
        self.model.name = 'Swimming Pool'
        self.assertEqual(self.model.name, 'Swimming Pool')

    def test_name_type(self):
        """
        Test that the 'name' attribute is of type str.
        """
        self.assertIsInstance(self.model.name, str)


if __name__ == '__main__':
    unittest.main()
