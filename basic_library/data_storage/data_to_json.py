#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 21:26
# @Author  : lzm
# @File    : data_to_json.py

import json
from data_storage import request_data as rd

data = rd.get_data()

print(data[0].get('sort'))
# json转换成字符串,indent参数可以格式化json字符串，缩进2个字符,ensure_ascii禁止中文转换为Unicode码
text = json.dumps(data, indent=2, ensure_ascii=False)
print(type(text))

json_data = json.loads(text)  # 字符串转json
print(type(json_data))

with open('f://data.json', 'a', encoding='utf-8') as file:
    file.write(text)
