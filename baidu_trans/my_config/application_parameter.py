#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 21:43
# @Author  : lzm
# @File    : application_parameter.py

import yaml

"""
读取配置文件中的内容，赋值给方法或者变量，以供其他地方使用
"""


def load_config():
    """
    加载配置文件
    :return:
    """
    with open('../config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


params = load_config()
# print(params)
