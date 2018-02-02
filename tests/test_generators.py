# -*- coding: utf-8 -*-

"""
Tests for generators.
"""

import unittest
import types

from pyknowledge import generators


class TestGenerators(unittest.TestCase):

    def test_fib(self):
        """
        Test that the generator behaves as expected.
        """
        self.assertEqual(type(generators.fib()), types.GeneratorType)
        sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
        for index, n in enumerate(generators.fib()):
            if index == len(sequence):
                break
            self.assertEqual(n, sequence[index])
