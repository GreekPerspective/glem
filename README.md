# glem
GLEM is a lemmatizer for Ancient Greek.

It has been created in the project 'Unraveling the Language of Perspective' (http://ncs.ruhosting.nl/perspective/), which is supported by the EU under FP7, ERC Starting Grant 338421-Perspective.

The paper 'A memory-based lemmatizer for Ancient Greek' reports on how it works, what material it uses, and what the accuracy is. It can be found in the repository and at http://dl.acm.org/citation.cfm?id=3078100.

A webservice where you can upload texts that you want to have lemmatized can be found at https://webservices-lst.science.ru.nl/portal/


Dependencies
============

Just **Python 3** for the simple word list based lemmatizer.

To add machine learning based lemmatization that also takes into account the context, you also need **[Frog](https://languagemachines.github.io/frog/)**. By far the easiest way to install Frog is to use [LaMachine](https://proycon.github.io/LaMachine/).

Installation
=============

Run: ``python3 setup.py install``

We recommend using LaMachine or a Python virtual environment of your own. Alternatively for a global installation,
prepend ``sudo``.


Example usage
=============

Glem comes with a pretrained model, based on lemmas chosen by humans (in the UiO PROIEL project, PI: Dag Haug), for Herodotus. If you are inside the Lamachine environment (something like ```lamachine/bin/activate```), you can use it (with or without Frog) as follows:

```glem -f input.txt```

The files for this model can be found in ```glem/pretrained_models/herodotus``` .
