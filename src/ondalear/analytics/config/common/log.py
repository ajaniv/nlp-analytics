"""
.. module:: ondalear.core.log
   :synopsis: log module

"""
import os
import logging
from logging import config

from ondalear.analytics.config.common.root import CURRENT_ENV, LOCAL_ENV, DEV_ENV, LOG_DIR

LOG_LEVEL_INFO = 'INFO'
LOG_LEVEL_ERROR = 'ERROR'
LOG_LEVEL_DEBUG = 'DEBUG'

LOG_LEVEL = (LOG_LEVEL_DEBUG
             if CURRENT_ENV in (DEV_ENV, LOCAL_ENV)
             else LOG_LEVEL_INFO)

# create log directory if required
try:
    os.makedirs(LOG_DIR)
except OSError:
    if not os.path.isdir(LOG_DIR):
        raise

_verbose_format = ('%(asctime)s | %(levelname)s | %(process)d |' +
                   ' %(module)s | %(lineno)d | %(message)s ')

_simple_format = '%(levelname)s %(message)s'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': _verbose_format
        },
        'simple': {
            'format': _simple_format
        },
    },
    'filters': {
        'special': {
        }
    },
    'handlers': {
        'null': {
            'level': LOG_LEVEL_DEBUG,
            'class':'logging.NullHandler',
        },
        'console':{
            'level': LOG_LEVEL_DEBUG,
            'class':'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'log_file': {
            'level': LOG_LEVEL_DEBUG,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'analytics.log'),
            'maxBytes': 16777216,  # 16megabytes
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'ondalear.analytics': {
            'handlers': ['console', 'log_file'],
            'level': LOG_LEVEL_INFO
        },
        'allennlp': {
            'handlers': ['console', 'log_file'],
            'level': LOG_LEVEL_INFO
        }
    }
}

def initialize(configuration=None):
    """Initialize logging"""
    if not initialize.has_run:
        configuration = configuration or LOGGING
        config.dictConfig(configuration)
        logger = logging.getLogger(__name__)
        logger.info('logging initialized')
    initialize.has_run = True
initialize.has_run = False
