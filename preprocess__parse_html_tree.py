# coding: utf8
"""This module preprocess html documents, removing unnecesary nodes"""
# -------------------------------------------------------------------
# System modules
# -------------------------------------------------------------------
import logging
# ---------------------------------------------
# External dependencies
# ---------------------------------------------
import bs4
# -------------------------------------------------------------------
# Local dependencies
# -------------------------------------------------------------------
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# Config
# -------------------------------------------------------------------
# Logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
logger.propagate = False

# Tags to remove from html object
pesky_tags = ['script',
              'form',
              'link',
              'img',
              'iframe',
              'noscript',
              'svg',
              'style',
              'meta']


def parse_html_tree(html, selector="body"):
    """This function removes some unnecesary html tags from the html object. The
tags removed are specified in the global variable "pesky_tags"
    """
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

    # Then simply extract the text
    return soup
