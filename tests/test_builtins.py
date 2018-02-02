# -*- coding: utf-8 -*-

"""
Tests for builtins.
"""

import types
import unittest


class TestBuiltInFunctions(unittest.TestCase):
    """
    Exploring content from https://docs.python.org/2/library/functions.html
    """

    def test_abs(self):
        """
        Demonstrate the built-in function abs
        """
        self.assertEqual(abs(-12), 12)
        self.assertEqual(abs(3.5), 3.5)
        self.assertEqual(abs(3-4j), 5)

    def test_all(self):
        """
        Demonstrate the built-in function all
        """
        self.assertTrue(all([1, 2, 3]))
        self.assertFalse(all(["hello", "world", None]))
        self.assertTrue(all([]))

    def test_any(self):
        """
        Demonstrate the built-in function any
        """
        self.assertTrue(any([None, 2, None]))
        self.assertTrue(all([]))

    def test_basestring(self):
        """
        Demonstrate the built-in function basestring - which is actually an abstract type
        """
        self.assertTrue(isinstance('yo', basestring))
        self.assertTrue(isinstance(r'yo', basestring))
        self.assertTrue(isinstance(u'yo', basestring))
        self.assertFalse(isinstance(unittest, basestring))

    def test_bin(self):
        """
        Demonstrate the built-in function bin
        """
        self.assertEqual(bin(5), '0b101')

        class Foo(object):

            def __index__(self):
                return 7

        self.assertEqual(bin(Foo()), '0b111')  # requires an int, so invokes __index__

    def test_bool(self):
        """
        Demonstrate the built-in function bool
        """
        self.assertTrue(bool(1))
        self.assertTrue(bool('foo'))
        self.assertFalse(bool(0))
        self.assertFalse(bool(None))

    def test_bytearray(self):
        """
        Demonstrate the built-in function bytearray
        """
        self.assertEqual(bytearray(2), bytearray(b'\x00\x00'))
        self.assertEqual(bytearray([128, 168]), bytearray(b'\x80\xa8'))
        self.assertEqual(bytearray(u'föo', encoding='ascii', errors='replace'), bytearray(b'f?o'))

        # source objects with buffer interface not explored here -
        # see https://jakevdp.github.io/blog/2014/05/05/introduction-to-the-python-buffer-protocol/

    def test_callable(self):
        """
        Demonstrate the built-in function callable
        """
        self.assertTrue(callable(unittest.TestCase))
        self.assertTrue(callable(self))  # because __call__ is implemented
        self.assertTrue(callable(self.__eq__))
        self.assertFalse(callable('foo'))
        self.assertFalse(callable(None))

    def test_chr(self):
        """
        Demonstrate the built-in function chr
        """
        self.assertEqual(chr(38), '&')
        self.assertRaises(ValueError, chr, 256)

    def test_classmethod(self):
        """
        Demonstrate the built-in function classmethod
        """
        class C(object):

            @classmethod
            def f(cls):
                return cls.__name__

        self.assertEqual(C.f(), 'C')
        self.assertEqual(C().f(), 'C')

    def test_cmp(self):
        """
        Demonstrate the built-in function cmp
        """
        self.assertEqual(cmp(1, 1), 0)
        self.assertTrue(cmp(0, 1) < 0)  # typically -1 but docs say negative integer ..
        self.assertTrue(cmp(1, 0) > 0)  # .. positive integer

    def test_compile(self):
        """
        TODO - see https://eli.thegreenplace.net/2009/11/28/python-internals-working-with-python-asts
        """
        pass

    def test_complex(self):
        """
        Demonstrate the built-in function complex
        """
        self.assertEqual(complex(3, 4), 3+4j)
        self.assertEqual(complex('3+4j'), 3+4j)

    def test_delattr(self):
        """
        Demonstrate the built-in function delattr
        """
        class C(object):
            animal = 1
            mineral = 2
            vegetable = 3

        delattr(C, 'animal')
        self.assertFalse('animal' in dir(C))

    def test_dict(self):
        """
        Demonstrate the built-in function dict
        """
        d = {'one': 1, 'two': 2, 'three': 3}
        self.assertEqual(dict(one=1, two=2, three=3), d)
        self.assertEqual(dict(zip(['one', 'two', 'three'], [1, 2, 3])), d)
        self.assertEqual(dict([('two', 2), ('one', 1), ('three', 3)]), d)
        self.assertEqual(dict({'three': 3, 'one': 1, 'two': 2}), d)

    def test_dir(self):
        """
        Demonstrate the built-in function dir
        """

        class C(object):
            animal = 1
            mineral = 2
            vegetable = 3

        self.assertEqual(type(dir(C)), types.ListType)
        self.assertTrue('animal' in dir(C))
        self.assertTrue('mineral' in dir(C))
        self.assertTrue('vegetable' in dir(C))
