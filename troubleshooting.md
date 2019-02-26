# Troubleshooting

## Check whether a package is installed or not

    python -c 'help("modules")' | grep <name of the package>

Or, for example:

    (email) ...$ find "$(pipenv --venv)/lib" -name "*pytest*"

## Pipenv: locking failed!

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


