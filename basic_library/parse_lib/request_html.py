#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 13:36
# @Author  : lzm
# @File    : request_html.py

import requests


def get_one_page(url):
    """
    根据url获取到响应的html
    :param url:
    :return:
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/79.0.3945.88 Safari/537.36 '
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


print(get_one_page('https://maoyan.com/board/4'))
