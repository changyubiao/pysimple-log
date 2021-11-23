import time

import logging
from simplelog import Logger

logger = Logger(name='simplelog', filename='app.log',level=logging.DEBUG)

print(f"filename:{logger.filename}")

log = logger.get_logger()

for i in range(10):
    log.info("hello world")
    log.error("hello world")
    log.debug("hello world")
    try:
        a_list = list()
        b = a_list[10]
    except IndexError as e:
        log.exception(f"hello world "
                      f"-e:{e}")
    time.sleep(0.5)
