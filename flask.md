# Flask



## Setup Flask with Apache

This section shows how to use Flask with an Apache server.

See [this documentation](http://flask.pocoo.org/docs/1.0/deploying/mod_wsgi/).

### Install the WSGI apache module

#### Introduction

The Apache module `mod_wsgi.so` is "hard linked" with the shared library that contains the Apache interpreter. This means that **if you need Python 3.6.4, then you need a version of the module `mod_wsgi.so` that has been compiled against this specific version of Python (3.6.4)**. See [this document](https://modwsgi.readthedocs.io/en/develop/user-guides/virtual-environments.html#virtual-environment-and-python-version) for details.

> When using a Python virtual environment with mod_wsgi, it is very important that it has been created using the same Python installation that mod_wsgi was originally compiled for. It is not possible to use a Python virtual environment to force mod_wsgi to use a different Python version, or even a different Python installation.
>
> You cannot for example force mod_wsgi to use a Python virtual environment created using Python 3.5 when mod_wsgi was originally compiled for Python 2.7. **This is because the Python library for the Python installation it was originally compiled against is linked directly into the mod_wsgi module. In other words, Python is embedded within mod_wsgi**. When mod_wsgi is used it does not run the command line python program to run the interpreter and thus why **you can’t force it to use a different Python installation**.

#### Installation from the Debian repository

##### Warning

This way of installing the WSGI module may not be compatible with your specific environment. Debian only provides precompiled versions of the `mod_wsgi.so` module for two versions of Python. If your specific need does not fit into these two versions, then you need to recompile the module `mod_wsgi.so`.

##### Python 2

    apt-get install libapache2-mod-wsgi

Make sure that the module is installed:

    # apache2ctl -t -D DUMP_MODULES | grep wsgi_module
    wsgi_module (shared)

Check the version of python that is compiled within "`mod_wsgi`"

    # cat /etc/apache2/mods-available/wsgi.load 
    LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so

    # ls -l /usr/lib/apache2/modules/mod_wsgi.so
    lrwxrwxrwx 1 root root 15 Dec 29  2016 /usr/lib/apache2/modules/mod_wsgi.so -> mod_wsgi.so-2.7

> The module uses Python 2.7. If you need another version of Python, then you may have to recompile the module.

##### Python 3

    apt-get install libapache2-mod-wsgi-py3

Make sure that the module is installed:

    # apache2ctl -t -D DUMP_MODULES | grep wsgi_module
    wsgi_module (shared)

Check the version of python that is compiled within "`mod_wsgi`"

    # cat /etc/apache2/mods-available/wsgi.load
    LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so

    # ls -l /usr/lib/apache2/modules/mod_wsgi.so
    lrwxrwxrwx 1 root root 15 Dec 29  2016 /usr/lib/apache2/modules/mod_wsgi.so -> mod_wsgi.so-3.5

> The module uses Python 3.5. If you need another version of Python, then you may have to recompile the module.

#### Recompile mod_wsgi

##### Prerequisites

Eventually:

    apt-get remove libapache2-mod-wsgi

    or

    apt-get remove libapache2-mod-wsgi-py3

Very important:

* Make sure that Python has been compiled with the configuration option `--enable-shared`.
* Make sure that all the _development files_ have been installed (header files, libraries...).

**Note**: to check that the _development files_ are installed, you can execute the command below:

    # find / -name "Python.h"
    /usr/local/include/python3.6m/Python.h

    # find / -name libpython3.6m.so.1.0 
    /usr/local/lib/libpython3.6m.so.1.0

If Python has not been compiled with the configuration option `--enable-shared`, or if the _development files_ are not available, then recompile it:

    sudo apt-get update && sudo apt-get upgrade
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev
    sudo apt-get install -y libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm
    sudo apt-get install -y libncurses5-dev  libncursesw5-dev xz-utils tk-dev

    wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz
    tar xvf Python-3.6.4.tgz
    cd Python-3.6.4
    ./configure --enable-optimizations --enable-shared
    make -j8
    sudo make altinstall

> `make altinstall` should install the _development files_ (see the `Makefile`).

##### Compilation

Read [this document](https://github.com/GrahamDumpleton/mod_wsgi).

Test if MPM is used:

    # apache2ctl -t -D DUMP_MODULES | grep mpm
    mpm_event_module (shared)

Install the required dependencies:

    apt-get install apache2-dev

Download the source:

    wget https://github.com/GrahamDumpleton/mod_wsgi/archive/develop.zip
    unzip develop.zip

Set the compiler options used by the compiler:

    export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib
    export C_INCLUDE_PATH=${C_INCLUDE_PATH}:/usr/local/include/python3.6m/

> Refer to the section "prerequisites" to find out the values to set. Please note that you may not need to configure the environment.

Then compile "`mod_wsgi`":

    cd /mod_wsgi-develop
    ./configure --with-python=python3.6
    make
    make install

If all goes well, then you should get:

    libtool: install: install src/server/.libs/mod_wsgi.so /usr/lib/apache2/modules/mod_wsgi.so
    libtool: install: install src/server/.libs/mod_wsgi.lai /usr/lib/apache2/modules/mod_wsgi.la
    libtool: finish: PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/sbin" ldconfig -n /usr/lib/apache2/modules
    ----------------------------------------------------------------------
    Libraries have been installed in:
       /usr/lib/apache2/modules

    If you ever happen to want to link against installed libraries
    in a given directory, LIBDIR, you must either use libtool, and
    specify the full pathname of the library, or use the '-LLIBDIR'
    flag during linking and do at least one of the following:
       - add LIBDIR to the 'LD_LIBRARY_PATH' environment variable
         during execution
       - add LIBDIR to the 'LD_RUN_PATH' environment variable
         during linking
       - use the '-Wl,-rpath -Wl,LIBDIR' linker flag
       - have your system administrator add LIBDIR to '/etc/ld.so.conf'

    See any operating system documentation about shared libraries for
    more information, such as the ld(1) and ld.so(8) manual pages.
    ----------------------------------------------------------------------
    chmod 644 /usr/lib/apache2/modules/mod_wsgi.so

Make sure that the Apache module is installed:

    # ls -l /usr/lib/apache2/modules/mod_wsgi.so
    -rw-r--r-- 1 root root 1104784 Mar 25 14:48 /usr/lib/apache2/modules/mod_wsgi.so

Restart Apache:

    /usr/sbin/apachectl -S && /usr/sbin/apachectl configtest && service apache2 restart && echo "OK"

Make sure that the Apache module is enabled:

    # apache2ctl -t -D DUMP_MODULES | grep wsgi_module
    wsgi_module (shared)

Then you should check that python works fine (with a non-root user):

    $ python3.6 --version
    Python 3.6.4

##### Troubleshooting

If the compiler cannot find a header file:

    echo "${C_INCLUDE_PATH}"

If Python cannot load a shared library, then make sure that the path to the directory that contains this library is declared:

    echo "${LD_LIBRARY_PATH}"
    ldconfig -v

> See [this link](http://blog.andrewbeacock.com/2007/10/how-to-add-shared-libraries-to-linuxs.html).

### Create a WSGI aplication loader

Create a Python file that will be used to load the Flask application.

Let's say that:

* `thermo.py` is the application source code.
* `thermo.wsgi` is the application loader.
* these two files are located into the same directory "`www`".

    www
    ├── thermo.py
    └── thermo.wsgi

Then, the code of the application loader looks like:

    # This configuration file assumes that:
    #
    # [1] this file and the application source code ("thermo.py") are located within the same directory.
    # [2] the Flask application is named "app" (in the application source code).
    #     That is, it has been created this way: app = Flask(__name__)
    #
    # If you are using PyCharm, then you should add the path to the directory that contains the application source code to
    # "PYTHONPATH".

    import sys
    import os

    def set_python_search_path():
        local_directory = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, local_directory)

    def activate_virtual_env():

        # $ find ~/ -name "activate_this.py"
        # /home/thermo/.local/share/virtualenvs/thermo_test-IVHwWUHZ/bin/activate_this.py

        activator = '/home/thermo/.local/share/virtualenvs/thermo_test-IVHwWUHZ/bin/activate_this.py'
        with open(activator) as f:
            exec(f.read(), {'__file__': activator})

    def debug():
        local_directory = os.path.dirname(os.path.abspath(__file__))
        log_path = os.path.join(local_directory, 'wsgi.trace')
        with open(log_path, 'w') as fd:
            fd.write("Python version = %s\n" % sys.version_info[0])
            fd.write("Python search paths = %s\n" % ', '.join(sys.path))

    activate_virtual_env()
    set_python_search_path()
    debug()

    from thermo import app as application

> **Note 1**: by convention, the file name end with the suffix "`.wsgi`" (ex: `thermo.wsgi`). However, this is only a convention and you could give this file any name you want.

> **Note 2**: as you can see, the file that contains the source code of the (Flask) application (`thermo.py`) is considered by the WSGI loader to be a Python module - `thermo` (within the package `www`). Thus you must configure the Python module loader so that it finds the module to load (`thermo`).

### Create a virtual host

First create the virtual host configuration file `/etc/apache2/sites-available/thermo.conf`:

    <VirtualHost *:80>
        ServerName example.ddns.net
        ServerAlias www.example.ddns.net

        WSGIDaemonProcess thermo user=thermo group=thermo threads=5
        WSGIScriptAlias / /home/thermo/projects/thermo_test/www/thermo.wsgi

        <Directory /home/thermo/projects/thermo_test/www>
            WSGIProcessGroup thermo
            WSGIApplicationGroup %{GLOBAL}
            Require all granted
        </Directory>
    </VirtualHost>

Please note:

* **The path to the WSGI loader**: `/home/thermo/projects/thermo_test/www/thermo.wsgi`
* **The user that will execute the application**: `user=thermo group=thermo`

Then:

Activate the configuration:

    sudo a2ensite thermo.conf

Check the Apache configuration:

    sudo /usr/sbin/apachectl configtest
    sudo /usr/sbin/apachectl -S

Reload the configuration:

    sudo service apache2 reload && echo "OK"

Test the configuration. If an error occurs, then you can usually find out what's wrong by looking at the Apache LOG files:

    sudo tail -f /var/log/apache2/access.log /var/log/apache2/error.log /var/log/apache2/other_vhosts_access.log

Error message:

    ==> /var/log/apache2/error.log <==
    [Mon Mar 25 10:32:39.638399 2019] [core:error] [pid 30187:tid 139887059617536] (13)Permission denied: [client 170.140.220.100:56168] AH00035: access to /log denied (filesystem path '/home/thermo/projects/thermo_test/www') because search permissions are missing on a component of the path

This means that somewhere within the directory tree that leads to the WSGI application loader (`thermo.wsgi`) or to the application file (`thermo.py`), a directory does not have the required permission. The command `chmod -R 0755 /path` should solve the problem.

Error message:

    ==> /var/log/apache2/error.log <==
    [Mon Mar 25 10:41:50.390820 2019] [wsgi:error] [pid 30186:tid 139887219422976] [remote 170.140.220.100:56182] Traceback (most recent call last):
    [Mon Mar 25 10:41:50.390865 2019] [wsgi:error] [pid 30186:tid 139887219422976] [remote 170.140.220.100:56182]   File "/home/thermo/projects/thermo_test/www/thermo.wsgi", line 23, in <module>
    [Mon Mar 25 10:41:50.390978 2019] [wsgi:error] [pid 30186:tid 139887219422976] [remote 170.140.220.100:56182]     from thermo import app as application
    [Mon Mar 25 10:41:50.391016 2019] [wsgi:error] [pid 30186:tid 139887219422976] [remote 170.140.220.100:56182] ImportError: No module named thermo

This means that the Python search path is not well configured. Focus on these instructions:

    local_directory = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, local_directory

Error message:

    ==> /var/log/apache2/error.log <==
    [Mon Mar 25 15:07:52.252113 2019] [wsgi:error] [pid 31897:tid 140626163910400] [remote 176.144.220.100:57360] mod_wsgi (pid=31897): Failed to exec Python script file '/home/thermo/projects/thermo_test/www/thermo.wsgi'.
    [Mon Mar 25 15:07:52.252705 2019] [wsgi:error] [pid 31897:tid 140626163910400] [remote 176.144.220.100:57360] mod_wsgi (pid=31897): Exception occurred processing WSGI script '/home/thermo/projects/thermo_test/www/thermo.wsgi'.
    [Mon Mar 25 15:07:52.253293 2019] [wsgi:error] [pid 31897:tid 140626163910400] [remote 176.144.220.100:57360] Traceback (most recent call last):
    [Mon Mar 25 15:07:52.253598 2019] [wsgi:error] [pid 31897:tid 140626163910400] [remote 176.144.220.100:57360]   File "/home/thermo/projects/thermo_test/www/thermo.wsgi", line 27, in <module>
    [Mon Mar 25 15:07:52.253846 2019] [wsgi:error] [pid 31897:tid 140626163910400] [remote 176.144.220.100:57360]     from thermo import app as application
    [Mon Mar 25 15:07:52.254085 2019] [wsgi:error] [pid 31897:tid 140626163910400] [remote 176.144.220.100:57360]   File "/home/thermo/projects/thermo_test/www/thermo.py", line 18, in <module>
    [Mon Mar 25 15:07:52.254333 2019] [wsgi:error] [pid 31897:tid 140626163910400] [remote 176.144.220.100:57360]     from flask import Flask, request
    [Mon Mar 25 15:07:52.254587 2019] [wsgi:error] [pid 31897:tid 140626163910400] [remote 176.144.220.100:57360] ModuleNotFoundError: No module named 'flask'

This means that the virtual environment is not activated. You need to find the file "`activate_this.py`" that activates the environment:

    $ find ~/ -name "activate_this.py"
    /home/thermo/.local/share/virtualenvs/thermo_test-IVHwWUHZ/bin/activate_this.py

Then you need to load this file from the WSGI application loader:

    activator = '/home/thermo/.local/share/virtualenvs/thermo_test-IVHwWUHZ/bin/activate_this.py'
    with open(activator) as f:
        exec(f.read(), {'__file__': activator})


