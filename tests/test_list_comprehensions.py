# -*- coding: utf-8 -*-

"""
Tests for list_comprehensions.
"""

import unittest
import types

from pyknowledge import list_comprehensions


class TestListComprehensions(unittest.TestCase):

    def test_divisible_by_three(self):
        """
        Test that the function returns a list of numbers divisible by three
        """
        number_list = range(1,20)
        returned = list_comprehensions.divisible_by_three(number_list)
        self.assertEqual(types.ListType, type(returned))
        self.assertEqual([3, 6, 9, 12, 15, 18], returned)
