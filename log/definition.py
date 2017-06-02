#!/usr/bin/env python

import logging
import logging.config
import os
import sys

File_path = os.getcwd()
LOGGING = {
    'basic': {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'simple': {
                'format': '%(asctime)s %(levelname)-8s [%(lineno)-4s] %(message)s',
                'datefmt': '%M:%S'
            },
            'verbose': {
                'format': '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)s] %(message)s',
                'datefmt': '%Y-%m-%dT%H:%M:%S'
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'delay': True,
                'filename': '%s/logs/basic.log'%File_path,
                'formatter': 'verbose'
            }
        },
        'loggers': {
            '': {
                'handlers': [
                    'console'
                ],
                'level': 'DEBUG'
            }
        }
    },
    'bdd': {
        'handlers': {
            'file': {
                'filename': '%s/logs/bdd_project.log'%File_path,
            }
        },
        'loggers': {
            '': {
                'handlers': [
                    'console',
                    'file'
                ]
            }
        }
    },
    'simple_scenario': {
        'handlers': {
            'file': {
                'filename': '%s/logs/simple_scenario.log'%File_path,
            }
        },
        'loggers': {
            '': {
                'handlers': [
                    'console',
                    'file'
                ]
            }
        }
    },
    'software_bdd': {
        'handlers': {
            'file': {
                'filename': '%s/logs/software_bdd.log'%File_path,
            }
        },
        'loggers': {
            '': {
                'handlers': [
                    'console',
                    'file'
                ]
            }
        }
    }
}

def _update_config(dst, src):
    for key in src:
        value = src[key]
        if type(value) == dict:
            _update_config(dst[key], value)
        else:
            dst[key] = value


def create_logger(name):

    # load basic configuration
    config = {}
    config.update(LOGGING['basic'])


    if name in LOGGING:
        _update_config(config, LOGGING[name])

    logging.config.dictConfig(config)

    return logging.getLogger('')


# if __name__ == "__main__":
#     loggerA = create_logger('bdd')
#     loggerA.error("log error")
#
#     loggerB = create_logger('software_bdd')
#     loggerB.error("log error 2")


