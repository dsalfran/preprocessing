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
from preprocessing.utils import fix_encoding_of_string, replace_dates, clean_messy_paragraph
from preprocessing.sentences_splitter import sentence_splitter
# -------------------------------------------------------------------


def extract_uls(tree, simplified_blocks=None):
    if simplified_blocks is None:
        simplified_blocks = []

    missing_id = 0
    for ul in tree.find_all('ul'):
        if ul.get('id') is None:
            ul['id'] = ul_id = 'ul-{}'.format(missing_id)
            missing_id += 1

        items = []
        for li in ul.find_all('li'):
            li_string = li.text
            li_string = li_string.strip()
            items.append(li_string)

        simplified_blocks.append({ul_id: items})

    return simplified_blocks



def flatten_ul_blocks(simplified_blocks):
    flatten_blocks = []

    for item in simplified_blocks:
        for key, value in item.items():
            for text in value:
                flatten_blocks.append({'meta': {'ul': key}, 'text': text})

    return flatten_blocks


def extract_paragraphs(tree, simplified_blocks=None):
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
        simplified_blocks.append({'meta': {'ul': par_id}, 'text': clean_messy_paragraph(item)})

    return simplified_blocks


def flatten_paragraphs(simplified_blocks, flatten_paragraphs=None):
    if flatten_paragraphs is None:
        flatten_paragraphs = []

    for item in simplified_blocks:
        meta = item.get('meta')
        sentences = sentence_splitter.tokenize(item.get('text'))
        for sentence in sentences:
            flatten_paragraphs.append({'meta': meta, 'text': sentence})

    return(flatten_paragraphs)


def extract_flattened_blocks(html):
    tree = parse_html_tree(html)
    blocks = flatten_ul_blocks(extract_uls(tree))
    tree = parse_html_tree(html, pesky_tags=peskier_tags, token_replacement=True,
                           tags_replacement=True)
    blocks = flatten_paragraphs(extract_paragraphs(tree), blocks)

    return blocks
