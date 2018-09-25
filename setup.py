#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------
# System modules
# ---------------------------------------------
import os
import sys
from setuptools import find_packages, setup


# Package meta-data.
NAME = 'preprocessing'
DESCRIPTION = 'Job posts preprocessing methods'
URL = 'https://dsalfran@bitbucket.org/talentbait/preprocessing.git'
EMAIL = 'danielsalfran@gmail.com'
AUTHOR = 'Daniel Salfran'
LICENSE = 'GPL-3'

required = [
    'langdetect>=1.0.7','bs4>=0.0.1','nltk>=3.3', 'lxml>=4.2.5'
]

setup(
    name=NAME,
    version='0.1',
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=required,
    include_package_data=True,
    license=LICENSE,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # data_files=datafiles
    package_data={'preprocessing': ['cities_large.txt']}
)

