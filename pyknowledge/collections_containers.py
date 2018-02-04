# -*- coding: utf-8 -*-

"""
pyknowledge.collections_containers

This module explores material found at http://book.pythontips.com/en/latest/collections.html
"""

from collections import defaultdict, OrderedDict, Counter, deque, namedtuple

enum_supported = True
try:
    from enum import Enum
except ImportError:
    enum_supported = False  # not until Python 3.4


def favourite_colours_to_dict(colours):
    """
    Compiles a list of tuples denoting favourite colours into a defaultdict containing lists.
    No need to check for existence of keys !
    """
    favourite_colours = defaultdict(list)

    for name, colour in colours:
        favourite_colours[name].append(colour)

    return favourite_colours


def nested_colours_to_dict(colours):
    """
    Compiles a list of 3-tuples denoting attitudes to colours into a nested defaultdict.
    See https://en.wikipedia.org/wiki/Autovivification#Python
      and https://gist.github.com/hrldcpr/2012250
    """
    tree = lambda: defaultdict(tree)
    colour_attitudes = tree()
    for name, attitude, colour in colours:
        colour_attitudes[name][attitude] = colour

    return colour_attitudes


def ordered_dict_of_colours(colours):
    """
    Compiles a list of tuples into an OrderedDict.
    """
    return OrderedDict(colours)


def colour_counter(colours):
    """
    Counts colours given for each name in a list of (name, colour) tuples.
    """
    return Counter(name for name, colour in colours)


def rolling_colours_shift_3_right(colours):
    """
    Given a list of colours, return a list with values shifted 3 places to the right.
    Colours which 'fall off' the right hand end reappear at the left end.
    """
    colours_deque = deque(colours, maxlen=len(colours))
    for i in range(3):
        colours_deque.appendleft(colours_deque[-1])
    return list(colours_deque)


def get_animal_namedtuple():
    """
    Returns a namedtuple so that it can be inspected in the test.
    """
    Animal = namedtuple('Animal', 'name age type')
    return Animal(name="perry", age=31, type="cat")


if enum_supported:

    class Species(Enum):
        cat = 1
        dog = 2
        horse = 3


    def get_animal_type_for_dog():
        return Species.dog