# Package

## Descrition

Basically, a package is a directory with a bunch of Python files ("`.py`").

**Before Python 3.3**, a file called "`__init__.py`" must be present in the package directory. This file is required to make Python treat the directories as containing packages.

**From Python 3.3** (included), the file "`__init__.py`" is not required anymore. See [PEP 420 -- Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420/).

## Setting path

The environment variable that lists all tops of packages directories trees is `PYTHONPATH`.

For some specific use cases, it can be interesting to dynamically set this information:

    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir))

or:

    if __name__ == "__main__":
        import sys
        import os
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir))

> If you use PyCharm, then you can tell the editor where to look for packages.

## \_\_pycache\_\_

    find ./ -type d -name "__pycache__" -print

See [PEP 3147 -- PYC Repository Directories](https://www.python.org/dev/peps/pep-3147/)

> Python's import machinery is extended to write and search for byte code cache files in a single directory inside every Python package directory. This directory will be called \_\_pycache\_\_.

Whenever Python loads a Python file ("`.py`") that is interpreted as being a module (that is, a package component), it creates a directory called "`__pycache__`" within the directory that contains this file.

> Make sure to declare all directories "`__pycache__`" in the appropriate "`.gitignore`" files.

> Please note that the directory that contains the unit tests (typically "`tests`") may, or may not, be treated as being a package, depending on how you use the module "`unittest`". However, as a general rule, you should add the entry "`__pycache__`" to the file "`.gitignore`".
