# Logging

## Simple logging

    import logging
    import os

    PATH_FILE_LOG = os.path.join('/tmp', 'basic.log')
    SESSION = '1234'

    logging.basicConfig(filename=PATH_FILE_LOG,
                        level=logging.DEBUG,
                        # https://docs.python.org/3.6/library/logging.html#logrecord-attributes
                        format=f'%(asctime)s {SESSION} %(levelname)s %(message)s',
                        datefmt='%Y%m%d-%I%M%S')
    logging.debug('This is an DEBUG message')
    logging.info('This is an INFO message')
    logging.warning('This is a WARNING message')
    logging.error('This is an ERROR message')
    logging.critical('This is a CRITICAL message')

* List of all available message attributes: [message attributes](https://docs.python.org/3.6/library/logging.html#logrecord-attributes)
* List of all available configuration parameters: [configuration parameters](https://docs.python.org/3.6/library/logging.html#logging.basicConfig)

This example above writes messages in a file with the following format:

    20190318-104122 1234 DEBUG This is an DEBUG message
    20190318-104122 1234 INFO This is an INFO message
    20190318-104122 1234 WARNING This is a WARNING message
    20190318-104122 1234 ERROR This is an ERROR message
    20190318-104122 1234 CRITICAL This is a CRITICAL message

> This is good enough for simple uses. However, it may not be suitable for a production environment.

## Custom formatter

[This example](code/logging_formatter.py) shows how to build a custom formatter.

