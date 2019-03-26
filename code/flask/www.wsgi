# This configuration file assumes that:
#
# [1] this file and the application source code ("www.py") are located within the same directory.
# [2] the Flask application is named "app" (in the application source code).
#     That is, it has been created this way: app = Flask(__name__)

import sys
import os

def set_python_search_path():
    local_directory = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, local_directory)

def activate_virtual_env():
    # echo "$(pipenv --venv)/bin/activate_this.py"
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

# Here, we load the application from the file "www.py".
from www import app as application

