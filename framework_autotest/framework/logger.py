import logging
import os
import time


class Logger(object):

    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        time_name = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath('.')) + r'\logs\{}'.format(time_name) + '.log'
        # print(log_path)

        fh = logging.FileHandler(log_path, encoding='utf-8')
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger

# logs = Logger('test').get_log()
# logs.info('aaaaaa')
