#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 15:31
# @Author  : lzm
# @File    : urllib_request_exception.py

import socket
from urllib import request, error

'''
urllib的error模块定义了由request模块产生的异常，如果出现了问题，request模块便会抛出error模块中定义的异常
'''

# URLError
'''
URLError继承自OSError类，是error异常模块的基类，由request模块产生的异常都可以通过捕获这个类进行处理
'''

try:
    response = request.urlopen('https://www.52pojie.cn/thread-1067129213231221-1-1.html')
except error.URLError as e:
    print('异常原因：%s' % e.reason)

# HTTPError
'''
HTTPError是URLError的子类，专门用来处理HTTP请求错误，比如认证请求失败等。主要有三个属性：
code:HTTP状态码
reason:返回错误原因
headers:返回请求头
'''

# try:
#     response1 = request.urlopen('https://www.52pojie.cn/thread-1067129213231221-1-1.html')
# except error.HTTPError as e:
#     print('status=%s,reason=%s,headers=%s' % (e.code, e.reason,  e.headers))


'''
由于HTTPError是URLError的子类，捕获异常的时候基于从小到大的原则，可以将上述的代码进行修改
'''

try:
    response1 = request.urlopen('https://www.52pojie.cn/thread-1067129213231221-1-1.html')
except error.HTTPError as e:
    print('HTTPError:status=%s,reason=%s,headers=%s' % (e.code, e.reason, e.headers))
except error.URLError as e:
    print(e.reason)
else:  # else用来处理正常访问的逻辑
    print('Request Successful!!!')

'''
有时候reason返回的不是一个字符串，而是一个对象，此时就需要根据对象的类型进行处理
'''

try:
    response2 = request.urlopen('https://www.baidu.com', timeout=0.01)
except error.URLError as e:
    print(type(e.reason))  # <class 'socket.timeout'>
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
