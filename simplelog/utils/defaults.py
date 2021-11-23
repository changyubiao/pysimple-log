import os.path as p

# pysimple-log/simplelog
basedir = p.dirname(p.dirname(p.abspath(__file__)))


def default_log_fmt():
    log_fmt = '[%(asctime)s %(levelname)s/%(process)s] %(name)s %(filename)s:%(funcName)s:%(lineno)d %(message)s'

    return log_fmt


def default_filename():
    path = p.join(basedir, 'log/simple.log')
    return path


def default_date_fmt():
    date_fmt = '%Y-%m-%d %H:%M:%S'
    return date_fmt


if __name__ == '__main__':
    default_filename()
