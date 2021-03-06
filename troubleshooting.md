# Troubleshooting

## Python

### Check whether a package is installed or not

#### Solution 1

    $ pipenv shell
    $ python -c "import googleapiclient.discovery"

> This solution is the best one.

#### Solution 2

    $ pipenv shell
    $ python -c 'help("modules")' | grep googleapiclient

#### Solution 3

    $ pipenv shell
    $ python -c 'help("modules")' | grep googleapiclient

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

## PyCharm

### Force the re-indexing of all libraries

Sometimes, particularly when using remote interpreters, remote libraries are ignored by the code editor.

If this the the case then:

First, check if the libraries show up in the remote interpreter configuration panel.

![Remote packages](images/pycharm-remote-packages.png)

If the libraries show up, then it means that the editor knows about them, but the cache was not up to date. You should invalidate the cache:

![Invalidate the cache](images/pycharm-invalidate-cache.png)

