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

This example above writes messages in a file with the following format:

    20190319-124623 aqszed R __main__ DEBUG This is an DEBUG message
    20190319-124623 aqszed R __main__ INFO This is an INFO message
    20190319-124623 aqszed R __main__ WARNING This is a WARNING message
    20190319-124623 aqszed R __main__ ERROR This is an ERROR message
    20190319-124623 aqszed R __main__ CRITICAL This is a CRITICAL message
    20190319-124623 aqszed L-09ef1a __main__ INFO bash-3.2%24%20python%20test2.py%0Asome%20text%20in%20single%20line%0AAs%20opposed%20to%0Asome%20text%0Awritten%20as%0Aheredoc%0Aand%2
    0then%20another%20single%20line
            # 09ef1a # bash-3.2$ python test2.py
            # 09ef1a # some text in single line
            # 09ef1a # As opposed to
            # 09ef1a # some text
            # 09ef1a # written as
            # 09ef1a # heredoc
            # 09ef1a # and then another single line



