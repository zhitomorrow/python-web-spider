#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 21:54
# @Author  : lzm
# @File    : trans_word.py

import requests

from baidu_trans.my_config.application_parameter import params

"""
调用百度翻译接口，翻译关键词
"""


def trans_keyword(word):
    print(params)
    key = params['platform']['baidu']['key']
    appId = params['platform']['baidu']['appId']


trans_keyword('apple')
