pysimple-Log
=============

概要
----
使用系统库logging 进行封装了一下日志格式进行封装,
同时使用 concurrent_log_handler来完成多进程安全的写日志。


安装
----
Install and update using `pip`_ :

.. code-block::python

    pip install  pysimple-log


快速开始
--------

.. code-block::python

    from simplelog import logger

    logger.info("this is test")
    logger.error("this is test")


定制化logger
------------
.. code-block::python

    import logging
    from  simplelog import  Logger
    log = Logger(name='test',filename='app.log',level=logging.DEBUG)
    
    logger = log.get_logger()

    logger.debug("this is test")
    logger.warning("this is test")
    logger.info("this is test")
    logger.error("this is test")
    logger.exception("this is test")


结果如下:

    [2020-03-06 22:53:57 WARNING/33060] test <input>:<module>:9 this is test
    [2020-03-06 22:53:57 INFO/33060] test <input>:<module>:10 this is test
    [2020-03-06 22:53:57 ERROR/33060] test <input>:<module>:11 this is test
    [2020-03-06 22:53:57 ERROR/33060] test <input>:<module>:12 this is test
    NoneType: None


贡献
----
如果你对这个项目感兴趣，非常欢迎可以一起维护这个项目。
如果你在使用的过程发现什么问题，可以联系我。


.. _pip: https://pip.pypa.io/en/stable/quickstart/
