# -*- coding: utf-8 -*-

"""
Tests for collections_containers.
"""

import unittest

from collections import defaultdict
from pyknowledge import collections_containers


class TestCollectionsContainers(unittest.TestCase):

    def test_favourite_colours_to_dict(self):
        """
        Test that the defaultdict(list) works as expected.
        """
        colours = (
            ('Yasoob', 'Yellow'),
            ('Ali', 'Blue'),
            ('Arham', 'Green'),
            ('Ali', 'Black'),
            ('Yasoob', 'Red'),
            ('Ahmed', 'Silver'),
        )
        colours_dict = collections_containers.favourite_colours_to_dict(colours)
        self.assertEqual(type(colours_dict), type(defaultdict()))
        self.assertEqual(
            colours_dict,
            {
                'Arham': ['Green'],
                'Yasoob': ['Yellow', 'Red'],
                'Ahmed': ['Silver'],
                'Ali': ['Blue', 'Black']
            }
        )

    def test_nested_colours_to_dict(self):
        """
        Test that the nested defaultdict works as expected.
        """
        colours = (
            ('Yasoob', 'hates', 'Yellow'),
            ('Ali', 'prefers', 'Blue'),
            ('Arham', 'likes', 'Green'),
            ('Ali', 'meh', 'Black'),
            ('Yasoob', 'loves', 'Red'),
            ('Ahmed', 'abhors', 'Silver'),
        )
        colours_dict = collections_containers.nested_colours_to_dict(colours)
        self.assertEqual(type(colours_dict), type(defaultdict()))
        self.assertEqual(
            colours_dict,
            {
                'Arham': {'likes': 'Green'},
                'Yasoob': {'hates': 'Yellow', 'loves': 'Red'},
                'Ahmed': {'abhors': 'Silver'},
                'Ali': {'prefers': 'Blue', 'meh': 'Black'}
            }
        )

    def test_ordered_dict_of_colours(self):
        """
        Test the the OrderedDict preserves the order of the given data.
        """
        input = [("Red", 198), ("Green", 170), ("Blue", 160)]
        colours_dict = collections_containers.ordered_dict_of_colours(input)
        self.assertEqual(input, [(k, v) for k,v in colours_dict.items()])

    def test_colour_counter(self):
        """
        Test the Counter works as expected.
        """
        colours = (
            ('Yasoob', 'Yellow'),
            ('Ali', 'Blue'),
            ('Arham', 'Green'),
            ('Ali', 'Black'),
            ('Yasoob', 'Red'),
            ('Ahmed', 'Silver'),
        )
        counter = collections_containers.colour_counter(colours)
        self.assertEqual(
            counter,
            dict(Yasoob=2, Ali=2, Arham=1, Ahmed=1)
        )

    def test_rolling_colours_shift_3_right(self):
        """
        Test the deque (doubled-ended queue) works as expected.
        """
        self.assertEqual(
            collections_containers.rolling_colours_shift_3_right(
                ['Green', 'Yellow', 'Red', 'Blue', 'Orange', 'White']
            ),
            ['Blue', 'Orange', 'White', 'Green', 'Yellow', 'Red']
        )

    def test_get_animal_namedtuple(self):
        """
        Test the namedtuple works as expected.
        """
        perry = collections_containers.get_animal_namedtuple()
        self.assertEqual(perry.name, 'perry')
        self.assertEqual(perry.age, 31)
        self.assertEqual(perry.type, 'cat')

        def inc_age(obj):
            obj.age = obj.age + 1

        self.assertRaises(AttributeError, inc_age, perry)

        self.assertEqual(
            perry._asdict(),
            {
                'name': 'perry',
                'age': 31,
                'type': 'cat'
            }
        )

    def test_get_animal_type_for_dog(self):
        """
        Test that the Enum works as expected.
        """
        if collections_containers.enum_supported:  # from 3.4
            self.assertEqual(
                collections_containers.get_animal_type_for_dog(),
                collections_containers.Species.dog
            )
            self.assertEqual(collections_containers.Species.dog, 2)