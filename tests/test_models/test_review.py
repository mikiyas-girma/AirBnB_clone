#!/usr/bin/python3

"""modules contains tests for Review"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def test_instance_attributes(self):
        """
        Test that Review instance has the expected attributes
        """

        review = Review()
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

    def test_instance_attributes_with_values(self):
        """
        Test that Review instance attributes can be set with values
        """

        review = Review()
        review.place_id = '123'
        review.user_id = '456'
        review.text = 'Great place!'
        self.assertEqual(review.place_id, '123')
        self.assertEqual(review.user_id, '456')
        self.assertEqual(review.text, 'Great place!')

    def test_instance_attributes_edge_cases(self):
        """
        Test edge cases for Review instance attributes
        """

        review = Review()
        review.place_id = ''
        review.user_id = ''
        review.text = ''
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

        review.place_id = 'a' * 1000
        review.user_id = 'b' * 1000
        review.text = 'c' * 1000
        self.assertEqual(review.place_id, 'a' * 1000)
        self.assertEqual(review.user_id, 'b' * 1000)
        self.assertEqual(review.text, 'c' * 1000)


if __name__ == '__main__':
    unittest.main()
