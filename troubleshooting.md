# Troubleshooting

## Python

### Check whether a package is installed or not

    python -c 'help("modules")' | grep <name of the package>

Or, for example:

    (email) ...$ find "$(pipenv --venv)/lib" -name "*pytest*"

## Pipenv

### Locking failed!

This error may occur and you have no idea why.

First I remove all the previously installed packages:

    (email) ...$ pipenv uninstall --all

Then, I make sure that a package that was installed has effectively been removed. For example (assuming that `pytest` was installed):

    (email) ...$ python -c 'help("modules")' | grep pytest

Rename the file `Pipfile` so it will not be used again:

    (email) ...$ mv Pipfile Pipfile.backup

Delete the file `Pipfile.lock`:

    (email) ...$ rm Pipfile.lock

Then try to install the packages again.

### Cannot import name 'Template'

If you use the versions (_or greater_) of `pip` and `pipenv` listed below :

    $ pipenv --version
    pipenv, version 2018.11.26

    $ pip --version
    pip 19.0.3 from /usr/local/lib/python3.6/site-packages/pip (python 3.6)

Then make sure that there is no file named "`string.py`" in the current directory that shadows the package "`string`"!

