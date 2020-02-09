#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 9:37
# @Author  : lzm
# @File    : urllib_request.py

import urllib.request

response = urllib.request.urlopen("https://www.baidu.com/")
print(type(response))  # <class 'http.client.HTTPResponse'>

'''
http.client.HTTPResponse：
  包含read()、readinto()、gatheader(name)、getheaders()、fileno()等方法
  以及msg、version、status、reason、debuglevel、closed等属性
'''

# print(response.read().decode('utf-8'))

print(response.getheaders())

'''
[('Accept-Ranges', 'bytes'), ('Cache-Control', 'no-cache'), ('Content-Length', '227'), ('Content-Type', 'text/html'), ('Date', 'Sun, 09 Feb 2020 01:43:55 GMT'), ('P3p', 'CP=" OTI DSP COR IVA OUR IND COM "'), ('P3p', 'CP=" OTI DSP COR IVA OUR IND COM "'), ('Pragma', 'no-cache'), ('Server', 'BWS/1.1'), ('Set-Cookie', 'BD_NOT_HTTPS=1; path=/; Max-Age=300'), ('Set-Cookie', 'BIDUPSID=994AA44121F646CC64AB1EB1CCBCD495; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com'), ('Set-Cookie', 'PSTM=1581212635; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com'), ('Set-Cookie', 'BAIDUID=994AA44121F646CCF6E814EB8AA45254:FG=1; max-age=31536000; expires=Mon, 08-Feb-21 01:43:55 GMT; domain=.baidu.com; path=/; version=1; comment=bd'), ('Strict-Transport-Security', 'max-age=0'), ('Traceid', '158121263503800499309372477165181545560'), ('X-Ua-Compatible', 'IE=Edge,chrome=1'), ('Connection', 'close')]
'''

print('Content-Type:%s' % (response.getheader('Content-Type')))

print(response.status)

print(response.version)
