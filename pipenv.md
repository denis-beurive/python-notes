# Install

    pip install --user pipenv

The option tells `pip` to install `pipenv` into the home directory of the current user.

`pipenv` will be located under the following directory:

    ${HOME}/.local/bin/

Thus, set the user PATH environment variable accordingly (into `~/.bashrc`):

    export PATH="${HOME}/.local/bin/:${PATH}"

# Set the version of Python to use

This command below creates a virtual environment (_virtualenv_) for a project. Go the  root directory of the project and run:

    pipenv --python 3.6.4

> This command assumes that `python 3.6.4` is already installed.

Once a virtual environment has been created for the project, we can activate it. See [Activate a virtual environment](#activate-a-virtual-environment).

# Activate a virtual environment

To activate a virtual environment bound to a project, go to the root directory of the project and run the command below:

    pipenv shell

Within this shell, all Python related commands will refer to the version of Python specified by the command `pipenv --python`.

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






