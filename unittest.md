# Unit tests

## Synopsis

    import unittest
    import os
    import sys

    # Set the Python search path...
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir))

    from dbeurive.imap.client import Client
        
        def test_method1(self):
            ...

        def test_method2(self):
            ...

    # The code below allows you to run the unit test by simply executing it.
    if __name__ == '__main__':
        unittest.main()

## Running the unit tests

### Running a single unit test

    python -m unittest testfile.py

_By default_, you have to be in **the same directory as the file that implements the unit test** ! Indeed, if you try to execute the command `python3 -m unittest ./tests/testfile.py`, then `unittest` will try to load the **module** `tests.testfile`.

You can specify the path to the Python script that implements the unit tests. However, to do that, you must set the environment variable `PYTHONPATH` so that Python knowns where to look for the namespace "tests". For example, assuming that we have the following directory tree:

    /home/dev/projects/email
    └── tests
        └── testfile.py

Then, you can run:

    $ PYTHONPATH=/home/dev/projects/email
    $ python -m unittest tests/testfile.py

### Automatisation

#### Using unittest discover

Let's say that the unit tests files are located under the directory `tests`.

    .
    ├── tests
    │   ├── client_test.py
    │   ├── config_test.py
    └── unittest.sh

The script `unittest.sh` (shown below) will run the unit tests `client_test.py` and `config_test.py`.

    #!/usr/bin/env bash
    # 
    # unittest.sh
    #
    # Usage:
    #
    #    unittest.sh
    #    unittest.sh -v

    SOURCE="${BASH_SOURCE[0]}"
    while [ -h "$SOURCE" ] ; do SOURCE="$(readlink "$SOURCE")"; done
    readonly __DIR__="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

    echo "Run relatively to \"${__DIR__}\""

    python -m unittest discover -s "${__DIR__}/tests" "$@" -p *_test.py

Please note:

* The option `-s` specifies the path to the unit tests implementations.
* The option `-p` defines the naming scheme that applies to a unit test implementation.

#### Use xmlrunner

Install `xmlrunner`:

    pipenv install xmlrunner
