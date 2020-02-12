#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 15:14
# @Author  : lzm
# @File    : requests_prepared_request.py

import requests

'''
在requests里，可以将请求封装成叫做Prepared Request的数据结构
'''

url = 'https://httpbin.org/post'
data = {
    'name': 'Tom',
    'age': 22
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79.0.3945.88 Safari/537.36 '
}

session = requests.session()
req = requests.Request('POST', url, data=data, headers=headers)
prepped = session.prepare_request(req)
response = session.send(prepped)
print(response.text)
