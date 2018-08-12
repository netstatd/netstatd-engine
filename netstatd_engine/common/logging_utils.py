import logging


DEBUG = logging.DEBUG
logging.basicConfig()


def get_logger(name):
    return logging.getLogger(name)


def set_logger_level(logger, level=None):
    if level is None:
        level = logging.INFO
    logger.setLevel(level)
