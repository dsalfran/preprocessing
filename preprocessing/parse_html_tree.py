# coding: utf8
"""This module preprocess html documents, removing unnecesary nodes"""
# -------------------------------------------------------------------
# System modules
# -------------------------------------------------------------------
import logging
import re
# ---------------------------------------------
# External dependencies
# ---------------------------------------------
import bs4
# -------------------------------------------------------------------
# Local dependencies
# -------------------------------------------------------------------
from preprocessing.utils import fix_encoding_of_string, replace_dates
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# Config
# -------------------------------------------------------------------
# Logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
logger.propagate = False

# Tags to remove from html object
pesky_tags = ['script', 'form', 'link', 'img', 'iframe', 'noscript', 'svg',
              'style', 'meta']

peskier_tags = ['script', 'style', 'form', 'link', 'img', 'iframe', 'head',
              'noscript', 'svg', 'meta', 'button', 'pre', 'map', 'area',
              'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul']

invalid_tags = ['b', 'i', 'u', 'a', 'font', 'strong', 'center', 'span']


def parse_html_tree(html, selector="body", pesky_tags=pesky_tags, token_replacement=False, tags_replacement=False):
    """This function removes some unnecesary html tags from the html object. The
tags removed are specified in the global variable "pesky_tags"
    """
    html = fix_encoding_of_string(html)
    # some methods work better if dates and URLs are removed
    if token_replacement:
        html = replace_dates(html)
        html = re.sub(r'<a.*></a>', 'URL_ADDRESS', html)

    # Get the document body
    soup = bs4.BeautifulSoup(html, 'lxml').select(selector)

    if not soup:
        # Just return a fake empty body (Null Object pattern)
        return bs4.BeautifulSoup("<body></body>", 'lxml')

    soup = soup[0]

    # Remove pesky tags
    for tag in pesky_tags:
        for node in soup.find_all(tag):
            node.decompose()

    # Replace nodes with 'invalid_tags' with just their text
    if tags_replacement:
        for tag in invalid_tags:
            for match in soup.findAll(tag):
                match.replaceWithChildren()

    # Then simply extract the text
    return soup
