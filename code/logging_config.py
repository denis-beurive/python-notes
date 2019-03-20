import logging.config
import os

# Create the configuration structure that describes the logging service.

config = {
    'version': 1,
    'formatters': {
        'low_priority': {
            'format': '%(asctime)s %(name)s %(levelname)s %(message)s',
            'datefmt': '%Y%m%d-%I%M%S'
        },
        'high_priority': {
            'format': 'URGENT %(asctime)s %(name)s %(levelname)s %(message)s',
            'datefmt': '%Y%m%d-%I%M%S'
        }
    },
    'handlers': {
        'standard': {
            'class': 'logging.FileHandler',
            'filename': '/tmp/standard.log',
            'level': 10, # DEBUG
            'formatter': 'low_priority'
        },
        'urgent': {
            'class': 'logging.FileHandler',
            'filename': '/tmp/urgent.log',
            'level': 30, # WARNING
            'formatter': 'high_priority'
        }
    },
    'loggers': {
        'high': {
            'level': 10, # DEBUG
            'handlers': ['urgent']
        },
        'high.low': {
            'level': 10,  # DEBUG
            'propagate': True,
            'handlers': ['standard']
        }
    }
}

# Apply the configuration.

logging.config.dictConfig(config)

# Get the loggers.

logger_low = logging.getLogger('high.low')
logger_high = logging.getLogger('high')

# Now let's LOG messages.

logger_low.debug('LOW debug')
logger_low.info('LOW info')
logger_low.warning('LOW warning')
logger_low.error('LOW error')
logger_low.critical('LOW critical')

logger_high.debug('HIGH debug')
logger_high.info('HIGH info')
logger_high.warning('HIGH warning')
logger_high.error('HIGH error')
logger_high.critical('HIGH critical')

