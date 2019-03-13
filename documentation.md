# Documentation

There are several ways to document a Python code. One way to document the code is to use the Google style docstrings.

* [PEP 257: Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
* [Example Google style docstrings](https://gist.github.com/candlewill/fce04bb26d402288cd02f09bd4f5f562)
* [Google Python Style Guide: docstrings](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#381-docstrings)

## The Google Docstring

Example:

    """This module implements the configuration loader."""

    from typing import List
    import os
    import json
    from dbeurive.color import Color

    class Config:
        """Configuration container.

        Attributes:
            _path (str): path to the configuration file.
            _raw_config (dict): raw representation of the configuration.

        """

        def __init__(self, path: str):
            """Create a Configuration.

            The configuration is loaded from a file.

            Args:
                path (str): path to the configuration file to load.

            Raises:
                ValueError: the exception is raised whenever the configuration file could not be loaded.
            """
            if not os.path.exists(path):
                raise ValueError(f'The path {path} does not exist.')
            if not os.path.isfile(path):
                raise ValueError(f'The path {path} does not identifies a file.')
            self._path = path
            with open(path, 'r') as fd:
                text: str = fd.read()
            try:
                self._raw_config: dict = json.loads(text)
            except json.JSONDecodeError as e:
                raise ValueError(f'The configuration {path} is not valid: the content of the file is not a valid JSON ({e})')
            self._conf = self._validate_and_build_conf()

        def get_path(self) -> str:
            """Return the path to the configuration file.

            Returns:
                A string that represents the path to the configuration file.
            """
            return self._path

        def _validate_and_build_conf(self) -> List[Color]:
            """Validate the loaded configuration description and build the configuration.

            Returns:
                The method returns the configuration.

            Raises:
                ValueError: the exception is raised if the configuration is not valid.
            """
            if not isinstance(self._raw_config, list):
                raise ValueError(f'The configuration {self._path} is not valid: the JSON does not represent a list.')

            colors: List[Color] = []
            self._raw_config: list
            # noinspection PyUnusedLocal
            entry: dict
            for entry in self._raw_config:
                if not isinstance(entry, dict):
                    raise ValueError(f'The configuration {self._path} is not valid: the JSON does not represent a list of dictionaries.')
                if not 'red' in entry:
                    raise ValueError(f'The configuration {self._path} is not valid: the quantity of red is not specified!')
                if not 'green' in entry:
                    raise ValueError(f'The configuration {self._path} is not valid: the quantity of green is not specified!')
                if not 'blue' in entry:
                    raise ValueError(f'The configuration {self._path} is not valid: the quantity of blue is not specified!')
                colors.append(Color(entry['red'], entry['green'], entry['blue']))
            return colors

More examples:

[Example Google style docstrings](https://gist.github.com/candlewill/fce04bb26d402288cd02f09bd4f5f562)

## Generating the documentation

* [Comparison of Python documentation generators](https://medium.com/@peterkong/comparison-of-python-documentation-generators-660203ca3804)

### PyDoc

Generate the documentation:

    pydoc -w /path/to/the/python/file

> Note that PyDoc produces a very basic documentation. **Use [Sphinx](http://www.sphinx-doc.org/en/master/index.html) instead**.


