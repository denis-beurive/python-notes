# Install pipenv

    pip install --user pipenv

The option tells `pip` to install `pipenv` into the home directory of the current user.

`pipenv` will be located under the following directory:

    ${HOME}/.local/bin/

Thus, set the user PATH environment variable accordingly (into `~/.bashrc`):

    export PATH="${HOME}/.local/bin/:${PATH}"

# Create a virtual environment for a project

    cd /the/project/directory
    pipenv install --python 3.6.4

> See [this link](https://pipenv.readthedocs.io/en/latest/) for all the available options.

This will create two new files, `Pipfile` and `Pipfile.lock`, in your project directory, and a new virtual environment for your project if it doesn’t exist already.

> Here, we specify that we want to use Python version `3.6.4` (instead of the default version of Python available on this host).

> This command assumes that `python 3.6.4` is already installed.

Once a virtual environment has been created for the project, we can activate it. See [Activate a virtual environment](#activate-a-virtual-environment).

# Activate a virtual environment

To activate a virtual environment bound to a project, go to the root directory of the project and run the command below:

    pipenv shell

Within this shell, all Python related commands will refer to the version of Python specified by the command `pipenv --python`.

# Get the path to the directory the contains a virtual environment configuration

    $ pipenv --venv
    /home/dev/.local/share/virtualenvs/tmp-SWmmaX4T

    $ ls /home/dev/.local/share/virtualenvs/tmp-SWmmaX4T
    bin  include  lib

As you can see, the directory contains all the "elements" that defines a Python environment.

# Get the path to the project associated with the current virtual environment

    (tmp) dev@unassigned-hostname:~/tmp$ pipenv --where
    /home/dev/tmp

# Get the list of environment variables use by pipenv

This command can be really useful.

    $ pipenv --envs
    The following environment variables can be set, to do various things:

      - PIPENV_IS_CI
      - PIPENV_CACHE_DIR
      - PIPENV_COLORBLIND
      - PIPENV_DEFAULT_PYTHON_VERSION
      - PIPENV_DONT_LOAD_ENV
      - PIPENV_DONT_USE_PYENV
      - PIPENV_DOTENV_LOCATION
      - PIPENV_EMULATOR
      - PIPENV_HIDE_EMOJIS
      - PIPENV_IGNORE_VIRTUALENVS
      - PIPENV_INSTALL_TIMEOUT
      - PIPENV_MAX_DEPTH
      - PIPENV_MAX_RETRIES
      - PIPENV_MAX_ROUNDS
      - PIPENV_MAX_SUBPROCESS
      - PIPENV_NO_INHERIT
      - PIPENV_NOSPIN
      - PIPENV_SPINNER
      - PIPENV_PIPFILE
      - PIPENV_PYPI_MIRROR
      - PIPENV_SHELL_EXPLICIT
      - PIPENV_SHELL_FANCY
      - PIPENV_TIMEOUT
      - PIPENV_VENV_IN_PROJECT
      - PIPENV_YES
      - PIPENV_SKIP_LOCK
      - PIPENV_PYUP_API_KEY
      - PIPENV_PYTHON
      - PIPENV_TEST_INDEX
      - PIPENV_USE_SYSTEM
      - PIPENV_VIRTUALENV
      - PIPENV_SKIP_VALIDATION
      - PIPENV_SHELL
      - PIPENV_VERBOSITY
      - PIPENV_SPINNER_FAIL_TEXT
      - PIPENV_SPINNER_OK_TEXT

    You can learn more at:
       http://docs.pipenv.org/advanced/#configuration-with-environment-variables

# Pipenv on a remote host with PyCharm (2018.3)

From within the project _virtual environment_ (`pipenv shell`), _on the remete host_, run the following command:

    (email) ...$ which python
    /home/dev/.local/share/virtualenvs/email-7PV48K4_/bin/python

This will give you the path to the Python interpreter used within that environment.

Then you specify the _absolute path_ to _this_ Python interpreter within the project interpreter settings (within PyCharm).

![Project interpreter settings](images/pycharm-project-interpreter-settings.png)

All the packages installed on the _remote environment_ (on the remote host) can be seen on the "project interpreter settings page". Thus, if you see these packages, then it means that PyCharm knows about them.

**However, it takes time for PyCharm to process these data and refresh the code being edited**. See [Cleaning System Cache](https://www.jetbrains.com/help/pycharm/cleaning-system-cache.html).

If you think that it takes too much time, then you can:

* Clean PyCharm cache. See [Cleaning System Cache](https://www.jetbrains.com/help/pycharm/cleaning-system-cache.html). Please note that this will take time...
* Hit "Refresh" on the "project interpreter settings page". If the "Refresh" link is not visible, then it means that there is nothing to refresh.

# Install a package

    pipenv install <name of the package>

Example:

    pipenv install pytest

# Uninstall a package

    pipenv uninstall crypto




