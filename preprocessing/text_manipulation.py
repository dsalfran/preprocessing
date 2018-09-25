#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module contains text manipulation functions"""
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
from preprocessing.sentences_splitter import sentence_splitter
# ---------------------------------------------


# ---------------------------------------------
# Config
# ---------------------------------------------
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def clean_messy_paragraph(paragraph):
    """Remove multiple spaces and line breaks from paragraphs. This is useful when dealing with text from html documents"""

    paragraph = re.sub(r'\n', ' ', paragraph)
    paragraph = re.sub(r'\s+', ' ', paragraph)

    return(paragraph)
