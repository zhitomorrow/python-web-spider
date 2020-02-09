#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 9:48
# @Author  : lzm
# @File    : request_params.py

import urllib.request
import urllib.parse
import urllib.error
import socket

'''
urlopen方法是可以携带参数的，主要的参数如下所示：
urllib.request.urlopen(url,data=None,[timeout,]*,cafile=None,capath=None,cadefault=False,context=Node)
data参数：data参数是可选的，如果要传递该参数，需要使用bytes()方法将参数转化为bytes类型，此时请求就不再是get请求，而是post请求
timeout参数：请求超时时间
cafile：指定CA证书
capath：指定的CA证书的路径
cadefault：弃用参数，默认是False
context：ssl.SSLContext类型，用来指定SSL设置
'''
try:
    params = {'word': 'hello'}
    data = bytes(urllib.parse.urlencode(params), encoding='utf8')
    # 0.1s会抛出urllib.error.URLError: <urlopen error timed out>异常，提示超时
    response = urllib.request.urlopen('http://httpbin.org/post', data=data, timeout=0.1)
    print(response.read().decode('utf8'))
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('异常原因：TIME OUT')



