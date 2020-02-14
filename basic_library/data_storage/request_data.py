#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 20:41
# @Author  : lzm
# @File    : request_data.py

import requests
from pyquery import PyQuery as pq

'''
访问猫眼电影TOP100排行首页，获取序号、电影名称、主演、评分
'''

base_url = 'https://maoyan.com/board/4'


def get_page_heml():
    """
      根据url获取到响应的html
      :return:
    """
    url = base_url
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


def parse_html(html):
    """
    使用pyquery解析需要的屬性值
    :param html:
    :return:
    """
    doc = pq(html)
    items = doc('dl dd').items()
    data = list()
    for item in items:
        sort = item.children('i').text()  # 序號
        print('序號：%s' % sort)
        movie_name = item.find('.name').text()  # 電影名稱
        print('電影名稱： %s' % movie_name)
        main_star = item.find('.star').text()  # 主演
        print('主演： %s' % main_star)
        release_time = item.find('.releasetime').text()  # 上映時間
        print('上映時間： %s' % release_time)
        score = item.find('.integer').text() + item.find('.fraction').text()
        print('評分：%s' % score)
        print('\n' + '=' * 50 + '\n')
        # data.append(tuple(sort, movie_name, main_star, release_time, score))
        dic = {
            'sort': sort,
            'movie_name': movie_name,
            'main_star': main_star,
            'release_time': release_time,
            'score': score
        }
        data.append(dic)
    return data


def get_data():
    html = get_page_heml()
    return parse_html(html)


# get_data()
