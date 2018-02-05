# -*- coding: utf-8 -*-

"""
pyknowledge.map_filter_reduce

This module explores material found at http://book.pythontips.com/en/latest/map_filter.html
"""

from functools import reduce

def squared(numbers):
    """
    Given a list of integers, return a list of each one squared.
    """
    return map(lambda x: x ** 2, numbers)


def squared_and_summed(numbers):
    """
    Given a list of integers, return a list of lists of the integer squared and summed.
    """
    funcs = [lambda x: x ** 2, lambda x: x + x]
    return [
        map(lambda x: x(number), funcs)
        for number in numbers
    ]


def less_than_zero(numbers):
    """
    Given a list of integers, return a list of integers that are less than zero.
    List comprehensions may be a better alternative.
    """
    return filter(lambda x: x < 0, numbers)


def product(numbers):
    """
    Given a list of integers, return the product of them.
    Note import of reduce from functools for compatibility with Python 3
    """
    return reduce((lambda x, y: x * y), numbers)
