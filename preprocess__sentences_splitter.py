#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module defines the sentences splitter used in several text processing methods"""
# ---------------------------------------------
# System modules
# ---------------------------------------------
# ---------------------------------------------
# External dependencies
# ---------------------------------------------
import nltk
# ---------------------------------------------
# Local dependencies
# ---------------------------------------------
# ---------------------------------------------


# We use the nltk sentence segmenter to split the contents of HTML documents
# into sentences
sentence_splitter = nltk.tokenize.punkt.PunktSentenceTokenizer()
# Add more german abbreviation rules to the sentence splitter
sentence_splitter._params.abbrev_types.add('inkl')
sentence_splitter._params.abbrev_types.add('incl')
sentence_splitter._params.abbrev_types.add('u.v.m')
sentence_splitter._params.abbrev_types.add('u.a')
sentence_splitter._params.abbrev_types.add('u.n')
sentence_splitter._params.abbrev_types.add('o.ä')
sentence_splitter._params.abbrev_types.add('i.b')
sentence_splitter._params.abbrev_types.add('jhrl')
sentence_splitter._params.abbrev_types.add('e.v')
sentence_splitter._params.abbrev_types.add('n.v')
sentence_splitter._params.abbrev_types.add('mio')

sentence_splitter._params.abbrev_types.add('tel.-nr')
sentence_splitter._params.abbrev_types.add('telefon-nr')
sentence_splitter._params.abbrev_types.add('nr')
sentence_splitter._params.abbrev_types.add('max')
sentence_splitter._params.abbrev_types.add('min')
sentence_splitter._params.abbrev_types.add('abs')
sentence_splitter._params.abbrev_types.add('o.g')
sentence_splitter._params.abbrev_types.add('referenz-nr')
sentence_splitter._params.abbrev_types.add('ref.-nr')
sentence_splitter._params.abbrev_types.add('z.t')
sentence_splitter._params.abbrev_types.add('mind')
sentence_splitter._params.abbrev_types.add('insb')

sentence_splitter._params.abbrev_types.add('bezgl')
sentence_splitter._params.abbrev_types.add('zusätzl')
sentence_splitter._params.abbrev_types.add('gem')
sentence_splitter._params.abbrev_types.add('verggr')

sentence_splitter._params.abbrev_types.add('stellv')
sentence_splitter._params.abbrev_types.add('etc')
sentence_splitter._params.abbrev_types.add('z.z')
sentence_splitter._params.abbrev_types.add('tvöd')

sentence_splitter._params.abbrev_types.add('s-bhf')
sentence_splitter._params.abbrev_types.add('z.b')
sentence_splitter._params.abbrev_types.add('dr')
sentence_splitter._params.abbrev_types.add('a.m')

sentence_splitter._params.abbrev_types.add('dr.med')
sentence_splitter._params.abbrev_types.add('tel')
sentence_splitter._params.abbrev_types.add('bzw')
sentence_splitter._params.abbrev_types.add('bzgl')

sentence_splitter._params.abbrev_types.add('ggf')
sentence_splitter._params.abbrev_types.add('ggfs')

sentence_splitter._params.abbrev_types.add('ca')
sentence_splitter._params.abbrev_types.add('z')
sentence_splitter._params.abbrev_types.add('hd')
sentence_splitter._params.abbrev_types.add('dipl.ing')
sentence_splitter._params.abbrev_types.add('dipl.-ing')
sentence_splitter._params.abbrev_types.add('dipl.kfm')
sentence_splitter._params.abbrev_types.add('dipl.-kfm')

sentence_splitter._params.abbrev_types.add('dt')
sentence_splitter._params.abbrev_types.add('co')
sentence_splitter._params.abbrev_types.add('zzgl')
sentence_splitter._params.abbrev_types.add('str')
sentence_splitter._params.abbrev_types.add('gr')
sentence_splitter._params.abbrev_types.add('d.h')
sentence_splitter._params.abbrev_types.add('dgl')

sentence_splitter._params.abbrev_types.add('d.i')
sentence_splitter._params.abbrev_types.add('ehem')
sentence_splitter._params.abbrev_types.add('amtl')
sentence_splitter._params.abbrev_types.add('entspr')
sentence_splitter._params.abbrev_types.add('evtl')
sentence_splitter._params.abbrev_types.add('fa')
sentence_splitter._params.abbrev_types.add('gegr')
sentence_splitter._params.abbrev_types.add('hrn')

sentence_splitter._params.abbrev_types.add('11. mal')
