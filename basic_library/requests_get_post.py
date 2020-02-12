#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 8:01
# @Author  : lzm
# @File    : requests_get_post.py

import requests

'''
requests的get请求
'''

base_url = 'http://httpbin.org/get'

# get请求附件请求参数
# 方法一
response = requests.get(base_url + '?name=Jerry&age=22')
print('方法一响应结果： %s ' % response.text)

# 方法二，将参数封装到一个字典中
params = {
    'name': 'Jerry',
    'age': 22
}

response = requests.get(base_url, params)
print('方法二响应结果： %s ' % response.text)

# 响应结果是json
'''
如果响应结果是json格式的，那么可以直接调用json()方法
'''

response = requests.get(base_url)
print('响应结果类型：%s ' % (type(response.text)))
print('响应结果： %s ' % (response.json()))
print(type(response.json()))

'''
响应结果类型：<class 'str'> 
响应结果： {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.22.0', 'X-Amzn-Trace-Id': 'Root=1-5e434222-a50c2fec4ade974413516778'}, 'origin': '111.194.44.100', 'url': 'http://httpbin.org/get'} 
<class 'dict'> 
可以发现，json()方法将JSON格式的字符串转换为字典
'''

# 响应结果是网页，那么直接返回html页面
# 响应结果是二进制数据（图片、视频）

response = requests.get('https://www.github.com/favicon.ico')
print(response.text)
print(response.content)
print(type(response.text))  # <class 'str'>
print(type(response.content))  # <class 'bytes'>
# 将文件写入到本地
# with open('favicon.ico', 'wb') as f:
#     f.write(response.content)

# 添加headers

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79.0.3945.88 Safari/537.36 '
}

response = requests.get('https://www.baidu.com', headers=headers)
print(response.text)


# post请求
data = {
    'name': 'Jerry',
    'age': 20
}
response = requests.post('https://httpbin.org/post', data)
print(response.text)
print(response.status_code)
print(response.headers)
print(response.cookies)
print(response.url)
print(response.history)

'''
200
{'Date': 'Wed, 12 Feb 2020 06:42:11 GMT', 'Content-Type': 'application/json', 'Content-Length': '500', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
<RequestsCookieJar[]>
https://httpbin.org/post
[]
'''

