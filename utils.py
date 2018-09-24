#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module contains small helper and general utility functions"""
# ---------------------------------------------
# System modules
# ---------------------------------------------
import re
import logging
# ---------------------------------------------
# External dependencies
# ---------------------------------------------
# ---------------------------------------------
# Local dependencies
# ---------------------------------------------
# --------------------------------------------


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

