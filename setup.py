
#! /usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname),'r',encoding='utf-8').read()

setup(
    name = "Glem",
    version = "1.3.1", #also update in glem.py and webglem.py
    author = "Corien Bary, Iris Hendrickx, Peter Berck, Wessel Stoop",
    author_email = "c.bary@let.ru.nl",
    description = ("GLEM is a lemmatizer for Ancient Greek."),
    license = "GPL-3.0-only",
    keywords = "nlp computational_linguistics entities linguistics ancient_greek, lemmatizer lemmatization frog clam webservice rest",
    url = "https://github.com/GreekPerspective/glem",
    packages=["glem","webglem"],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Text Processing :: Linguistic",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    zip_safe=False,
    include_package_data=True,
    package_data = { 'glem': ['extra-wlt.txt','list_proiel_perseus_merged_word_lemma_POS_nofreq','list_proiel_word_lemma_POS_freq','pretrained_models/herodotus/*'], 'webglem':['*.wsgi','*.yml'] },
    install_requires=['CLAM >= 3.0', 'python-frog'],
    entry_points = { 'console_scripts': [ 'glem = glem.glem:main' ]}
)
