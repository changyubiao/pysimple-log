# -*- coding: utf-8 -*-
"""
pysimple-log
------
pysimple-log for every project in log record simply.

Basic Usage:

    >>> from simplelog import logger
    >>> logger.info('hello')
    [2020-03-06 22:29:01 INFO/33060] simple_log <input>:<module>:1 hello
    >>> logger.error('hello world')
    [2020-03-06 22:30:06 ERROR/33060] simple_log <input>:<module>:1 hello world
    >>> logger.exception('hello world')
    [2020-03-06 22:30:15 ERROR/33060] simple_log <input>:<module>:1 hello world
    NoneType: None
    >>> logger.exception('hello world')
    [2020-03-06 22:30:36 ERROR/33060] simple_log <input>:<module>:1 hello world
    NoneType: None
    >>> logger.error('hello world')
    [2020-03-06 22:30:38 ERROR/33060] simple_log <input>:<module>:1 hello world

"""

import os.path as p
from simplelog.utils.logger import Logger

# basedir=simplelog
basedir = p.dirname(p.abspath(__file__))

__author__ = 'Frank.chang'
__author_email__ = 'frank.chang@lexisnexis.com'

__version__ = '0.0.2'

logger = Logger().get_logger()

if __name__ == '__main__':
    print(basedir)
