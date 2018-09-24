#!/usr/bin/env python
# -*- coding: utf-8 -*-
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


setup(
    name=NAME,
    version='1.0.8',
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
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
)

