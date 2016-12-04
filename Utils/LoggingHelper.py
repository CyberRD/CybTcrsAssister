#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import logging.config
import os


_path = os.path.dirname(os.path.abspath(__file__))
_path = os.path.join(_path, '..', 'logging.ini')
DEFAULT_LOG_CONFIG = os.path.abspath(_path)


def get_logger(file_name=DEFAULT_LOG_CONFIG, logger_name='root'):
    """
    Init logger. Default use INFO level. If 'DEBUG' is '1' in env use DEBUG level.
    :return:
    """
    logging.config.fileConfig(file_name)
    logger = logging.getLogger(logger_name)
    return logger
