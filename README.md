# Introduction

This repository contains some Python notes.

## Tools

* [pipenv](pipenv.md)
* [pycharm](pycharm.md)
* [unittest](unittest.md)
* [wheel](https://github.com/denis-beurive/pywheel)

## Style guides

General:

* [Google Python Style Guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)

DocStrings:

* [PEP 257: Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
* [Google Python Style Guide: docstrings](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#381-docstrings)
* [Example Google style docstrings](https://gist.github.com/candlewill/fce04bb26d402288cd02f09bd4f5f562)

## Code organisation

* [package](package.md)

## Language

* [operators](operators.md)
* [documentation](documentation.md)
* [inheritance](inheritance.md)
* [functions / decorators](function.md)
* [logging](logging.md)
* [type checking](type_checks.md)
* [unpack / splat](unpack.md)
* [debug](debug.md)
* [environment](environment.md)
* [lists](lists.md)
* [files](files.md)
* [directories](directories.md)
* [conversions](conversions.md)
* [dictionaries](dictionaries.md)
* [strings](strings.md)
* [regular expressions](regex.md)
* [comprehensions](comprehensions.md)
* [generator expression](generator_expression.md)
* [named tuple](namedtuple.md)
* [exception](exception.md)
* [object](object.md)
* [sorting](sorting.md)
* [module](module.md)
* [socket](socket.md)
* [closure](code/closure.py)
* [filters](code/filters.py)

# Design patterns

* [factory](factory.md)

# Packages

* [cli parsing](cli-parsing.md)
* [serialization](serialization.md)
* [logging](logging.md)
* [url](url.md)
* [base64](base64.md)
* [flask](flask.md)
* [uuid - get a unique ID](uniqid.md)
* [threading](lock.md)
* [datetime](datetime.md)

**Good packages**:

* [CLI parser: Click](https://click.palletsprojects.com/en/7.x/)

# Script examples

* [PlantUML automation](code/plantuml_automation.py)
* [Visit all entries within a data structure](code/data_walk.py)
* [Calculate fingerprints of all files within a given directory](code/md5src.py)
* Redis [producer](code/redis_producer.py) and [consumer](code/redis_consumer.py)
* [Timestamps comparaison](code/timestamp_cmp.py)
* [Fun with QR codes](code/qrcode_ex.py)

# Other

* [declaring the source encoding](encoding.md)
* [troubleshooting](troubleshooting.md)

**Tuples vs Lists**

A tuple is an assortment of data, separated by commas, which makes it similar to the Python list, but a tuple is fundamentally different in that a tuple is "immutable." This means that it cannot be changed, modified, or manipulated. 

**Sets vs Lists and Tuples**

Sets vs Lists and Tuples. Lists and tuples are standard Python data types that store values in a sequence. Sets are another standard Python data type that also store values. The major difference is that sets, unlike lists or tuples, **cannot have multiple occurrences of the same element** and **store unordered values**



