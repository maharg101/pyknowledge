# -*- coding: utf-8 -*-

"""
Tests for multiple_function_arguments.
"""

import unittest
import types

from pyknowledge import multiple_function_arguments


class TestMultipleFunctionArguments(unittest.TestCase):

    def test_build_string(self):
        """
        Test that the multiple argument function behaves as expected.
        """
        returned = multiple_function_arguments.build_string(
            'I', 'really', 'love', 'python', 'it', 'is', 'cool',
            twice='really', thrice='cool'
        )
        self.assertEqual(type(returned), types.StringType)
        self.assertEqual('I really really love python it is cool cool cool', returned)
