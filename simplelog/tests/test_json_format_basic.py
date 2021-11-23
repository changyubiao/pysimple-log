# -*- coding: utf-8 -*- 
import logging
import time

from simplelog import Logger, JSONFormatter

log_config = Logger(name='test_log',
                    filename=r'app.log',
                    level=logging.DEBUG,
                    json_formatter=JSONFormatter)


def test_json_format_basic():
    print(f"filename:{log_config.filename}")

    log = log_config.get_logger()
    log.propagate = False

    log.info('this is a test log.',extra={'key1':'hahaha'})
    for i in range(1):
        log.info("hello world")
        log.error("hello world")
        log.debug("hello world")
        try:
            a_list = list()
            b = a_list[10]
        except IndexError as e:
            log.exception(f"hello error "
                          f"-e:{e}")
        time.sleep(0.5)


if __name__ == '__main__':
    test_json_format_basic()
    # filename = r'app.log'
    # with open(filename, 'w') as f:
    #     f.write(
    #         'hello frank'
    #     )
    pass