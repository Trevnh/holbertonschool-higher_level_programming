#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer"""

    def test_empty_list(self):
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def test_ordered_list(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(max_integer(test_list), 10)

    def test_middle(self):
        test_list = [37, 63, 89, 36, 17]
        self.assertEqual(max_integer(test_list), 89)

    def test_start(self):
        test_list = [97, 5, 81, 29, 2]
        self.assertEqual(max_integer(test_list), 97)

    def test_end(self):
        test_list = [84, 43, 54, 56, 90]
        self.assertEqual(max_integer(test_list), 90)

    def test_one_negative(self):
        test_list = [32, 38, -53, 70, 36]
        self.assertEqual(max_integer(test_list), 70)

    def test_all_negative(self):
        test_list = [-26, -37, -77, -85, -49]
        self.assertEqual(max_integer(test_list), -26)

    def test_one_number(self):
        test_list = [50]
        self.assertEqual(max_integer(test_list), 50)

    def test_multiple(self):
        test_list = [1, 2, 5, 5, 3]
        self.assertEqual(max_integer(test_list), 5)