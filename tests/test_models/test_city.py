#!/usr/bin/python3
"""module for testing City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    This class contains unit tests for the City class.
    """

    def test_city_attributes(self):
        """
        Test case to check the default attributes of a City instance.
        """
        city = City()
        self.assertEqual(city.state_id, '')
        self.assertEqual(city.name, '')

    def test_city_attributes_with_values(self):
        """
        Test case to check the attributes of a City instance
        with specific values.
        """
        city = City(state_id='123', name='New York')
        self.assertEqual(city.state_id, '123')
        self.assertEqual(city.name, 'New York')


if __name__ == '__main__':
    unittest.main()
