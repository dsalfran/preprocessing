#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module contains small helper and general utility functions"""
# ---------------------------------------------
# System modules
# ---------------------------------------------
import re
import hashlib
import logging
from copy import deepcopy
# ---------------------------------------------
# External dependencies
# ---------------------------------------------
# ---------------------------------------------
# Local dependencies
# ---------------------------------------------
# ---------------------------------------------


# ---------------------------------------------
# Config
# ---------------------------------------------
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


# ----------------------------------------
# Text manipulation
# ----------------------------------------
def fix_encoding_of_string(string):
    """
    This functions replaces common wrongly encoded characters by the proper utf8 one

    Input:
        string: string with (or whitout) encoding issues

    Output:
        string: same string as input with fixed issues
    """

    # Really strange characters
    string = re.sub(r'â', '', string)
    string = re.sub(r'â', '', string)
    string = re.sub(r'Ã', 'O', string)
    string = re.sub(r'â', '', string)

    # Replace non-breaking space
    # string = re.sub('\xa0', ' ', string)
    string = re.sub(' ', ' ', string)

    # Replace umlaute
    string = re.sub('Ã„', 'Ä', string)
    string = re.sub('Ã¤', 'ä', string)
    string = re.sub('Ã–', 'Ö', string)
    string = re.sub('Ã¶', 'ö', string)
    string = re.sub('Ã\x9c', 'Ü', string)
    string = re.sub('Ãœ', 'Ü', string)
    string = re.sub('Ã¼', 'ü', string)
    string = re.sub('Ã', 'ü', string)
    string = re.sub('Â´', "´", string)

    # Replace zero-width space in strings of array
    string = re.sub('\u200b', '', string)

    # Replace soft-hyphen
    string = re.sub('­', '', string)
    string = re.sub('\xad', '', string)

    # Repair ß
    string = re.sub('Ã', 'ß', string)
    string = re.sub('Ã\x9f', 'ß', string)
    string = re.sub('ÃŸ', 'ß', string)

    # Replace non-breaking space
    string = re.sub('\xa0', ' ', string)

    return string


def replace_dates(string):
    """This function replaces German format dates with a token string"""

    # replace dd.mm.yy or dd.mm.yyyy by DATE_STRING
    string = re.sub(r'\d{2}[/\.\-\s]\d{2}\.\d{2,4}', 'DATE_STRING', string)
    # replace dd.mm. by DATE_STRING
    string = re.sub(r'\d{2}[/\.\-\s]\d{2}\.', 'DATE_STRING', string)

    return(string)


def clean_messy_paragraph(paragraph):
    """Remove multiple spaces and line breaks from paragraphs. This is useful when dealing with text from html documents"""

    paragraph = re.sub(r'\n', ' ', paragraph)
    paragraph = re.sub(r'\s+', ' ', paragraph)

    return(paragraph)


def clean_line(line):
    """This function strips line breaks, tabs, and multiple and trailing blank spaces

    Input:
    line: string of text

    Returns: Clean line

    """

    if isinstance(line, str):
        line = re.sub(r'\n', ' ', line)
        line = re.sub(r'\\n', ' ', line)
        line = re.sub(r'\t', ' ', line)
        line = re.sub(r'\s+', ' ', line)
        return line.strip()

    return line


def computeMD5hash(string):
    """Function to compute hash of strings. Useful to find equal sentences

    """
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()


def yesbool(str):
    """
    This method parses a string with value `yes` or `no` and
    returns a corresponding `bool` value of `True` or `False`.
    Useful for parsing HTTP query args to allow the pretty use `&arg=yes`.

    >>> yesbool('yes')
    True
    >>> yesbool('no')
    False
    >>> try:
    ...     yesbool('maybe')
    ...     print("Haha, passed")
    ... except ValueError:
    ...     print("Didn't passed")
    Didn't passed
    """
    if str not in ['yes', 'no']:
        raise ValueError("'%s' is not a valid value. Should be either 'yes' or 'no'.")

    return str == 'yes'


# ----------------------------------------
# Python objects manipulation
# ----------------------------------------
def flatten_list(nested_list):
    """Flatten an arbitrarily nested list, without recursion (to avoid
    stack overflows). Returns a new list, the original list is unchanged.
    >> list(flatten_list([1, 2, 3, [4], [], [[[[[[[[[5]]]]]]]]]]))
    [1, 2, 3, 4, 5]
    >> list(flatten_list([[1, 2], 3]))
    [1, 2, 3]
    """
    nested_list = deepcopy(nested_list)

    while nested_list:
        sublist = nested_list.pop(0)

        if isinstance(sublist, list):
            nested_list = sublist + nested_list
        else:
            yield sublist
