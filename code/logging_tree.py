import logging
import os

PATH_FILE_LOG = os.path.join('/tmp', 'app.log')
SESSION = 'session'

# Create the top logger.

handler_std_a = logging.FileHandler(PATH_FILE_LOG, 'a')
handler_std_a.setLevel(logging.DEBUG)
handler_std_a.setFormatter(logging.Formatter(fmt='STD A-> %(asctime)s %(name)s %(levelname)s %(message)s',
                                             datefmt='%Y%m%d-%I%M%S'))

handler_secure_a = logging.FileHandler(PATH_FILE_LOG, 'a')
handler_secure_a.setLevel(logging.WARNING)
handler_secure_a.setFormatter(logging.Formatter(fmt='SEC A-> %(asctime)s %(name)s %(levelname)s %(message)s',
                                                datefmt='%Y%m%d-%I%M%S'))

loggerA = logging.getLogger('A')
loggerA.setLevel(logging.DEBUG)
loggerA.addHandler(handler_std_a)
loggerA.addHandler(handler_secure_a)

# Create other logger - A.B

handler_std_ab = logging.FileHandler(PATH_FILE_LOG, 'a')
handler_std_ab.setLevel(logging.DEBUG)
handler_std_ab.setFormatter(logging.Formatter(fmt='STD A.B-> %(asctime)s %(name)s %(levelname)s %(message)s',
                                              datefmt='%Y%m%d-%I%M%S'))

handler_secure_ab = logging.FileHandler(PATH_FILE_LOG, 'a')
handler_secure_ab.setLevel(logging.WARNING)
handler_secure_ab.setFormatter(logging.Formatter(fmt='SEC A.B-> %(asctime)s %(name)s %(levelname)s %(message)s',
                                                 datefmt='%Y%m%d-%I%M%S'))

loggerAB = logging.getLogger('A.B')
loggerAB.setLevel(logging.DEBUG)
loggerAB.addHandler(handler_std_ab)
loggerAB.addHandler(handler_secure_ab)

# Create other logger - A.C

handler_std_ac = logging.FileHandler(PATH_FILE_LOG, 'a')
handler_std_ac.setLevel(logging.DEBUG)
handler_std_ac.setFormatter(logging.Formatter(fmt='STD A.C-> %(asctime)s %(name)s %(levelname)s %(message)s',
                                              datefmt='%Y%m%d-%I%M%S'))

handler_secure_ac = logging.FileHandler(PATH_FILE_LOG, 'a')
handler_secure_ac.setLevel(logging.WARNING)
handler_secure_ac.setFormatter(logging.Formatter(fmt='SEC A.C-> %(asctime)s %(name)s %(levelname)s %(message)s',
                                                 datefmt='%Y%m%d-%I%M%S'))

loggerAC = logging.getLogger('A.C')
loggerAC.setLevel(logging.DEBUG)
loggerAC.addHandler(handler_std_ac)
loggerAC.addHandler(handler_secure_ac)

# Create other logger - A.B.C

handler_std_abc = logging.FileHandler(PATH_FILE_LOG, 'a')
handler_std_abc.setLevel(logging.DEBUG)
handler_std_abc.setFormatter(logging.Formatter(fmt='STD A.B.C-> %(asctime)s %(name)s %(levelname)s %(message)s',
                                               datefmt='%Y%m%d-%I%M%S'))

handler_secure_abc = logging.FileHandler(PATH_FILE_LOG, 'a')
handler_secure_abc.setLevel(logging.WARNING)
handler_secure_abc.setFormatter(logging.Formatter(fmt='SEC A.B.C-> %(asctime)s %(name)s %(levelname)s %(message)s',
                                                  datefmt='%Y%m%d-%I%M%S'))

loggerABC = logging.getLogger('A.B.C')
loggerABC.setLevel(logging.DEBUG)
loggerABC.addHandler(handler_std_abc)
loggerABC.addHandler(handler_secure_abc)

# Now, save messages / TEST 1

loggerABC.debug('TEST 1')
loggerABC.debug('debug[abc]')
loggerABC.info('info[abc]')
loggerABC.warning('warning[abc]')
loggerABC.error('error[abc]')
loggerABC.critical('critical[abc]')
loggerABC.debug('END TEST 1')

# Now, save messages / TEST 2

loggerABC.propagate = False

loggerABC.debug('TEST 2')
loggerABC.debug('debug[abc]')
loggerABC.info('info[abc]')
loggerABC.warning('warning[abc]')
loggerABC.error('error[abc]')
loggerABC.critical('critical[abc]')
loggerABC.debug('END TEST 2')

# Now, save messages / TEST 3

loggerABC.propagate = True
loggerAB.propagate = False

loggerABC.debug('TEST 3')
loggerABC.debug('debug[abc]')
loggerABC.info('info[abc]')
loggerABC.warning('warning[abc]')
loggerABC.error('error[abc]')
loggerABC.critical('critical[abc]')
loggerABC.debug('END TEST 3')


