#!/usr/bin/python
# -*- coding: utf-8 -*-
import jieba

from toy.utils.exception import *

def cut(content):
    word_list = jieba.lcut(content)
    word_num = len(word_list)
    word_str = ",".join(word_list)
    return word_str, word_num