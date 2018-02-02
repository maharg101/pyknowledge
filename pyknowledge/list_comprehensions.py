# -*- coding: utf-8 -*-

"""
pyknowledge.list_comprehensions

This module explores material found at http://www.learnpython.org/en/List_Comprehensions
"""


def divisible_by_three(number_list):
    """
    Given a list of numbers, return a list of the numbers which are divisible by three.
    """
    return [x for x in number_list if not x % 3]
