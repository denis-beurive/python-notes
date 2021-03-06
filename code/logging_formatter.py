# This file shows how to implement a custom formatter.
#
# This formatter uses two specific tags:
# - session
# - linearized
#
# These tags are added to all lines that get appended to the LOG file.
#
# All messages that contain more than one line is linearised prior of
# being written to the LOG file.

import logging
import os
import uuid
from urllib.parse import quote, unquote

PATH_FILE_LOG = os.path.join('/tmp', 'basic.log')
SESSION = "aqszed"

# See https://docs.python.org/3.6/library/logging.html#formatter-objects

class MyFormatter(logging.Formatter):

    uid_prefix = 0

    # ------------------------------------------------------------
    # Overridden methods.
    # ------------------------------------------------------------

    # Please note that we introduce a parameter: "session"
    def __init__(self, fmt=None, datefmt=None, style='%', session: str=None):
        super().__init__(fmt=fmt, datefmt=datefmt, style=style)
        self.__session = session

    def formatTime(self, record, datefmt=None):
        return super().formatTime(record, datefmt=datefmt)

    def formatException(self, ei):
        return super().formatException(ei)

    def formatStack(self, stack_info):
        return super(stack_info)

    def format(self, record: logging.LogRecord) -> str:
        state = 'R'
        if -1 != record.msg.find("\n"):
            ui = __class__._get_message_id()
            state = f'L-{ui}'
            record.msg = __class__._encode_string(record.msg) + "\n" + __class__._indent_multiline_string(record.msg, ui)
        record.__setattr__('session', self.__session)
        record.__setattr__('linearized', state)
        return super().format(record) # The line that will be appended to the LOG file.

    # ------------------------------------------------------------
    # Specific methods.
    # ------------------------------------------------------------

    def set_session(self, session: set):
        self.__session = session

    @staticmethod
    def _encode_string(s: str) -> str:
        return quote(s)

    @staticmethod
    def _decode_string(s: str) -> str:
        return unquote(s)

    @staticmethod
    def _indent_multiline_string(s: str, message_id: str) -> str:
        return "\n".join(map(lambda x: f"\t# {message_id} # {x}", s.split("\n")))

    @staticmethod
    def _get_message_id() -> str:
        uid: str = str(__class__.uid_prefix) + uuid.uuid1().hex[0:5]
        __class__.uid_prefix += 1
        return uid


# Instantiate the formatter.
#
# Please note that we introduce two new tags:
# - session
# - linearized

formatter = MyFormatter(fmt='%(asctime)s %(session)s %(linearized)s %(name)s %(levelname)s %(message)s',
                        datefmt='%Y%m%d-%I%M%S',
                        session=SESSION)

# Instantiate a handler, and bind it to the formatter.

handler = logging.FileHandler(PATH_FILE_LOG)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

# Instantiate a logger and add the handler to it.

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# Then log messages.

logger.debug('This is an DEBUG message')
logger.info('This is an INFO message')
logger.warning('This is a WARNING message')
logger.error('This is an ERROR message')
logger.critical('This is a CRITICAL message')

message = """\
bash-3.2$ python test2.py
some text in single line
As opposed to
some text
written as
heredoc
and then another single line\
"""

logger.info(message)

