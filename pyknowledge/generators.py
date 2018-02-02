# -*- coding: utf-8 -*-

"""
pyknowledge.generators

This module explores material found at http://www.learnpython.org/en/Generators
"""


def fib():
    """
    Generates the Fibonacci series.

    Returns a generator which will yield integer values.
    """
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b
