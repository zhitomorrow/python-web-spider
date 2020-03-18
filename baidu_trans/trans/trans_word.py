#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 21:54
# @Author  : lzm
# @File    : trans_word.py

import requests
import random
import hashlib
import json

from baidu_trans.my_config.application_parameter import params

"""
调用百度翻译接口，翻译关键词
"""

# 需要翻译的语言有多种，因此采用auto的方式
from_language = 'auto'

# 翻译为中文
to_language = 'zh'

# 百度翻译api请求的url
trans_api_url = "http://api.fanyi.baidu.com/api/trans/vip/translate"


def trans_keyword(word):
    """
    调用百度翻译的接口，翻译相应的内容
    :param word:
    :return:
    """
    # print(params)
    key = params['platform']['baidu']['key']
    app_id = str(params['platform']['baidu']['appId'])
    # print('key==>%s' % key)
    # print('appId==>%s' % app_id)
    salt = random_num()
    sign = app_id + word + salt + key
    # print('sign==>%s' % sign)
    hash_md5 = hashlib.md5(sign.encode('utf-8'))
    sign = hash_md5.hexdigest()
    # print('sign==>%s' % sign)

    data = {
        'q': word,
        'from': from_language,
        'to': to_language,
        'appid': app_id,
        'salt': salt,
        'sign': sign
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(trans_api_url, headers=headers, data=data)
    # print('响应结果>>>>%s' % response.text)
    json_data = response.text
    # print(json_data)
    # print(type(json_data))
    text = json.loads(json_data)
    # print(type(text))
    # print(text['trans_result'][0]['dst'])
    return text['trans_result'][0]['dst']


def random_num():
    """
    获取10000到100000之间的随机整数
    :return:
    """
    return str(random.randint(10000, 100000))


# trans_keyword('apple')
