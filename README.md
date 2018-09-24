# Preprocessing tools

This module provide general utilities and methods to help process html and text documents.

## Current methods:

1. `extract_sentences_from_html`: Cleans html objects and return the sentences it finds
2. `parse_html_tree`: Removes unnecesary html nodes from the document's body.
3. `replace_dates`: Replaces German format dates with a token string
4. `fix_encoding_of_string`: Replaces common encoding mistakes with the proper utf8 character.
