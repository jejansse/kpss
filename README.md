# Kraaij-Pohlmann Dutch Snowball Stemmer

This repository contains a Python version of the Kraaij-Pohlmann Snowball stemmer you can find in SBL format on the [snowball site](http://snowball.tartarus.org/algorithms/kraaij_pohlmann/stemmer.html).

## What & why?

The Dutch Snowball stemmer that is included in NLTK, ElasticSearch etc. performs OK-ish, but can be improved. The Kraaij-Pohlmann algorithm is more complex and creates better stems, albeit at the cost of not always being very interpretable. Since I was unable to find an implementation of the Kraaij-Pohlmann algorithm in Python I decided to package up a version generated using sbl2py from the SBL file on the [snowball site](http://snowball.tartarus.org/algorithms/kraaij_pohlmann/stemmer.html). By installing this package you can use the stemmer without having to go through sbl2py.

## Installation

Clone the repository:

```
git clone https://github.com/jejansse/kpss
```

Then use buildout to build the egg:

```
cd kpss
python bootstrap.py
bin/buildout
bin/buildout setup . bdist_egg
```

The egg can then be used anywhere you want (e.g. in a PySpark script).

## Usage

Usage of the stemmer is pretty straightforward. First ensure the egg is on your python path:

```
PYTHONPATH="$PYTHONPATH:/path/to/kpss/kpss-0.1-py2.7.egg" bin/python
```

Then just load the module and call the `stem` function:

```
>>> from kpss import kpss
>>> [kpss.stem(t) for t in "Alle eendjes zwemmen in het water".split()]
[u'Alle', u'eend', u'zwem', u'in', u'het', u'water']
```
