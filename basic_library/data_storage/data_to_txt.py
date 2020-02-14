#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 21:06
# @Author  : lzm
# @File    : data_to_txt.py

from data_storage import request_data as rd

'''
请求数据，将数据保存到txt文件中
'''

data = rd.get_data()
print(data)

# text = '\n'.join(data)
text = str(data)


'''
a表示以追加的方式添加到txt文件中
'''
with open('f:/data.txt', 'a', encoding='utf-8') as file:
    file.write(text)
    file.write('\n'+'='*50+'\n')
