# -*- coding: utf-8 -*- 

import multiprocessing
import time

from simplelog import logger


def worker(interval=1):
    n = 10
    while n > 0:
        for i in range(100):
            logger.info("The time:{0!r}. i={1}".format(time.ctime(), i))  # 输出时间的格式
        time.sleep(interval)
        n -= 1


def main():
    process_list = []

    for _ in range(10):
        p = multiprocessing.Process(target=worker, args=(1,))
        p.start()
        process_list.append(p)

        logger.info(f"pid:{p.pid} "
                    f"-pname:{p.name} "
                    f"-p is alive :{p.is_alive()} ")

    for p in process_list:
        p.join()


def test_log():
    for i in range(50):
        time.sleep(0.2)
        logger.info(f"=== All task done === i:{i}")


if __name__ == "__main__":
    main()
