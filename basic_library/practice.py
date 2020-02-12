#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 20:44
# @Author  : lzm
# @File    : practice.py

import requests
import re
import time

'''
练习，使用requests抓取猫眼电影TOP100的电影信息，首页地址：https://maoyan.com/board/4，第二页地址https://maoyan.com/board/4?offset=10，依次类推
'''


def main(offset):
    """
   程序入口
   :return:
   """
    url = 'https://maoyan.com/board/4?offset='+str(offset)
    print(url)
    html = get_one_page(url)
    # print(html)
    parse_html(html)


def get_one_page(url):
    """
    请求单个页面，返回响应的html
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


def parse_html(html):
    """
    使用正则表达式匹配：序号、电影名称、主演、上映时间、评分、图片
    :param html:
    :return:
    """
    # 序号对应的正则:<dd>.*?board-index.*?>(.*?)</i>
    # 图片对应的正则：<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)"
    # 电影名称对应的正则：<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>
    # 主演对应的正则：<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>
    # 评分对应的正则：<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>

    # reg = '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(' \
    #       '.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i> '

    # 以获取序号、图片和电影名的正则测试，加上主演以及评分后正则效率太慢
    reg = '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>'
    pattern = re.compile(reg, re.S)
    items = re.findall(pattern, html)
    print(items)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)
