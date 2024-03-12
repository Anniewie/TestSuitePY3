import logging

class Log():
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format = '%(asctime)s %(levelname)s %(message)s',
            datefmt = '%Y- %m- %d %H %M %S',
            filename = './../report/log/2024-03-12/test.log',
            filemode ='w'
        )

    def add_log(self, page, func, des):
        out_str = page + ':' + func + ':' + des
        logging.info(out_str)