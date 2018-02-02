# -*- coding: utf-8 -*-

"""
pyknowledge.multiple_function_arguments

This module explores material found at http://www.learnpython.org/en/Multiple_Function_Arguments
"""


def build_string(prefix, *words, **functions):
    """
    Returns a string
     - prefixed with the given prefix
     - containing the words given as positional arguments, with each word:
       - repeated twice if the word is specified by the option key 'twice'
       - repeated three times if the word is specified by the option key 'thrice'
    """
    words_to_return = [prefix]
    for word in words:
        if word == functions['twice']:
            words_to_return.extend([word]*2)
        elif word == functions['thrice']:
            words_to_return.extend([word]*3)
        else:
            words_to_return.append(word)
    return ' '.join(words_to_return)
