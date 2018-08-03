#!/usr/bin/python
# -*- coding: utf-8 -*-
import jieba

from toy.utils.timer import Timer
from toy.utils.exception import *
from toy.utils.logger import LoggerFactory

def cut(content, docid=None):
    log = LoggerFactory.getDebugLogger()
    with Timer() as t:
        word_list = jieba.lcut(content)
    log.info("docid:{}, Processing time for Jieba's cut is: {}".format(docid, t.elapse))

    word_num = len(word_list)
    word_str = ",".join(word_list)
    return word_str, word_num