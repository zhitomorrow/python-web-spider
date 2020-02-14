#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 21:40
# @Author  : lzm
# @File    : data_to_csv.py

import csv
from data_storage import request_data as rd

'''
数据内容写入到csv中
'''

data = rd.get_data()


def parse_data():
    if len(data) <= 0:
        return None
    keys = data[0].keys()
    rows_list = list()
    for item in data:
        rows_list.append(list(item.values()))
    return {'field': list(keys), 'rows': rows_list}


def write_to_csv():
    text = parse_data()
    field = text.get('field')
    rows = text.get('rows')
    with open('f://data.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(field)
        writer.writerows(rows)


write_to_csv()
