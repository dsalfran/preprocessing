#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module to hold global configuration settings"""
# ---------------------------------------------
# System modules
# ---------------------------------------------
import os
import logging
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
logging.basicConfig(level=logging.INFO)

# Define project path
path_project = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------
# General Data
# ---------------------------------------------
# Cities file
cities_list = path_project + "/cities_large.txt"

# ------------------------------
# BeautifulSoup
# ------------------------------
# Define the default bs4 html parser
html_parser = 'html5lib'
