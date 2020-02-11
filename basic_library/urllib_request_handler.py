#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 14:59
# @Author  : lzm
# @File    : urllib_request_handler.py

from urllib.error import URLError
import urllib.request
import http.cookiejar

'''
对于request，当需要设置cookie、代理等更高级的操作时，此时需要更强大的工具Handler。
Handler有专门处理登陆验证的、有处理Cookies的、有处理代理设置的，利用这些处理器，我们几乎可以做到HTTP请求中的所有的事情
HTTPDefaultErrorHandler：处理HTTP响应错误，错误都会抛出HTTPError类型的异常
HTTPDirectHandler:重定向
HTTPCookieProcessor:用以处理cookie
ProxyHandler:设置代理，默认代理为空
HTTPPasswordMgr:用于管理密码，它维护了用户名和密码的列表
HTTPBasicAuthHandler:用于管理认证，如果一个连接打开时需要认证，那么可以用它来解决认证问题
'''

'''
利用Hanlder可以构建Opener，调用Opener的open()方法就可以完成一次HTTP请求
'''


# 添加代理
proxy_handler = urllib.request.ProxyHandler({
    'http': 'http://127.0.0.1:8888'
})

opener = urllib.request.build_opener(proxy_handler)

try:
    response = opener.open('https://www.baidu.com')
    print('响应状态码: %s' % response.status)
except URLError as e:
    print(e.reason)


# Cookies
cookie = http.cookiejar.CookieJar()
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
cookie_opener = urllib.request.build_opener(cookie_handler)
cookie_response = cookie_opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+'='+item.value)

'''
打印的cookie值如下所示：
BAIDUID=19DDFF643644529B132C63A73927D4AE:FG=1
BIDUPSID=19DDFF643644529B1CD53BDD2714F9A7
H_PS_PSSID=1436_21114_26350_22158
PSTM=1581405412
delPer=0
BDSVRTM=0
BD_HOME=0
cookie值可以以键值对的方式打印，也可以输出为文件格式，主要是Mozilla浏览器的Cookies格式（MozillaCookieJar）以及libwww-perl格式的Cookies文件（LWPCookieJar），只需要替换cookiejar为对应的值即可
'''




