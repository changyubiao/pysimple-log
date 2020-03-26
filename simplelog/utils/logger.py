# -*- coding: utf-8 -*- 
import logging
from logging import basicConfig
import os.path as p
import os
from typing import Union

from concurrent_log_handler import ConcurrentRotatingFileHandler

from simplelog.utils.defaults import default_log_fmt
from simplelog.utils.defaults import default_date_fmt

basedir = p.dirname(p.dirname(p.abspath(__file__)))


class Logger:

    def __init__(self,
                 name=None,
                 filename=None,
                 log_fmt=None,
                 date_fmt=None,
                 backup_count=5,
                 max_bytes=1024 * 1024 * 100,
                 level=logging.INFO
                 ):
        """
        :param name: logger's name
        :param filename:  文件路径 /aaa/bbb/file.log
        :param log_fmt: 日志的格式
        :param date_fmt: 日期的格式
        :param backup_count: default:5,保留几份日志
        :param max_bytes: default: 100M
        :param level: logging.INFO ,logging.DEBUG ,...
        """
        self._name = name or 'simple_log'
        self.log_fmt = log_fmt if log_fmt is not None else default_log_fmt()
        self.filename = filename

        self.date_fmt = date_fmt if date_fmt is not None else default_date_fmt()
        self.backup_count = backup_count
        self.max_bytes = max_bytes

        basicConfig(
            format=self.log_fmt,
            datefmt=self.date_fmt,
            level=level,
        )
        self._log = None

    def get_logger(self):
        log = logging.getLogger(self.name)
        formatter = logging.Formatter(self.log_fmt)
        # 定制handler ,maxBytes=1024 * 1024 * 100 = 100M
        if not self.filename:
            # 如果没有filename 不做切割就可以了,
            # 也不写入文件
            pass
        else:
            # 判断这个文件是否存在
            if not self.exists():
                self.touch()

            rotate_handler = ConcurrentRotatingFileHandler(filename=self.filename,
                                                           backupCount=self.backup_count,
                                                           maxBytes=self.max_bytes)
            rotate_handler.setFormatter(formatter)
            log.addHandler(rotate_handler)
        return log

    def exists(self):
        if p.exists(self.filename):
            return True
        else:
            return False

    def touch(self):
        """
        创建 日志文件路径
        :return:
        """
        father_dir = p.dirname(self.filename)
        print(f"father_dir: {father_dir}")
        try:
            os.makedirs(father_dir)
        except FileExistsError as e:
            print(f"file exists :{father_dir}"
                  f"- e:{e}")
        except FileNotFoundError as e:
            print(f"father_dir not exist: {father_dir!r}"
                  f"- e:{e}")

        with open(self.filename, 'w'):
            pass

    @property
    def name(self):
        return self._name

    def __call__(self, *args, **kwargs):
        return self.get_logger()


def set_level(name: str = None, level: Union[int, str] = logging.INFO):
    """
    Set the logging level of this logger.  level must be an int or a str.

    level 的可选值
    Union[ int, logging.INFO, logging.DEBUG, logging.ERROR, logging.WARNING]

    :param name: Logger 的 name ,默认值 simple_log
    :param level: 
    :return: None
    """
    # print("set level beginning....")
    log = logging.getLogger(name or 'simple_log')

    log.setLevel(level=level)
