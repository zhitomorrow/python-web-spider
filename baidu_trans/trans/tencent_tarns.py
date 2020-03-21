#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 22:29
# @Author  : lzm
# @File    : tencent_tarns.py

import json
import requests
import time
import hashlib


# 腾讯翻译api地址
url = 'https://api.translator.qq.com/service/api'

app_id = 'xxx'

secretKey = 'xxx'


def time_stamp():
    """
    获取毫秒级别的时间戳，13位
    :return:
    """
    t = time.time()
    return str(round(t * 1000))


def tencent(keyword):
    _t = time_stamp()
    hash_md5 = hashlib.md5((app_id + secretKey + _t).encode('utf-8'))
    token = hash_md5.hexdigest()
    data = {
        'appId': app_id,
        "_t": _t,
        "token": token,
        'guid': '',
        'platform': 'PC',
        "action": "TextTranslate",
        "sourceText": keyword,
        "source": 'auto',
        "target": 'zh',
        "untranslatedText": ''
    }
    params = json.dumps(data)
    print('请求参数>>>>%s' % params)

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=params)
    json_data = response.text
    text = json.loads(json_data)
    return text['targetText']

