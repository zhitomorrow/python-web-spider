#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 22:30
# @Author  : lzm
# @File    : data_to_redis.py

from redis import StrictRedis

host = '127.0.0.1'
port = 6379
pass_word = '123456'

redis = StrictRedis(host=host, port=port, db=0, password=pass_word)
redis.set('name', 'Tom')
print(redis.get('name'))
