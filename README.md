# pysimple-log 

你还为 配置日志而烦恼吗？ 你还为一些不同的日志格式而痛苦吗？  那么现在来使用这个库吧。
这个库的目的简化 繁琐的日志配置，简单，省时。

## 概要
使用 logging 进行封装了一下 日志格式进行封装,
同时使用 concurrent_log_handler 来完成多进程安全的写日志

## 特性
- 对日志格式进行了默认格式的定义 
- 使用 concurrent_log_handler库来保证多进程写日志的安全性
- 对日志进行切割，防止日志太大，不利于查看文件
- 对日志切割后，可以设置保留几份



## 安装
Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

```bash 
pip install pysimple-log
```


## 快速开始   
```python

from simplelog import logger  

logger.info("this is test")
logger.error("this is test")
logger.warning("this is test")

```


## 定制化logger 
```python

    import logging
    from  simplelog import  Logger
    log = Logger(name='test',filename='app.log',level=logging.DEBUG)
    
    logger = log.get_logger()

    logger.debug("this is test")
    logger.warning("this is test")
    logger.info("this is test")
    logger.error("this is test")
    logger.exception("this is test")
```
结果如下:
```
[2020-03-06 22:53:57 WARNING/33060] test <input>:<module>:9 this is test
[2020-03-06 22:53:57 INFO/33060] test <input>:<module>:10 this is test
[2020-03-06 22:53:57 ERROR/33060] test <input>:<module>:11 this is test
[2020-03-06 22:53:57 ERROR/33060] test <input>:<module>:12 this is test
NoneType: None
```


## 高级的一些用法 
核心的类 [Logger](simplelog/utils/logger.py)  

参数介绍
```bash 

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
```
## 使用方法 
```python

    import logging
    from  simplelog import  Logger
    # 实例化 Logger 对象
    log = Logger(name='app',filename='app.log',level=logging.INFO)
    
    # 获取 logger 对象
    logger = log.get_logger()
    
    logger.info("hello world")
    logger.warning("hello world")
    logger.exception("hello world")
    logger.error("hello world")
```




## 设置 日志级别 set_level 
```python

    import logging
    from simplelog import Logger
    from simplelog import set_level
    # 实例化 Logger 对象
    log = Logger(name='app',filename='app.log',level=logging.INFO)
    
    #获取 logger 对象
    logger = log.get_logger()

    logger.debug('hello world 1')
    logger.info('hello world 2')
    logger.warning('hello world 3')
    logger.error('hello world 4')

    set_level(name=log.name,level=logging.WARNING)
    logger.debug('hello world 1')
    logger.info('hello world 2')
    logger.warning('hello world 3')
    logger.error('hello world 4')

    set_level(name=log.name,level=logging.ERROR)
    logger.debug('hello world 1')
    logger.info('hello world 2')
    logger.warning('hello world 3')
    logger.error('hello world 4')

```



## 捕获堆栈信息 设置 exc_info = True
```python
    
    import logging
    from simplelog import Logger
    # 实例化 Logger 对象
    log = Logger(name='app',filename='app.log',level=logging.INFO)

    logger = log.get_logger()
    # exc_info = True 
    logger.error("This is error ",exc_info=True)
```


## 输出json的格式的日志
```python
    import logging
    from simplelog import Logger,JSONFormatter
    # 实例化 Logger 对象
    log = Logger(name='app',level=logging.INFO,json_formatter=JSONFormatter)

    logger = log.get_logger()
    logger.propagate = False

    logger.info("hello world",extra={'key1':'hello world'})
    logger.warning("hello world")
    logger.exception("hello world")
    logger.error("hello world")
   ```






## 贡献
如果你对这个项目感兴趣，非常欢迎可以一起维护这个项目。
如果你在使用的过程发现什么问题,可以联系我。


## 链接 
- [pypi 地址](https://pypi.org/project/pysimple-log/)
- [pysimple-log github](https://github.com/changyubiao/pysimple-log)
- [作者邮箱](15769162764@163.com)  