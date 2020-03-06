# pysimple-Log 
使用 logging 进行封装了一下 日志格式进行封装,
同时使用 concurrent_log_handler 来完成多进程安全的写日志


# 快速开始   
```python

from simplelog import logger  

logger.info("this is test")
logger.error("this is test")

```


# 定制化logger 
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
运行结果如下:
```
[2020-03-06 22:53:57 WARNING/33060] test <input>:<module>:9 this is test
[2020-03-06 22:53:57 INFO/33060] test <input>:<module>:10 this is test
[2020-03-06 22:53:57 ERROR/33060] test <input>:<module>:11 this is test
[2020-03-06 22:53:57 ERROR/33060] test <input>:<module>:12 this is test
NoneType: None
```

