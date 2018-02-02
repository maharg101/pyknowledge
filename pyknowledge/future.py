# -*- coding: utf-8 -*-

"""
pyknowledge.future

This module explores material found at http://python-future.org/imports.html and other places
"""

from __future__ import absolute_import, division, print_function

import types


def important_function():
    """
    Just some examples
    """

    # print function
    assert(type(print) == types.BuiltinMethodType)
    assert(type(print) == types.BuiltinFunctionType)
    if 6 == 9:
        print('If the sun refuse to shine')

    # division
    assert(10 / 4 == 2.5)

    # absolute_import - https://docs.python.org/2.5/whatsnew/pep-328.html
    try:
        from . import foobar
    except ImportError:
        pass  # demonstrating that the relative import function works
