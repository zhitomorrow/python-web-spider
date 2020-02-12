#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 14:44
# @Author  : lzm
# @File    : requests_senior.py

import requests
import urllib3


'''
requests模块的高级用法
'''

# 文件上传
files = {
    'file': open('../README', 'rb')
}

response = requests.post('http://httpbin.org/post', files=files)
print(response.text)


# cookies
response = requests.get('https://www.baidu.com')
print(response.cookies)
for key, value in response.cookies.items():
    print(key+'='+value)

'''
<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
BDORZ=27315
'''

# 会话维持（session）
'''
使用requests的get()和post()方法模拟网页的请求时，多次请求是不同的会话，也就是相当于使用多个浏览器打开不同的网页。
虽然通过多次传递相同的cookies可以达到维持会话的目的，但是相对繁琐，可以通过Session对象维持同一个会话，并且不需要每次传递cookies
'''

requests.get('http://httpbin.org/cookies/set/number/12345678')
response = requests.get('http://httpbin.org/cookies')
print(response.text)
'''
上述的方式是无法获取到cookies的，响应结果如下：
{
  "cookies": {}
}
'''

# 使用session
session = requests.session()
session.get('http://httpbin.org/cookies/set/number/12345678')
response = session.get('http://httpbin.org/cookies')
print(response.text)
'''
响应结果：
{
  "cookies": {
    "number": "12345678"
  }
}
使用Sessions可以做到模拟同一个会话而不担心Cookies的问题，它通常用于模拟登陆成功之后再进行下一步的操作
'''

# SSL证书验证
'''
将verify参数设置为False时可以取消ssl验证
'''
urllib3.disable_warnings()  # 取消ssl验证时，如果不加这行会提示警告信息
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

'''
也可以指定一个本地证书作为SSL验证，指定cert参数的值，这个是可以是单个文件（包含秘钥和证书）或者一个包含两个文件路径的元组
'''
response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
print(response.status_code)

# 代理设置和超时设置
'''
不仅支持http代理，还支持socks协议代理，但是需要安装socks库，安装命令：pip3 install 'requests[socks]'
'''
proxies = {
    'http': 'http://127.0.0.1:6666',
    # 'http': 'socks5://127.0.0.1:9050',
    'https': 'http://127.0.0.1:8888'
}

requests.get('https://www.baidu.com', proxies=proxies, timeout=0.1)
