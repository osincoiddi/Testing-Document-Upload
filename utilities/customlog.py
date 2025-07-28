import logging
import os
from logging import basicConfig

class LogGen:
    @staticmethod
    def loggen():
        path=os.path.abspath(os.curdir)+ '\\logs\\automation.log\\'
        logging.basicConfig(filename=path,
                            format= '%(asctime)s:%(levelname)s:%(message)s',datefmt="%Y-%m-%d %H:%M:%S")
        logger=logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
