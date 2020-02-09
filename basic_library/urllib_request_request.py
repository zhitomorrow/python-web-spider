#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 15:59
# @Author  : lzm
# @File    : urllib_request_request.py

from urllib import request, parse


'''
urlopen()方法可以实现简单的http请求，但是参数较少，不满足构建完整请求的需求，比如需要传递headers，此时可以使用Request类来构建，将Request对象传递给urlopen方法
urllib.request.Request(url,data=None,headers={},origin_req_host=None,unverifiable=False,method=None)
url:必传参数
data:必须是bytes类型的
headers:请求头，字典类型。还可以通过调用请求实例的add_header()方法添加
method:请求的方法，get/post/put
'''

# req = request.Request('http://httpbin.org')
# response = request.urlopen(req)
# print(response.read().decode('utf8'))


url = 'http://httpbin.org/post'
headers = {
    'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/79.0.3945.88 Safari/537.36',
    'Host': 'httpbin.org'
}
params = {
    'name': 'Jack'
}

data = bytes(parse.urlencode(params), encoding='utf8')
req = request.Request(url, data=data, headers=headers, method='POST')
req.add_header('Accept-Language', 'zh-CN,zh;q=0.9')
response = request.urlopen(req)
print('响应结果: %s' % (response.read().decode('utf-8')))




