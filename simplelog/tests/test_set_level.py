# -*- coding: utf-8 -*- 

import logging
from simplelog import Logger, set_level

logger = Logger().get_logger()

print('line:19 ======info ======')

set_level(name=logger.name, level=logging.INFO)
logger.debug('hello frank1')
logger.info("hello world 2")
logger.warning('hello  frank3')
logger.error('hello frank 4')


print('line:19 ======debug ======')
set_level(name=logger.name, level=logging.DEBUG)
logger.debug('hello frank1')
logger.info("hello world 2")
logger.warning('hello  frank3')
logger.error('hello frank 4')
print('line:20 ====== warning ======')

set_level(level=logging.WARNING)
logger.debug('hello frank1')
logger.info("hello world 2")
logger.warning('hello  frank3')
logger.error('hello frank 4')

if __name__ == '__main__':
    pass
