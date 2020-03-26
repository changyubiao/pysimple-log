# -*- coding: utf-8 -*- 

import logging
from simplelog import Logger, set_level

log = Logger(name='test_log')

logger = log.get_logger()

print(f"log.name:{log.name}")
print('line:11 ======debug ======')
set_level(name=log.name, level=logging.DEBUG)
logger.debug('hello frank1')
logger.info("hello world 2")
logger.warning('hello  frank3')
logger.error('hello frank 4')

print('line:18 ======info ======')
set_level(name=log.name, level=logging.INFO)
logger.debug('hello frank 1')
logger.info("hello world 2")
logger.warning('hello frank 3')
logger.error('hello frank 4')

print('line:25 ====== warning ======')
set_level(name=log.name, level=logging.WARNING)
logger.debug('hello frank 1')
logger.info("hello world 2")
logger.warning('hello frank 3')
logger.error('hello frank 4')

print('line:32 ====== error ======')
set_level(name=log.name, level=logging.ERROR)
logger.debug('hello frank 1')
logger.info("hello world 2")
logger.warning('hello frank 3')
logger.error('hello frank 4')

