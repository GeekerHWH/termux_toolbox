import sys
import logging

def setup_logger(logger: logging.Logger):
    logger.setLevel(logging.DEBUG)
    stdout_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('[%(levelname)s %(filename)s:%(lineno)s] %(message)s')
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)
