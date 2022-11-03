# glem

GLEM is a lemmatizer for Ancient Greek.

It has been created in the project [Unraveling the Language of Perspective](http://ncs.ruhosting.nl/perspective/), which is supported by the EU under FP7, ERC Starting Grant 338421-Perspective.

The paper 'A memory-based lemmatizer for Ancient Greek' reports on how it works, what material it uses, and what the accuracy is. It can be found in the repository and at http://dl.acm.org/citation.cfm?id=3078100.

A webservice where you can upload texts that you want to have lemmatized can be found at https://webservices.cls.ru.nl/. Or you can host your own.

## Dependencies

Just **Python 3** for the simple word list based lemmatizer.

To add machine learning based lemmatization that also takes into account the context, glem uses [Frog](https://languagemachines.github.io/frog/) via its [python binding](https://github.com/proycon/python-frog).

## Installation

Run: ``pip install .``

We recommend using a Python virtual environment of your own. Alternatively for a global installation,
prepend ``sudo``.


## Example usage

Glem comes with a pretrained model, based on lemmas chosen by humans (in the UiO PROIEL project, PI: Dag Haug), for Herodotus. You can use it (with or without Frog) as follows:

```
glem -f input.txt
```

The files for this model can be found in ``glem/pretrained_models/herodotus`` .

## Webservice

A ``Dockerfile`` is provided for deployment of the GLEM webservice in production environments.

From the repository root, build as follows:

``
$ docker build -t webglem .
``

Consult the [Dockerfile](Dockerfile) for various build-time parameters that you may want to set for your own production environment.

When running, mount the path where you want the user data stored into the container, a directory `webglem-userdata` will be created here:

``
$ docker run -p 8080:80 -v /path/to/data/dir:/data webglem
``
