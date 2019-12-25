import logging
# from logging.handlers import TimedRotatingFileHandler
# from concurrent_log_handler import ConcurrentRotatingFileHandler
# from cloghandler import ConcurrentRotatingFileHandler

import os
import sys

from concurrent_log_handler import ConcurrentRotatingFileHandler

log_file_name = 'log/app.log'

log_fmt = '[%(asctime)s %(levelname)s/%(process)s] %(name)s %(filename)s:%(funcName)s:%(lineno)d %(message)s'
_datefmt = '%Y-%m-%d %H:%M:%S'

logging.basicConfig(
    format=log_fmt,
    datefmt=_datefmt,
    level=logging.INFO,
)

source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if source_dir not in sys.path:
    print(
        f"logger_config.py source_dir :{source_dir}, {source_dir} will be added in sys.path")
    sys.path.append(source_dir)


def test_logger(name=None):
    logger.info(f'{name} this is  my first  hello world')
    logger.warning(f'{name} this is  my first  hello world')
    logger.error(f'{name} this is  my first  hello world')
    logger.exception(f'{name} this is  my first  hello world')


def get_clound_logger():
    log = logging.getLogger("atom_history_retriever")
    formatter = logging.Formatter(log_fmt)
    # 定制 handler      maxBytes=1024 * 1024 * 100  == 100M
    rotate_handler = ConcurrentRotatingFileHandler(filename=log_file_name,backupCount=5, maxBytes=1024 * 1024 * 100)
    rotate_handler.setFormatter(formatter)
    log.addHandler(rotate_handler)
    return log


logger = get_clound_logger()

if __name__ == "__main__":
    # logger = get_logger()
    # print(f"logger.handlers :{logger.handlers}")
    test_logger('frank111')
    pass
