
#! /usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname),'r',encoding='utf-8').read()

setup(
    name = "Glem",
    version = "1.0",
    author = "Corien Bary, Iris Hendrickx, Peter Berck, Wessel Stoop",
    author_email = "c.bary@let.ru.nl",
    description = ("GLEM is a lemmatizer for Ancient Greek."),
    license = "GPL",
    keywords = "nlp computational_linguistics entities linguistics ancient_greek, lemmatizer lemmatization frog",
    url = "https://github.com/GreekPerspective/glem",
    packages=[],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Text Processing :: Linguistic",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    zip_safe=False,
    include_package_data=False,
    install_requires=[],
    entry_points = {}
)
