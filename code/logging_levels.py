import os
import logging
import uuid
from urllib.parse import quote, unquote

LOG_FILE_STD = os.path.join('/tmp', 'std.log')
LOG_FILE_SECURE = os.path.join('/tmp', 'secure.log')

# Build a special formatter for high priority messages.

class HighPriorityFormatter(logging.Formatter):

    uid_prefix = 0

    # ------------------------------------------------------------
    # Overridden methods.
    # ------------------------------------------------------------

    # Please note that we introduce a parameter: "session"
    def __init__(self, fmt=None, datefmt=None, style='%', session: str=None):
        super().__init__(fmt=fmt, datefmt=datefmt, style=style)
        self.__session = session if session is not None else __class__._get_id()

    def formatTime(self, record, datefmt=None):
        return super().formatTime(record, datefmt=datefmt)

    def formatException(self, ei):
        return super().formatException(ei)

    def formatStack(self, stack_info):
        return super(stack_info)

    def format(self, record: logging.LogRecord) -> str:
        state = 'R'
        if -1 != record.msg.find("\n"):
            ui = __class__._get_id()
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
    def _get_id() -> str:
        uid: str = str(__class__.uid_prefix) + uuid.uuid1().hex[0:5]
        __class__.uid_prefix += 1
        return uid

# Handler for low priority messages (technical and functional messages).
# This handler will process all messages.

handler_low_priority = logging.FileHandler(LOG_FILE_STD)
handler_low_priority.setLevel(logging.DEBUG)
handler_low_priority.setFormatter(logging.Formatter(fmt='%(asctime)s %(name)s %(levelname)s %(message)s',
                                                    datefmt='%Y%m%d-%I%M%S'))

# Handler for high priority messages (alert and critical), and send them to the standard LOG file.
# This handler will process messages which levels are WARNING and above.

handler_high_priority = logging.FileHandler(LOG_FILE_STD)
handler_high_priority.setLevel(logging.WARNING)
handler_high_priority.setFormatter(HighPriorityFormatter(fmt='%(asctime)s %(name)s %(levelname)s URGENT %(message)s',
                                                         datefmt='%Y%m%d-%I%M%S'))

# Handler for high priority messages (alert and critical), and send them to the secure LOG file.
# This handler will process messages which levels are WARNING and above.

handler_secure = logging.FileHandler(LOG_FILE_SECURE)
handler_secure.setLevel(logging.WARNING)
handler_secure.setFormatter(HighPriorityFormatter(fmt='%(asctime)s %(name)s %(levelname)s SECURE %(message)s',
                                                  datefmt='%Y%m%d-%I%M%S'))

# Instantiate the logger.
#
# WARNING: Make sure to set the logger level (to the value DEBUG in this case).
#          **The logger level overwrites all handlers levels.**
#
#          For example:
#
#          If you don't set the logger level, then its level is set
#          to WARNING (by default). Even though "handler_low_priority" handler
#          level is DEBUG, it will not receive any messages. Indeed, all message
#          which level is less than WARNING will be rejected by the logger before they ever get to a handler.

logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler_low_priority)
logger.addHandler(handler_high_priority)
logger.addHandler(handler_secure)

logger.debug('low priority message 1')
logger.info('low priority message 2')
logger.warning('high priority message 1')
logger.error('high priority message 2')
logger.critical('high priority message 3')

