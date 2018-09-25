# coding: utf8
"""This module preprocess html documents, extracting blocks of text from unordered lists and paragraphs"""
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
from preprocessing.parse_html_tree import parse_html_tree, peskier_tags
from preprocessing.utils import fix_encoding_of_string, replace_dates
from preprocessing.text_manipulation import messy_paragrah_to_sentences
# -------------------------------------------------------------------


def extract_flattened_uls(tree, simplified_blocks=None):
    if simplified_blocks is None:
        simplified_blocks = []

    missing_id = 0

    for ul in tree.find_all('ul'):
        if ul.get('id') is None:
            ul['id'] = ul_id = 'ul-{}'.format(missing_id)
            missing_id += 1

        li_id = 0
        for li in ul.find_all('li'):
            li_string = li.text
            li_string = li_string.strip()
            if li.get('id') is None:
                _id = 'li-{}'.format(li_id)
                li_id += 1
            simplified_blocks.append({'text': li_string, "meta": {"ul": ul_id, "li": _id}})

    return simplified_blocks


def extract_flattened_paragraphs(tree, simplified_blocks=None):
    if simplified_blocks is None:
        simplified_blocks = []

    missing_id = 0


   # Extract paragraphs that are written as <p> ... </p>
    paragraphs = []
    for par in tree.find_all('p'):
        if len(par.text.split()) >= 5:
            paragraphs.append(par.text)

        par.decompose()

    # Extract paragraphs that are written as <div> ... </div>. This is done after
    # the paragraph (<p>) nodes have been deleted, to avoid duplication.
    for div in tree.find_all('div'):
        children_divs = div.find_all('div')
        if len(children_divs) > 1:
            pass
        else:
            if len(div.text.split()) >= 5:
                paragraphs.append(div.text)

            div.decompose()

    for item in paragraphs:
        par_id = 'par-{}'.format(missing_id)
        missing_id += 1
        sentences = messy_paragrah_to_sentences(item)
        li_id = 0
        for sentence in sentences:
            _id = "li-{}".format(li_id)
            li_id += 1
            simplified_blocks.append({'text': sentence, "meta": {"ul": par_id, "li": _id}})

    return(simplified_blocks)


def extract_flattened_blocks(html):
    tree = parse_html_tree(tree)
    simplified_blocks = extract_flattened_uls(tree)
    tree = parse_html_tree(html, pesky_tags=peskier_tags, token_replacement=True, tags_replacement=True)
    simplified_blocks = extract_flattened_paragraphs(tree, simplified_blocks)
    return simplified_blocks
