import logging
import os
import os.path as p
from logging import basicConfig
from typing import Union

from concurrent_log_handler import ConcurrentRotatingFileHandler

from simplelog.utils.defaults import default_date_fmt
from simplelog.utils.defaults import default_log_fmt
# from simplelog.utils.json_log_formatter import JSONFormatter


basedir = p.dirname(p.dirname(p.abspath(__file__)))


class Logger:
    """
    Logger 配置中心, 这里主要进行logger的常用配置,
    配置完成后 可以通过 get_logger 方法来获取logger

    >>> from simplelog import Logger
    >>> logger = Logger().get_logger()

    """

    def __init__(self,
                 name=None,
                 filename=None,
                 log_fmt=None,
                 date_fmt=None,
                 backup_count=5,
                 max_bytes=1024 * 1024 * 100,
                 level=logging.INFO,
                 json_formatter=None,
                 ):
        """
        :param name: logger's name  日志的名称，如果不指定 有默认值 simple_log

        :param filename: 文件路径 '/aaa/bbb/file.log' ,日志文件的路径,如果没有提供这个值，
                         则不写入文件，直接输出日志 到控制台。

        :param log_fmt: 日志的格式 ,默认格式如下：
         [日期 时间  日志级别/进程号] logger的名称 文件名称 函数名:行号 打印日志内容
        [2020-03-09 18:02:21 INFO/39044] simplelog test_basic.py:<module>:14 hello world

        :param date_fmt: 日期的格式 ,使用指定的时间格式，默认格式 '%Y-%m-%d %H:%M:%S'

        :param backup_count: 对日志切割后 可以设置保留几份，默认保留5份

        :param max_bytes: 超过 max_bytes 将会陪切割，默认值:100M, 单位是 字节

        :param level: logging.INFO ,logging.DEBUG , 默认级别:INFO
                       日志级别参考logging 模块
                       CRITICAL = 50
                       FATAL = CRITICAL
                       ERROR = 40
                       WARNING = 30
                       WARN = WARNING
                       INFO = 20
                       DEBUG = 10

        :param json_formatter: josn_formatter class

        """
        self._name = name or 'simple_log'
        self.log_fmt = log_fmt if log_fmt is not None else default_log_fmt()
        self.filename = filename

        self.date_fmt = date_fmt if date_fmt is not None else default_date_fmt()
        self.backup_count = backup_count
        self.max_bytes = max_bytes
        self.json_formatter = json_formatter
        self.level = level
        self._log = None

        # init  log formatter
        if not self.json_formatter:
            basicConfig(
                format=self.log_fmt,
                datefmt=self.date_fmt,
                level=self.level,
            )
            self.formatter = logging.Formatter(self.log_fmt)
        else:
            self.formatter = self.json_formatter()


    def get_logger(self):
        log = logging.getLogger(self.name)

        # 定制handler ,maxBytes=1024 * 1024 * 100 = 100M
        if not self.filename:
            # 如果没有filename 不做切割就可以了,
            # 也不写入文件
            handler = logging.StreamHandler()
            handler.setFormatter(self.formatter)
            log.addHandler(handler)
            pass
        else:
            # 判断这个文件是否存在
            if not self.exists():
                self.touch()

            rotate_handler = ConcurrentRotatingFileHandler(filename=self.filename,
                                                           backupCount=self.backup_count,
                                                           maxBytes=self.max_bytes)
            rotate_handler.setFormatter(self.formatter)
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
        print(f"father_dir: {father_dir!r}")
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
    log = logging.getLogger(name or 'simple_log')
    log.setLevel(level=level)
