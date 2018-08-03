#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml
import logging
import logging.config
import logging.handlers
from functools import lru_cache


class LoggerFactory(object):

    # -----------------------------------------------------
    # Disabled Constructor
    # -----------------------------------------------------

    def __init__(self):
        assert False, 'LoggerFactory can not be initialized.'

    # -----------------------------------------------------
    # Factory Methods
    # -----------------------------------------------------

    @staticmethod
    @lru_cache(maxsize=1)
    def getDebugLogger():
        logger = LoggerFactory._getLogger('debug')
        return logger

    @staticmethod
    @lru_cache(maxsize=1)
    def getProdLogger():
        logger = LoggerFactory._getLogger('prod')
        return logger

    @staticmethod
    def getWrappedLogger(docid):
        logger = LoggerFactory._getLogger('wrapped')
        f = _ContextFilter(docid)
        logger.addFilter(f)
        return logger

    # -----------------------------------------------------
    # Private Functions
    # -----------------------------------------------------

    @staticmethod
    def _getLogger(name):
        # Use customized logger
        logging.setLoggerClass(_CustomExtraLogger)
        # Load config
        conf = open('../conf/logging.conf', 'r')
        logging.config.dictConfig(yaml.load(conf))
        conf.close()
        # Get logger by name
        logger = logging.getLogger(name)
        return logger


class _CustomExtraLogger(logging.Logger):

    EXTRA = {'app': 'toyapi'}

    def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False):
        if extra is None:
            extra = self.EXTRA
        super(_CustomExtraLogger, self)._log(level, msg, args, exc_info, extra, stack_info)


class _ContextFilter(logging.Filter):
    """ _ContextFilter automatic wrap record doc_id,  task_label_setting_id and industry """

    def __init__(self, docid):
        super().__init__()
        self.docid = docid

    def filter(self, record):
        record.docid = self.docid
        return True

if __name__ == '__main__':
    print(_ContextFilter(1).name)