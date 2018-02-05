# -*- coding: utf-8 -*-

"""
Tests for map_filter_reduce.
"""

import unittest

from pyknowledge import map_filter_reduce


class TestGenerators(unittest.TestCase):

    def test_squared(self):
        """
        Test that mapping to a function works as expected.
        """
        self.assertEqual(
            map_filter_reduce.squared(range(1, 6)),
            [1, 4, 9, 16, 25]
        )

    def test_squared_and_summed(self):
        """
        Test mapping to multiple functions works as expected.
        """
        self.assertEqual(
            map_filter_reduce.squared_and_summed(range(1, 6)),
            [[1, 2], [4, 4], [9, 6], [16, 8], [25, 10]]
        )

    def test_less_than_zero(self):
        """
        Test the filter function works as expected.
        """
        self.assertEqual(
            map_filter_reduce.less_than_zero([-2, -1, 0, 1, 2]),
            [-2, -1]
        )

    def test_product(self):
        """
        Test the reduce function works as expected.
        """
        self.assertEqual(map_filter_reduce.product([1, 2, 3, 4]), 24)
