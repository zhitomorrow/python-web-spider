#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 16:01
# @Author  : lzm
# @File    : urllib_parse.py

from urllib import parse

'''
urllib库里还提供了parse模块，它定义了处理URL的标准接口，例如实现URL各部分的抽取、合并以及连接转换，它支持http、https、sftp等多个协议的URL处理
'''

# urlparse
'''
urlparse()方法可以实现URL的识别和分段
'''

result = parse.urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result))  # <class 'urllib.parse.ParseResult'>
print(result)
'''
ParseResult(scheme='https', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
'''

'''
urlparse()方法的参数有三个：
urlstring:必填项，要解析的url
scheme:该参数表示默认的协议，如果要解析的url没有带协议，那么在解析时就会使用默认的协议，也就是scheme的值
allow_fragments:表示是否忽略fragment,如果设置为false，fragment部分就会为空，它会被解析为path、params或者query的一部分，fragment部分为空
'''
result = parse.urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='http', allow_fragments=False)
print(type(result))  # <class 'urllib.parse.ParseResult'>
print(result)
'''
ParseResult(scheme='http', netloc='', path='www.baidu.com/index.html', params='user', query='id=5#comment', fragment='')
'''

# urlunparse
'''
urlparse()的对立方法，它接受的参数是一个可迭代对象，但是参数对象的长度必须是6，否则会抛出参数过多或者过少的问题
'''

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(parse.urlunparse(data))  # http://www.baidu.com/index.html;user?a=6#comment

# urlspilt
'''
这个方法和urlparse()方法非常相似，只不过他不再单独解析params这一部分，只返回5个结果
'''
result = parse.urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
print(result)
'''
SplitResult(scheme='https', netloc='www.baidu.com', path='/index.html;user', query='id=5', fragment='comment')
'''
print(result.scheme, result[0])  # 返回结果是元组类型，可以通过索引的方式获取


# urlunspilt
'''
urlspilt()方法的对立方法
'''
data = ['http', 'www.baidu.com', 'index.html',  'a=6', 'comment']
print(parse.urlunsplit(data))

# urljoin
'''
urljoin(arg1,arg2)，其中arg1是base_url，arg2是新的链接地址，该方法会分析base_url的scheme、netloc以及path这三个内容，并且对新链接缺失的部分进行补充，如果这3项在新的连接里面不存在，
那么就给予补充，如果已经存在，那么就使用新的连接的部分，最终返回结果，而且base_url中的params、query以及fragment是不起作用的
'''
print(parse.urljoin('https://www.baidu.com', 'FAQ.html'))
print(parse.urljoin('https://www.baidu.com', 'https://www.cnblogs.com/geyouneihan/p/12296740.html'))
print(parse.urljoin('www.baidu.com', '?category=2#coment'))
print(parse.urljoin('www.baidu.com#comment', '?category=2'))


# urlencode
'''
序列化请求参数
'''
params = {
    'name': 'Jerry',
    'age': 22
}

base_url = 'https://www.baidu.com?'
url = base_url + parse.urlencode(params)
print('url的结果[%s]' % url)

# parse_qs
'''
反序列化请求参数，返回值是字典
'''
url = 'name=Jerry&age=22'
print(parse.parse_qs(url))  # {'name': ['Jerry'], 'age': ['22']}

# parse_qsl
'''
反序列化请求参数，返回值是元组类型的列表
'''
url = 'name=Jerry&age=22'
print(parse.parse_qsl(url))  # [('name', 'Jerry'), ('age', '22')]

# quote
'''
URL编码，适用于参数中有中文的情况
'''
keyword = '中国加油'
url = 'https://www.baidu.com/s?wd = ' + parse.quote(keyword)
print(url)  # https://www.baidu.com/s?wd = %E4%B8%AD%E5%9B%BD%E5%8A%A0%E6%B2%B9

# unquote
'''
url解码
'''
url = 'https://www.baidu.com/s?wd = %E4%B8%AD%E5%9B%BD%E5%8A%A0%E6%B2%B9'
print(parse.unquote(url))











